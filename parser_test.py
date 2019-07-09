#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, pymysql# , re, os, sys, math

db = pymysql.connect(host="localhost", user="shru", passwd="123", db="json_parser", charset='utf8')
cursor = db.cursor()

file_json = open('/home/shru/kmm/json.json', 'r') # Открываем json файл
string_json = file_json.readline() # Читаем файл в одну строку (нахера?) патамушта the JSON object must be str, not 'TextIOWrapper'
list_json = json.loads(string_json) # Откр
lin = '-'*160
print('\n')
id = 0
for dict_item in list_json:
    document = dict_item['document']['receipt']['items']
    doc = dict_item['document']['receipt']
    #inn = doc['userInn']
    usr = doc.get('user')
    if 'user' not in doc:
        usr = 'none'
    else:
        if usr.find('"') > 0:
            a = usr.find('"')
            b = usr.rfind('"')
            usr = usr[a+1:b]
    date = doc['dateTime']
    for modifiers in document:
        name = modifiers['name']
        price = '%.2f'%(modifiers['price']/100)
        quantity = modifiers['quantity']
        summ = '%.2f'%(modifiers['sum']/100)
        id = id + 1
        ids = str(id)
        inn = doc['userInn']
        if len(name) < 2:
            name = 'none'
        if len(usr) < 2:
            usr = 'none'
        
        date = date.replace('-', '')
        date = date.replace(':', '')
        date = date.replace('T', '')
        line = 'insert into fns_data values(' + ids + ",'" + name + "'," + str(price) + "," + str(quantity) + "," + str(summ) + "," + date + ",'" + usr + "'," + inn + ');'
        sql = line
        cursor.execute(sql)
        
        print(line)
#        f = open('/home/shru/kmm/pars_js.txt', 'a')
#        f.write('price' + '\n')
#        f.close()
db.commit() 
db.close()

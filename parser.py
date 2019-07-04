#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json #, re, os, sys, math

file_json = open('/home/shru/kmm/json.json', 'r') # Открываем json файл
string_json = file_json.readline() # Читаем файл в одну строку (нахера?) патамушта the JSON object must be str, not 'TextIOWrapper'
list_json = json.loads(string_json) # Откр

for dict_item in list_json:
    document = dict_item['document']['receipt']['items']
    doc = dict_item['document']['receipt']
    date = doc['dateTime']
    for modifiers in document:
        name = modifiers['name']
        price = '%.2f'%(modifiers['price']/100)
        quantity = modifiers['quantity']
        summ = '%.2f'%(modifiers['sum']/100)
        line = name + " | Цена:" + str(price) + " | Количество:" + str(quantity) + " | Сумма:" + str(summ) + " | Дата:" + date
        print(line)
#        f = open('/home/shru/kmm/pars_js.txt', 'a')
#        f.write('price' + '\n')
#        f.close()

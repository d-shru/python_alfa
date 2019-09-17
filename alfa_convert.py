#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Нужно привесли файл банковской выписки к виду,
   пригодному для загрузки в программу учёта финансов, 
   представить строки в виде:
   
   2018-11-21;;-1940,90;Транспорт:Общественный транспорт;Метро;C;
"""

import re
#import datetime
from datetime import datetime # TODO: выяснить разницу с "import datetime"

def search_date(line):
    """ Ищем все даты в строке и загоняем в список. Дат может быть
    несколько: дата совершения операции, дата поступления платежа и 
    дата подтверждения банком. Нас интересует дата совершения операции,
    поэтому берём последний элемент списка.
    """
    date_list = re.findall('\d{2}\.\d{2}\.\d{4}|\d{2}\.\d{2}\.\d{2}', line)
    date_finded = date_list.pop()
    return (date_finded)


def date_forward(line):
    """ Функция, приводящая дату в нужный формат. 
    В некоторых датах год в формате 'YYYY', поэтому ловим исключение
    """
    try:
        date_forwarded = datetime.strptime(search_date(line), '%d.%m.%y')
    except ValueError:
        date_forwarded = datetime.strptime(search_date(line), '%d.%m.%Y') 
    date_forwarded = datetime.date(date_forwarded)
    return (date_forwarded)


def date_reverse(line):
    """ В некоторых строках даты инвертированы. 
    Приводим к нужному формату.
    """
    date_reversed = datetime.strptime(search_date(line), '%y.%m.%d')
    date_reversed = datetime.date(date_reversed)
    return (date_reversed)


def price_find(line):
    """ Находим в строке цену: разбиваем строку по разделителю и создаём
    список. Цена содержится в последнем элементе списка. Если последний
    элемент списка == 0, то берём предыдущий элемент
    """
    price_list = line.split(';')
    if price_list[-1] == '0':
        price_finded = price_list[-2]
    else:
        price_finded = price_list[-1]
    return (price_finded)


def price_convert(line):
    """ Приводим цену к нужному виду:
    Ищем в цене разделитель, если нет, то добавляем ',00'
    Если после разделителя - одна цифра, то то добавляем '0'
    Если не поступление, то добавляем перед ценой '-'
    """
    price = price_find(line)
    if price.find(',') < 0:
        price = price + ',00'
    else:
        #if price.find(',\d') < 0:
        if re.findall(',\S{2}', price) == []:
            price = price + '0'
              
    if line.find('Основание') < 0 and line.find('командиров') < 0:
        price = "-" + price
    return (price)


def dict_rplace(line, dict):
    """ Сопоставляем каждую строку файла с каждым ключом словаря,
    т.е. берём ключ - ищем в строке, если нет совпадения,то пишем в
    переменную '**'. Если есть совпадение - пишем значение ключа.
    """
    for i in dct.keys():
        if line.find(i) > 0:
            rplace = dct[i]
            break
        else:
            rplace = "**"
    return (rplace)


def line_convert():
    """Открываем файл для конвертирования и подготавливаем его:
    удаляем пробелы в конце каждой строки;
    удаляем точку в конце строки, если есть;
    удаляем символ ';' в конце, если есть.
    """
    for line in open('to_convert.txt'):
        line = line.rstrip()
        if line.endswith('.') is True:
            line = line[:-1]
        if line.endswith(';') is True:
            line = line[:-1]
        
        # Если сумма на удержании банком, то дата стоит в виде: yy.mm.dd
        if line.find(';HOLD;') < 0:  
            date = date_forward(line)
        else:
            date = date_reverse(line)
        
        price = price_convert(line)
        date = str(date)
        rplace = dict_rplace(line, dict)

        line_final = date + ";;" + price + ";" + rplace
           
        """ Формируем сконвертированный файл. В случае, если не все 
        точки оплаты присутствуют в словаре, то выводим их на stdout
        """
        file_result.write(line_final + '\n')
        if line_final.find('**') > 0:
            print (line)
    return (line_final)


""" Открываем список "точки_олаты-категория" для передачи в словарь."""
with open('dict.txt','r') as file_dict:
    dct = eval(file_dict.read())

with open('transcoded_alfa.csv', 'w') as file_result:
    line_convert()
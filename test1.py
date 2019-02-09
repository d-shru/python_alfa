#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Есть строка вида: **1999 Pokupka Uspeshno Summa: 1 940,90 RUR Ostatok: 14 217,94 RUR RU/Podolsk/OAO CPPC 21.11.2018 19:36:19
# Нужно привести её к виду: 2018-11-21;;-1940,90;Транспорт:Общественный транспорт;;C;
#

import sys, os

# вводим строку. ToDo: нужно сделать чтение строк из файла
S = '**1999 Pokupka Uspeshno Summa: 1 940,90 RUR Ostatok: 14 217,94 RUR RU/Podolsk/OAO CPPC 21.11.2018 19:36:19'
print (S)

# Пересоздаём строку без точки в конце строки, если она там есть
def dot():
    if S.endswith('.') == True:
        S = S[:-1]
S = S.rstrip() # Удаляем пробел в конце строки, если есть

# Извлечение и переформатирование даты. Дата всегда в конце строки и в одном формате.
dates = S[-19:]# Ищем дату в конце строки
DD = dates[:2] # Извлекаем день из даты
MM = dates[3:5] # Извлекаем месяц из даты
YYYY = dates[6:10] # Извлекаем год из даты
DATE = YYYY + '-' + MM + '-' + DD + ';;' # Собираем новый формат даты

# Вводим шаблоны для удаления. ToDo:добавлять шаблоны автоматом
str = '**1999 Pokupka Uspeshno Summa: ' # шаблон_1
str2 = 'RUR Ostatok: ' # шаблон_2

# вводим шаблоны для замены
cppc = 'RU/Podolsk/OAO CPPC'
trans = ';Транспорт:Общественный транспорт;;C;'

# Начинаем парсить строку
if S.startswith(str) == True: # Начинается ли строка S с шаблона_1
	b = len(str)  # Считаем длинну шаблона_1
	S = S[b:] # Удаляем из строки шаблон_1

slash1 = (S.find(str2)) # Ищем индекс шаблона_2
slash = (S.find('RU/')) # Ищем индекс первого вхождения RU/
remove = S[slash1:slash] # Выделяем срез для удаления
S = S[:-19]
S = S.replace(remove, '')
S = S.replace(cppc, trans)

semicolon = (S.find(' ;')) # Ищем индекс первого вхождения ";"

semicolon = semicolon + 1 # Переносим пробел из начала строки S (убрать пробелы потом будет легче сразу все из price)
price = S[:semicolon]
S = S[semicolon:] # Откусываем неправильную цену
#S = S.rstrip() # Удаляем пробел в конце строки S

price = price.replace(' ', '') # Убираем пробелы из цены
if ',' not in price: # Если цена без копеек, то добавляем ".00"
    price = '-' + price + ',00'
price = '-' + price

# Собираем строку
S = DATE + price + S
print (S)

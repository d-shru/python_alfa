#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os

L1 = []
L = []
i = 0
for line in open('/home/shru/kmm/sms1_1.txt'):
    line = line.rstrip() # удаляем пробелы в конце каждой строки
    if line.endswith('.') == True: # удаляем точку в конце строки, если есть
        line = line[:-1]
    indx = (line.find('RU/')) # Ищем индекс первого вхождения RU/
    if indx > 0: # Если есть вхождение, то добавляем в список всё , что от RU/ до даты в конце
        #print (indx)
        line = line[indx:-20]
        indx1 = (line.rfind('/'))
        indx1 = indx1+1
        line = line[indx1:]
        line = line.replace(' ','_')
        L.append(line)
        
L.sort() # сортировка списка

[L1.append(item) for item in L if item not in L1] # в новый список без дубликатов 
#print (L1)

for item in L1: print(item)




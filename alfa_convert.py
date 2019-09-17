# -*- coding: utf-8 -*-
#
# Есть строки
# Нужно привести их к виду: 
# 2018-11-21;;-1940,90;Транспорт:Общественный транспорт;Метро;C;
#
import re

with open('/home/shru/kmm/dict.txt','r') as file_dict: 
    dct = eval(file_dict.read())
with open('transcoded_alfa.csv', 'w') as file_result:
    for lines in open('to_convert.txt'):
        lines = lines.rstrip()  # удаляем пробелы в конце каждой строки
        if lines.endswith('.') is True:  # удаляем точку в конце строки, если есть
            lines = lines[:-1]
    
        date = re.findall('\d{2}\.\d{2}\.\d{4}|\d{2}\.\d{2}\.\d{2}', lines)  # ищем все даты в строке и загоняем в список
        date = date.pop()  # берём последний элемент списка (дат может быть несколько)
        indx = date.rindex('.')  # находим индекс разделителя '.'
        mm = date[indx - 2:indx]  # находим месяц
        if lines.find(';HOLD;') < 0:  # если сумма на удержании банком, то дата стоит в виде: yy.mm.dd
            year = date[indx + 1:]  # находим год
            dd = date[indx - 5:indx - 3]  # находим день
        else:
            dd = date[indx + 1:]  # находим год
            year = date[indx - 5:indx - 3]  # находим день
        if len(year) < 4:
            yyyy = year.replace(year, '20' + year)  # если год вида YY, то приводим год к к виду YYYY
        date = yyyy + '-' + mm + '-' + dd + ';;'  # Собираем новый формат даты
    
        # находим в строке цену
        indx1 = lines.rindex(';')  # ищем индекс разделителя в конце строки
        lines = lines.rstrip(';')  # удаляем разделитель
        indx2 = lines.rindex(';')  # снова ищем разделитель
        test = lines[indx2 + 1:indx1]  # между найденными разделителями будет цена
        if test == '0':
            lines = lines.rstrip('0')  # если цена = 0, то удаляем
            lines = lines.rstrip(';')
            indx3 = lines.rindex(';')
            test1 = lines[indx3 + 1:indx2]
            price = test1
        else:
            price = test
        if price.find(',') < 0:  # ищем в цене разделитель, если нет, то добавляем ",00"
            price = price + ',00'
    
        if lines.find('Основание') < 0 and lines.find('командиров') < 0:  # ищем поступления
            price = "-" + price
        # эта фигня сопоставляет каждую строку файла с КАЖДЫМ ключом словаря...
        #т.е. берём ключ - ищем в строке если нет, пишем 0 и
        # берём след. ключ - есть совпадение - пишем значение. смотрим след. ключ - не находим- пишем 0...
        for i in dct.keys():
            if lines.find(i) > 0:
                rplace = dct[i]
                break
            else:
                rplace = "**"
        line = date + price + ";" + rplace
    
        file_result.write(line + '\n')
        if line.find('**') > 0:
            pass
            #print (line)


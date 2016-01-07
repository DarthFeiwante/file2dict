#/usr/bin/env python3
'''
\section{file2dict.py}

\\hyperlink{content}{Content}

Program is intended for transformation of the file into dictionary
Программа предназначена для преобразования файла в словарь Python3

Requirements: python3

Program contains following functions
Программа содержит следующие функции:

\\textcolor{green}{file2dict(name, split\_sign)}

Its input parameters:
Его входными параметрами являются:

name - name of the file to be transformed
name - имя преобразуемого в словарь файла

limiter - final string of the transformation; below this strig rest strings will not be transformed 
(default=lusta, which means that whole file will be transformed)
limiter - строка, ниже которой записи в словарь не вносятся; это именованный аргумент, значение по умолчанию которого - 'lusta', 
означающее, что будет преобразован весь файл.

split\_sign (e.g. ;) - sign of split for the dictionary building; keys are string parts that placed before the sign, and
values - after the sign.
split\_sign (например, ';') - знак разделителя для создания словаря, ключами которого являются части каждой строки,
стоящие до разделителя 'split\_sign', а значениями - части соответствующих строк, стоящие после разделителя.

Result of the function is dictionary with name assigned to the returned object 
Результатом работы данной функции является словарь с именем <имя>: <имя> = file2dict(name, split\_sign)

The program is importable only
Данная программа только импортируемая

\\newpage
'''
def file2dict(name, split_sign, limiter='lusta'):
    d = {}
    l0 = []
    l = []
    for line in open(name):
        if len(line) == 1 or line[0] == '#': continue 
        if limiter in line: break
        elif limiter=='lusta': pass
        key, value = line.split(split_sign)
        d[key] = value.replace('\n', '').lstrip()
        l.append(key)
        l0.append(line)
    file2dict.list = l0
    file2dict.dict_list = l
    file2dict.dict = d


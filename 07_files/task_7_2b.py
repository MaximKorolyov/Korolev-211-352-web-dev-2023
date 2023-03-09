# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""



from sys import argv

ignore = ["duplex", "alias", "configuration"]

read_file, write_file = argv[1],argv[2]


with open(read_file) as f, open(write_file, "w") as dst:
    for line in f:
        f = line.split()
        ignore_str = set(f) & set(ignore)
        
        if not ignore_str and line[0]!="!":
             dst.write(line)
             print(line.rstrip())
             



             


# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""




select = input("Введите Vlan: ")



zapom = []
with open("07_files/CAM_table.txt", "r") as f:
    for line in f:
        mass = line.split()
        if mass and mass[0].isdigit():
            vlan, mac, _, interface = mass
            zapom.append([int(vlan), mac, interface])
            
           
         

for i in range(len(zapom)):
    if zapom[i][0] == int(select):
        print(f"{zapom[i][0]:<10}{zapom[i][1]:20}{zapom[i][2]}")





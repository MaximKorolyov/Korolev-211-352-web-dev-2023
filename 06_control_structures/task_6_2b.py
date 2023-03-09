# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""



valid = False
while valid!=True: 
    ip = input("Введите IP-адресс: ")
    ip = ip.split(".")
    valid = True
    if len(ip) !=4:
        valid = False
    else:
        for i in range(len(ip)-1):
            if not (ip[i].isdigit()):
                valid = False
                break
            if int(ip[i]) < 0 or int(ip[i]) > 255:
                valid = False
                break
                

    if valid == False:
        print("Неправильный IP-адрес, попробуйте снова")

if int(ip[0]) >=1 and int(ip[0]) <= 223:
    print("unicast")

elif int(ip[0]) >=224 and int(ip[0]) <= 239:
    print("multicast")
elif int(ip[0]) == 255:
        flag = True
        for i in range(1,3):
            if int(ip[i]) != 255:
                    flag = False
                    break
        if flag == True:
            print("local broadcast")

elif int(ip[0]) == 0:
    flag = True
    for i in range(1,3):
        if int(ip[i]) != 0:
            flag = False
            break
        if flag == True:
            print("unassigned")

else:
    print("unused")



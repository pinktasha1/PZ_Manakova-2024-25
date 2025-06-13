#напишите программу на пайтон которая считывает текстовый файл с именем 'ips.txt',
#находит в нём все корректные IPv4-адреса(например 192.168.1.1)
#и выводит их в консоль, каждый на новой строке.
# если файл не существует или не содержит корректных ip-адресов, программа должна выводить соответствующие сообщения

import re


def file_exists(filename):
    if FileExistsError(filename):
        print('Файла не существует')


def is_ipv4(ip):
    parts = ip.split('.')
    if len(parts) != 4 or not all(part.isdigit() and 0 <= int(part) < 256 for part in parts):
        print('Некорректный IP-адрес')


with open('ips.txt', 'r') as f:
    text = f.read()

find = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
ip_addresses = re.findall(find, text)
correct_ipv4 = [ip for ip in ip_addresses if is_ipv4(ip)]

if correct_ipv4:
    print("Найденные корректные IPv4-адреса:")
    for ip in correct_ipv4:
        print(ip)
else:
    print('Корректные IP-адреса не найдены')
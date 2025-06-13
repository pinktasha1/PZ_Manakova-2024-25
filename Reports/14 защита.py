import re


def is_ipv4(ip):
    parts = ip.split('.')
    if len(parts) != 4 or not all(part.isdigit() and 0 <= int(part) < 256 for part in parts):
        return False
    else:
        return True


try:
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
except  FileNotFoundError:
    print('Файл не найден')
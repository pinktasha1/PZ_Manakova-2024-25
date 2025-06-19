#Средствами Python реализовать программу для работы с однотабличной БД.
#Программа должна обеспечивать функционал по вводу данных в БД (10 позиций), их
#поиску, удалению и редактированию. При организации поиска, удаления и
#редактирования использовать WHERE, предусмотреть по три SQL-запроса для каждой
#операции. Структура БД указана в каждом варианте.


#Приложение ПРОМЫШЛЕННОСТЬ для автоматизированного учета
#информации о промышленных предприятиях республики. БД содержит таблицу
#Предприятия, имеющую следующую структуру записи: Код предприятия, Наименование
#предприятия, Физический адрес, Филиалы (количество филиалов), Общая числ. персонала,
#Общая стоим. оборудования, Объем выпускаемой продукции, Дата регистрации.

import sqlite3 as sq

conn = sq.connect('PROMISHLENNOST.db')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS predpriatie(
        pred_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL,
        amount_filial INTEGER DEFAULT 1,
        amount_personal INTEGER NOT NULL DEFAULT 1,
        amount_price INTEGER,
        volume INTEGER,
        data DATE NOT NULL
    )
''')
conn.commit()


def add_predpriyatie():
    print("\nДобавление предприятия:")
    pred_id = int(input('Код предприятия: '))
    name = input('Наименование предприятия: ')
    address = input('Физический адрес: ')
    amount_filial = int(input('Количество филиалов: '))
    amount_personal = int(input('Общая численность персонала: '))
    amount_price = int(input('Общая стоимость оборудования: '))
    volume = int(input('Объём выпускаемой продукции: '))
    data = input('Дата регистрации (ГГГГ-ММ-ДД): ')

    cur.execute('''
        INSERT INTO predpriatie 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (pred_id, name, address, amount_filial, amount_personal, amount_price, volume, data))
    conn.commit()
    print("Предприятие добавлено")


def insert_data():
    data = [
        (1, 'МеталлПромСталь', 'ул. Сталеваров, 15', 2, 120, 7500000, 8000, '2020-01-15'),
        (2, 'НефтеХимТех', 'пр. Индустриальный, 3', 1, 300, 25000000, 15000, '2018-05-23'),
        (3, 'ЭлектроЗавод', 'ул. Энергетиков, 42', 3, 500, 34000000, 22000, '2019-11-10'),
        (4, 'АгроМаш', 'с. Зерновое, ул. Полевая, 7', 1, 80, 12000000, 5000, '2021-03-05'),
        (5, 'СтройИнвест', 'ул. Кирова, 10', 4, 230, 19000000, 13000, '2020-09-30'),
        (6, 'ХимПромСоюз', 'пр. Ломоносова, 88', 2, 150, 18000000, 11000, '2022-02-14'),
        (7, 'МашСервис', 'ул. Техническая, 25', 1, 60, 9000000, 4000, '2023-06-01'),
        (8, 'ПищПром', 'ул. Вкусная, 12', 2, 90, 6700000, 7000, '2020-12-20'),
        (9, 'АвтоМехЗавод', 'ш. Северное, 5', 5, 670, 45000000, 30000, '2017-08-18'),
        (10, 'Металлургия-Плюс', 'ул. Металлов, 99', 2, 320, 22000000, 14000, '2021-07-11')
    ]
    cur.executemany('''
        INSERT OR IGNORE INTO predpriatie
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()
    print("10 записей успешно добавлены.")


def search_predpriyatie():
    kod = int(input("Введите код предприятия: "))
    cur.execute("SELECT * FROM predpriatie WHERE pred_id = ?", (kod,))
    pred = cur.fetchone()
    if pred:
        print(f'''
    Код: {pred[0]}
    Наименование: {pred[1]}
    Адрес: {pred[2]}
    Филиалы: {pred[3]}
    Персонал: {pred[4]}
    Стоимость оборудования: {pred[5]}
    Объём продукции: {pred[6]}
    Дата регистрации: {pred[7]}
            ''')
    else:
        print("Предприятие с таким кодом не найдено.")


def update_predpriyatie():
    print("\n[Изменить предприятие]")
    kod = int(input("Код предприятия: "))

    cur.execute("SELECT * FROM predpriatie WHERE pred_id=?", (kod,))
    pred = cur.fetchone()

    if not pred:
        print("Предприятие не найдено")
        return

    print("\nТекущие данные:")
    print(f"1. Наименование: {pred[1]}")
    print(f"2. Адрес: {pred[2]}")
    print(f"3. Кол-во филиалов: {pred[3]}")
    print(f"4. Персонал: {pred[4]}")
    print(f"5. Стоимость оборудования: {pred[5]}")
    print(f"6. Объём продукции: {pred[6]}")
    print(f"7. Дата регистрации: {pred[7]}")

    pole = int(input("\nЧто меняем? (1-7): "))
    novoe = input("Новое значение: ")

    columns = ["name", "address", "amount_filial", "amount_personal", "amount_price", "volume", "data"]

    if 1 <= pole <= 7:
        column_name = columns[pole - 1]
        cur.execute(f"UPDATE predpriatie SET {column_name}=? WHERE pred_id=?", (novoe, kod))
        conn.commit()
        print("Изменения сохранены")
    else:
        print("Ошибка выбора")


def delete_predpriyatie():
    print("\n[Удалить предприятие]")
    kod = int(input("Код предприятия: "))

    cur.execute("DELETE FROM predpriatie WHERE pred_id=?", (kod,))
    conn.commit()

    if cur.rowcount > 0:
        print("Предприятие удалено")
    else:
        print("Предприятие не найдено")


def main_menu():
    while True:
        print("\n====== ПРОМЫШЛЕННОСТЬ ======")
        print("1. Добавить предприятие")
        print("2. Найти предприятие")
        print("3. Изменить данные")
        print("4. Удалить предприятие")

        choice = input("Выберите действие (1-5): ")
        if choice == '1':
            add_predpriyatie()
        elif choice == '2':
            search_predpriyatie()
        elif choice == '3':
            update_predpriyatie()
        elif choice == '4':
            delete_predpriyatie()
            break
        else:
            print("Некорректный ввод.")

if __name__ == "__main__":
    main_menu()
    conn.close()
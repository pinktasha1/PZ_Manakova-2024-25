import sqlite3

conn = sqlite3.connect('tovari.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS tovari')

cur.execute('''
    CREATE TABLE IF NOT EXISTS tovari(
        id_tov INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        amount INTEGER NOT NULL,
        opt_price FLOAT NOT NULL
    )
''')
conn.commit()

data = [
    ('вода', 29.99, 200),
    ('хлеб', 40.99, 750),
    ('молоко', 100.00, 1500)
]
cur.executemany(
    'INSERT INTO tovari (name, amount, opt_price) VALUES (?, ?, ?)',
    data
)
conn.commit()

print("Исходные данные:")
for row in cur.execute('SELECT * FROM tovari'):
    print(row)

updated_data = ('сахар', 15, 45.00, 2)
cur.execute(
    'UPDATE tovari SET name = ?, amount = ?, opt_price = ? WHERE id_tov = ?',
    updated_data
)

print("\nПосле обновления 2-ого товара: ")
for row in cur.execute('SELECT * FROM tovari'):
    print(row)

conn.commit()
conn.close()
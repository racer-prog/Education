import sqlite3

connection = sqlite3.connect("not_telegram_2.db")

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

cursor.execute("DELETE FROM Users WHERE id = ? " , (6,))

cursor.execute("SELECT COUNT(*) FROM Users")
total = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
total_balance = cursor.fetchall()[0]

print(total_balance[0]/total)

connection.commit()
connection.close()
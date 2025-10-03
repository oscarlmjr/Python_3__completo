import sqlite3

from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    # f'SELECT * FROM {TABLE_NAME} LIMIT 2'
    f'SELECT * FROM {TABLE_NAME}'
)

for row in cursor.fetchall():
    # print(row)
    _id, name, weight = row
    print(_id, name, weight)

# row = cursor.fetchall()
# print(row)

print()

cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = "3"'
)
row = cursor.fetchone()
# print(row)
_id, name, weight = row
print(_id, name, weight)

cursor.close()
connection.close()

# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os
from typing import cast

import dotenv
import pymysql
import pymysql.cursors

TABLE_NAME = 'customers'
# CURRENT_CURSOR = pymysql.cursors.SSDictCursor
CURRENT_CURSOR = pymysql.cursors.DictCursor

dotenv.load_dotenv()

connection = pymysql.connect(
	host=os.environ['MYSQL_HOST'],
	user=os.environ['MYSQL_USER'],
	password=os.environ['MYSQL_PASSWORD'],
	database=os.environ['MYSQL_DATABASE'],
	charset='utf8mb4',
	# cursorclass=pymysql.cursors.DictCursor,
	cursorclass=CURRENT_CURSOR,
)

with connection:
	with connection.cursor() as cursor:
		cursor.execute(
			'CREATE TABLE IF NOT EXISTS customers ('
			'id INT NOT NULL AUTO_INCREMENT, '
			'nome VARCHAR(50) NOT NULL, '
			'idade INT NOT NULL, '
			'PRIMARY KEY (id)'
			') '
		)
		# CUIDADO: ISSO LIMPA A TABELA
		cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
	connection.commit()

		# Começo a manipular dados a partir daqui

	# Inserindo um valor usando placeholder e um iterável
	with connection.cursor() as cursor:
		sql = (
			f'INSERT INTO {TABLE_NAME} '
			'(nome, idade) '
			'VALUES '
			'(%s, %s) '
		)
		data = ('Luiz', 18)
		result = cursor.execute(sql, data)
	connection.commit()

	# Inserindo um valor usando placeholder e um dicionário
	with connection.cursor() as cursor:
		sql = (
			f'INSERT INTO {TABLE_NAME} '
			'(nome, idade) '
			'VALUES '
			'(%(name)s, %(age)s) '
		)
		data2 = {
			"age": 37,
			"name": "Le",
		}
		result = cursor.execute(sql, data2)

	connection.commit()

	# Inserindo vários valores usando placeholder e um tupla de dicionários
	with connection.cursor() as cursor:
		sql = (
			f'INSERT INTO {TABLE_NAME} '
			'(nome, idade) '
			'VALUES '
			'(%(name)s, %(age)s) '
		)
		data3 = (
			{"name": "Sah", "age": 33, },
			{"name": "Júlia", "age": 74, },
			{"name": "Rose", "age": 53, },
		)
		result = cursor.executemany(sql, data3)
	connection.commit()

	# Inserindo vários valores usando placeholder e um tupla de tuplas
	with connection.cursor() as cursor:
		sql = (
			f'INSERT INTO {TABLE_NAME} '
			'(nome, idade) '
			'VALUES '
			'(%s, %s) '
		)
		data4 = (
			("Siri", 22, ),
			("Helena", 15, ),
			("Luiz", 18, ),
		)
		result = cursor.executemany(sql, data4)
	connection.commit()

	# Lendo os valores com SELECT
	with connection.cursor() as cursor:
		menor_id = 2
		maior_id = 4

		sql = (
			f'SELECT * FROM {TABLE_NAME} '
			'WHERE id BETWEEN %s AND %s  '
		)
		cursor.execute(sql, (menor_id, maior_id))
		data5 = cursor.fetchall()

	# Apagando com DELETE, WHERE e placeholders no PyMySQL
	with connection.cursor() as cursor:
		sql = (
			f'DELETE FROM {TABLE_NAME} '
			'WHERE id = %s'
		)
		cursor.execute(sql, (1,))
		connection.commit()

		cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

	# Editando com UPDATE, WHERE e placeholders no PyMySQL
	with connection.cursor() as cursor:
		cursor = cast(CURRENT_CURSOR, cursor)

		sql = (
			f'UPDATE {TABLE_NAME} '
			'SET nome=%s, idade=%s '
			'WHERE id=%s'
		)
		cursor.execute(sql, ('Eleonor', 102, 4))
		# cursor.execute(f'SELECT * FROM {TABLE_NAME} ')
		resultFromSelect = cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

		data6 = cursor.fetchall()
		# print('For 1: ')
		for row in cursor.fetchall():
		# for row in cursor.fetchall_unbuffered():
			print(row)
		# cursor.execute(
		# 	f'SELECT id from {TABLE_NAME} ORDER BY id DESC LIMIT 1'
		# )
		lastIdFromSelect = cursor.fetchone()
		# print(lastIdFromSelect)

		# resultFromSelect = cursor.execute(f'SELECT * FROM {TABLE_NAME} ')
			# if row['id'] >= 5:
			# 	break
		# data6 = cursor.fetchall()
		# print()
		# print('For 2: ')
		# cursor.scroll(-1)
		# for row in cursor.fetchall_unbuffered():
		# for row in data6:
			# print(row)

		print('resultFromSelect', resultFromSelect)
		print('len(data6)', len(data6))
		print('rowcount', cursor.rowcount)

		# sql = (
		# 		f'INSERT INTO {TABLE_NAME} '
		# 		'(nome, idade) '
		# 		'VALUES '
		# 		'(%s, %s) '
		# 		)

		# data3 = (
		# 	{"name": "Sah", "age": 33, },
		# 	{"name": "Júlia", "age": 74, },
		# 	{"name": "Rose", "age": 53, },
		# )
		# result = cursor.executemany(sql, data3)
		# cursor.execute(sql, data)

		print('lastrowid', cursor.lastrowid)
		print('lastrowid na mão', lastIdFromSelect)

		# cursor.scroll(-1)
		cursor.scroll(0, 'absolute')
		print('rownumber', cursor.rownumber)

		for row in cursor.fetchall():
			print(row)

	connection.commit()

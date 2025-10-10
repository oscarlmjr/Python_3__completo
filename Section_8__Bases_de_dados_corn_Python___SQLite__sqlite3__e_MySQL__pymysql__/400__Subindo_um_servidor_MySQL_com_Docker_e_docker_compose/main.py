# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os

import dotenv
import pymysql
# import pymysql.cursors

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
	host=os.environ['MYSQL_HOST'],
	user=os.environ['MYSQL_USER'],
	password=os.environ['MYSQL_PASSWORD'],
	database=os.environ['MYSQL_DATABASE'],
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor,
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
		# print(cursor.mogrify(sql, (menor_id, maior_id)))
		data5 = cursor.fetchall()

	# Apagando com DELETE, WHERE e placeholders no PyMySQL
	with connection.cursor() as cursor:
		sql = (
			f'DELETE FROM {TABLE_NAME} '
			'WHERE id = %s'
		)
		# print(cursor.execute(sql, (1,)))
		cursor.execute(sql, (1,))
		connection.commit()

		cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

	# Editando com UPDATE, WHERE e placeholders no PyMySQL
	with connection.cursor() as cursor:
		sql = (
			f'UPDATE {TABLE_NAME} '
			'SET nome=%s, idade=%s '
			'WHERE id=%s'
		)
		cursor.execute(sql, ('Eleonor', 102, 4))
		cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

		for row in cursor.fetchall():
			# _id, name, age = row
			# _id, name, age = row.keys
			# _id, name, age = row.items
			# _id, name, age = row.values
			# print(_id, name, age)
			# print(row['nome'])
			print(row)
	connection.commit()

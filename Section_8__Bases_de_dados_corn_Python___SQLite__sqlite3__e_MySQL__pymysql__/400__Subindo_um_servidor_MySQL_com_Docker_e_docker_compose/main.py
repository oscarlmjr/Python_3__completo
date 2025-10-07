# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
# import os

# import dotenv
import pymysql

# dotenv.load_dotenv()

connection = pymysql.connect(
    host='localhost',
    user='usuario',
    password='senha',
    database='base_de_dados',
	# host=os.environ['MYSQL_HOST'],
    # user=os.environ['MYSQL_USER'],
    # password=os.environ['MYSQL_PASSWORD'],
    # database=os.environ['MYSQL_DATABASE'],
)
# connection.close()

with connection:
    with connection.cursor() as cursor:
        # SQL
        print(cursor)

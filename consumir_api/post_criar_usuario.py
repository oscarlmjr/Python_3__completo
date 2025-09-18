# https://www.youtube.com/watch?v=Qd8JT0bnJGs
# https://github.com/luizomf/simple_api_rest_sqlite
import requests
from pprint import pprint
_print = print
# print = pprint


url = 'http://127.0.0.1:3001/users'

user_data = {
	"nome": "Luiz Otávio",
	"password": "123456",
	"email": "luiz@email.com",
}

response = requests.post(url=url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
	# Sucesso
	print(response.status_code)
	print(response.reason)
	# print(response.text)
	print(response.json())
	# print('Byte', response.content)
else:
	# Erros
	print(response.status_code)
	print(response.reason)
	print(response.text)
	# print('Byte', response.content)

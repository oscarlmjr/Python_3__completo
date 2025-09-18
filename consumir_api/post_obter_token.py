# https://www.youtube.com/watch?v=Qd8JT0bnJGs
# https://github.com/luizomf/simple_api_rest_sqlite
import requests
from pprint import pprint
_print = print
# print = pprint


url = 'http://127.0.0.1:3001/tokens'

user_data = {
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
	response_data = response.json()
	token = response_data['token']

	with open('token.txt', 'w') as file:
		file.write(token)
		
	# print('Byte', response.content)
else:
	# Erros
	print(response.status_code)
	print(response.reason)
	print(response.text)
	# print('Byte', response.content)

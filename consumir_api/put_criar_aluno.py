# https://www.youtube.com/watch?v=Qd8JT0bnJGs
# https://github.com/luizomf/simple_api_rest_sqlite
import requests
from pprint import pprint
from get_token import token

_print = print
# print = pprint


url = 'http://127.0.0.1:3001/alunos/2'

headers = {
	'Authorization': token
}

aluno_data = {
	"nome": "Let",
	# "sobrenome": "Vieira",
	# "email": "luana@email.com",
	# "idade": "50",
	# "peso": "80.04",
	# "altura": "1.90",
}

response = requests.put(url=url, json=aluno_data, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
	# Sucesso
	print(response.status_code)
	print(response.reason)
	# print(response.text)
	print(response.json())
	response_data = response.json()
		
	# print('Byte', response.content)
else:
	# Erros
	print(response.status_code)
	print(response.reason)
	print(response.text)
	# print('Byte', response.content)

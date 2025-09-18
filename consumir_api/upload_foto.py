# https://www.youtube.com/watch?v=Qd8JT0bnJGs
# https://github.com/luizomf/simple_api_rest_sqlite
import requests
from pprint import pprint
from get_token import token
from requests_toolbelt import MultipartEncoder
from mimetypes import MimeTypes

_print = print
print = pprint

mimetypes = MimeTypes()

nome_arquivo = 'python_logo.png'
mimetype_arquivo = mimetypes.guess_type(nome_arquivo)[0]
print(mimetype_arquivo)

multipart = MultipartEncoder(fields={
	'aluno_id': '1',
	'foto': (nome_arquivo, open(nome_arquivo, 'rb'), mimetype_arquivo)
})

url = 'http://127.0.0.1:3001/fotos'

headers = {
	'Authorization': token,
	'Content-Type': multipart.content_type
}


response = requests.post(url=url, headers=headers, data=)

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
	print('Byte', response.content)

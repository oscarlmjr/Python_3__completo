import requests


url = 'http://127.0.0.1:3001/images/1588529894017_11362.png'
nome_arquivo = url.split('/')[-1]

response = requests.get(url)


if response.status_code >= 200 and response.status_code <= 299:
	# Sucesso
	print(response.status_code)
	print(response.reason)
	
	with open(nome_arquivo, 'wb') as file:
		file.write(response.content)
else:
	# Erros
	print(response.status_code)
	print(response.reason)

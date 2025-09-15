import unidecode
import pyperclip
# import unicodedata
# import os


def criar_string(string='', nova_string=''):

	string = input('Digite uma string: ')

	for n in string:
		if n.isalpha() or n.isdigit():
			nova_string += n
		else:
			nova_string += '_'

	nova_string = unidecode.unidecode(nova_string)
	pyperclip.copy(nova_string)
	print(nova_string)
	# print(unidecode.unidecode(nova_string), '\n')
	return criar_string()

criar_string()



# def criar_string(string='', nova_string=''):
#
#	 if nova_string != '':
#		 print(nova_string, '\n')
#
#	 string = input('Digite uma string: ')
#	 for n in string:
#		 if n.isalpha() or n.isdigit():
#			 nova_string += n
#		 else:
#			 nova_string += '_'
#	 import unidecode
#
#	 nova_string = unidecode.unidecode(nova_string)
#	 return criar_string(nova_string=nova_string)
#
#
# criar_string()


# while True:
#
#	 nova_string = ''
#	 string = input('Digite uma string: ')
#
#	 for n in string:
#		 if n.isalpha() or n.isdigit():
#			 nova_string += n
#		 else:
#			 nova_string += '_'
#	 import unidecode
#	 print(unidecode.unidecode(nova_string))
	# print(nova_string, '\n')
	# os.system('pause')
# input()


# texto original
# original = "peça ótimo péssimo não é tão às"
#
# # com unidecode
# processamento_1 = unidecode.unidecode(original)   # *
# print(processamento_1)  # peca otimo pessimo nao e tao as
#
#
# # com unicodedata
# processamento_2 = unicodedata.normalize("NFD", original)
# print(processamento_2)  # peça ótimo péssimo não é tão às
# processamento_2 = processamento_2.encode("ascii", "ignore")
# print(processamento_2)  # b'peca otimo pessimo nao e tao as'
# processamento_2 = processamento_2.decode("utf-8")   # *
# print(processamento_2)  # peca otimo pessimo nao e tao as
#
#
# # texto original
# original = "É o 5º e último. Estava 30°C"
#
# # com unidecode
# processamento_1 = unidecode.unidecode(original)
# print(processamento_1)   # E o 5o e ultimo. Estava 30degC
#
#
# # com unicodedata
# processamento_2 = unicodedata.normalize("NFD", original)
# print(processamento_2)   # É o 5º e último. Estava 30°C
# processamento_2 = processamento_2.encode("ascii", "ignore")
# print(processamento_2)   # b'E o 5 e ultimo. Estava 30C'
# processamento_2 = processamento_2.decode("utf-8")
# print(processamento_2)   # E o 5 e ultimo. Estava 30C

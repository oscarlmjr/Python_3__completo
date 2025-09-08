# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho_arquivo = 'D:\\Desenvolvimento\\curso_python\\secao_4\\187__with_open__context_manager__e_metodos_uteis_do_TextIOWrapper\\'
caminho_arquivo += 'aula187.txt'

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(('Linha 3\n', 'Linha 4\n'))   # iterável
    arquivo.seek(0, 0)   # move o cursor para o início do arquivo
    print(arquivo.read())
    print('Lendo')
    arquivo.seek(0, 0)
    print(arquivo.readline())
    print(arquivo.readline(), end='')   # similar ao __next__
    print(arquivo.readline().strip())
    print(arquivo.readline())
    print(arquivo.readline(),'não retorna Error/write(lines)', sep='')
    print(arquivo.readline(),'não retorna Error/write(lines)')

print('\n', '#' * 20, '\n')

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())

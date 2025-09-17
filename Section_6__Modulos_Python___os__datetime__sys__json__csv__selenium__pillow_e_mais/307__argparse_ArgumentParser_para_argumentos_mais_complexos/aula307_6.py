# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser


parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra "Olá mundo" na tela',
    type=str,
    metavar='STRING',
    default='Olá mundo'
)
args = parser.parse_args()

if args.basic is None:
    print('Você não passou o valor de basic.')
    print(args.basic)
else:
    print('O valor de basic:', args.basic)


# (Parte 2) Threads - Executando processamentos em paralelo
from threading import Thread
from time import sleep


def vai_demorar(texto: str, tempo: int):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 5))
t1.start()

t2 = Thread(target=vai_demorar, args=('Olá mundo 2!', 1))
t2.start()

t3 = Thread(target=vai_demorar, args=('Olá mundo 3!', 2))
t3.start()

for i in range(10):
    print(i)
    sleep(.5)



def gen1():
    print('gen1')
    yield 1
    print('gen3')


def gen2():
    print('gen2')
    yield from gen1()
    print('2')
    yield 3   # yield _ == None


g = gen2()

# for n in g:
#     print(n)

# print(next(gen2()))
print(next(g))
print(next(g))

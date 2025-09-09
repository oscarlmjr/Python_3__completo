a = b = c = d = 0

for _ in range(3):

    c = int(input('Digite um comprimento de um lado de um triângulo: '))
    # 3, 2, 1
  # 0  3  0   3  3  0
  # 3  2  0   2  2  0
  # 2  1  3   1  1  3
    a, b, c = b, c, d
    if a > c:
        d = a

    print(a, b, c, d)

# numero = '.god yzal eht revo spmuj xof nworb kciuq ehT'
#
# d = i = ''
#
# for n in numero:
#     i, d = n, i
#     i += d
#
# print(i)

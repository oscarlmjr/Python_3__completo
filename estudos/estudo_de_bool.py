
print(f'{bool([])=}')
print(f'{bool([[], []])=}\n')
# print(None == 0)
# print(None is False)
# print(False == False)

##########################

print(bool is bool, type(bool))
print(isinstance(bool, bool), '\n')

print(True is True)
print(True is False, type(True), type(False))
print(False is True, type(True), type(False))
print(False is False, '\n')

print(True is bool, type(True), type(bool))
print(isinstance(True, bool), type(True), type(bool))
print(False is bool, type(False), type(bool))
print(isinstance(False, bool), type(False), type(bool), '\n')

print(True is int, type(True), type(int))
print(isinstance(True, int))
print(bool is int)
print(isinstance(bool, int), '\n')

print(True is float, type(True), type(float))
print(isinstance(True, float), '\n')

print(True is str, type(True), type(str))
print(isinstance(True, str), '\n')

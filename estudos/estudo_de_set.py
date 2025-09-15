
conjunto = set()
print(conjunto, type(conjunto))
print()

# conjunto = {{"a": "a"}, ['b', 'c'], 1, 2, 3, True, None,}	# TypeError: 
# unhashable type: 'list'   # TypeError: unhashable type: 'dict'

conjunto = {"a", 1, 2, 3, True, None, False}
print(conjunto, type(conjunto))
print()

conjunto = set()
conjunto.add(1)
# conjunto.add(2, 3)   # TypeError: set.add() takes exactly one argument (2 
#given)
print(conjunto, type(conjunto))

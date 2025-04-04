###### Arithmetic ######
add = lambda x, y : x + y
print(f'Rslt = {add(5, -9)}')

###### List Comprehension ######
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = list(map(lambda x: x ** 2, num_list))
print(f'\n Squares: \n {squares}')

###### Lambda Key ######
dict_alpha = [(1, 'z'), (2, 'a'), (3, 'b')]
sorted_list = sorted(dict_alpha, key=lambda x: x[1])
print(f'\n Sorted List: \n {sorted_list}')

p_info = [
    (1, {'name': 'Charlie', 'email': 'charlie@example.com'}),
    (2, {'name': 'Bob', 'email': 'cutebob@example.com'}),
    (3, {'name': 'Alice', 'email': 'dealice@example.com'})
]

pii = [
    (
        {'name': 'Charlie', 'email': 'charlie@example.com'},
        {'name': 'Bob', 'email': 'cutebob@example.com'},
        {'name': 'Alice', 'email': 'dealice@example.com'}
    )
]

# sort by name
contacts = sorted(p_info, key=lambda x: x[1]['name'])
print(f'\n p_info: \n {contacts}')
contacts = sorted(pii, key=lambda x: x[1:])
print(f'\n pii: \n {contacts}')

# sort by email
contacts = sorted(p_info, key=lambda x: x[1]['email'])
print(f'\n p_info: \n {contacts}')
contacts = sorted(pii, key=lambda x: x[2:])
print(f'\n pii: \n {contacts}')

####### Filter ######
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
hash_keys = list(filter(lambda x: x % 3 == 0, num_list))
print(f'\n Hash_keys for pos: \n {hash_keys}')

####### Dictionary ######
ops = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x-y
}
print(f'\n {ops["+"](2, -12)}')
print(f'\n {ops["-"](2, -12)}')

####### Reduce ######
from functools import reduce
num_list = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, num_list)
print(f'\n reduce: Product: {product}')
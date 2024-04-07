# Tuple: ordered, immutable, allows duplicate elements

import timeit

my_tuple = 'Reira', 22, 'Tokyo', 'singer', 'Trapnest', 'vocalist'
print(type(my_tuple))

tuple1 = ('Reira', )
print(type(tuple1))

tuple2 = tuple(['Shin', 15, 'Tokyo'])

item = my_tuple[-1]
print(item)

#my_tuple[0] = 'Nana' # TypeError, immutable

for x in my_tuple:
    pass

if 'Reira' in my_tuple:
    print('yes')
else:
    print('no')

print(len(my_tuple))
print(my_tuple.count('singer'))

print(my_tuple.index('Tokyo'))

my_list = list(my_tuple)
print(my_list)

tuple_slice = my_tuple[2:5:2]
print(tuple_slice)

name ,age, city = my_tuple[0:3]
print(name)
print(age)
print(city)

print(timeit.timeit(stmt="['Reira', 22, 'Tokyo']", number= 1000000))
print(timeit.timeit(stmt="('Reira', 22, 'Tokyo')", number= 1000000))

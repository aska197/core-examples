#Lists: ordered, mutable, allows duplicate elements

my_list = ['banana', 'cherry', 'apple']

index = my_list[-1]
print(index)

for item in my_list:
    print(item)

if 'banana' in my_list:
    print('yes')
else:
    print('no')

len(my_list)
my_list.append('lemon')
print(my_list)

my_list.insert(1, 'bluberry')
print(my_list)

my_list.pop()
my_list.remove('cherry')

my_list.reverse()
my_list.sort()

new_list = sorted(my_list)

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sliced = numbers_list[::-1]
print(sliced)

list_copy = my_list

list_copy.append('orange')
print(my_list)

square_numbers = [i*i for i in numbers_list]
print(square_numbers)



name = input('Enter your full name: ')
name_len = len(name)

name_find = name.find('w')
name_reverse_find = name.rfind('w')
name = name.capitalize()
name = name.upper()
name = name.lower()
is_name_digit = name.isdigit()
is_name_alpha = name.isalpha()

phone = input('Enter your phone number: ')

phone_count = phone.count('+')
phone_replace = phone.replace('-', ' ')


print(name_len)
print(name_find)
print(name_reverse_find)
help(str)

username = input('Enter a username: ')

if len(username) > 12:
    print("Your username can't be more that 12 characters")
elif not username.find(' ') == -1:
    print("Your username can't cointain spaces")
elif not username.isalpha():
    print("Your username can't contian numbers")
else:
    print(f'Welcome {username}')




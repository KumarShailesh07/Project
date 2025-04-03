import random 
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'

length =  int(input('Enter the length of password: '))
password = ''

for i in range(length):
    password += random.choice(chars)

print(password)
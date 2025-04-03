#to take the length of a list
n = int(input('Enter the length of a list:'))
numbers = []

for i in range(0,n):
    print('Enter the list value at location ',i,':')
    #to take input as float
    item = float(input())
    #add number in list at last position
    numbers.append(item)
print('List is :',numbers)
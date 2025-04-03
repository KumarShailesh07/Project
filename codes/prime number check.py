def prime_number(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return "This is not a prime number"
        return "This is a prime number"
    else:
        return "This is not a prime number"
    
num = int(input("Enter the number:"))
print(prime_number(num))
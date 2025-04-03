num = int(input("Enter any number:"))
last_digit = num%10
print("Last digit of a number is:",last_digit)

if last_digit%3 == 0:
    print("Last digit will be divisible by 3")
else:
    print("Last digit will not be divisible by 3")
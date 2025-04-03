def addition(a,b):
    return a+b
def substraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def floor_division(a,b):
    return a//b
def exponential(a,b):
    return a**b
def modulo(a,b):
    return a%b

a = float(input("Enter The First Number:"))
b = float(input("Enter The Second Number:"))
operation = int(input("Enter:\n1->Addition\n2->Substraction\n3->Multiplication\n4->Division\n5->Floor Division\n6->Exponential\n7->Modulo :"))

if operation == 1:
    print(f"Sum of {a} an{b} is:",addition(a,b))
elif operation == 2:
    print(f"Difference of {a} and {b} is:",substraction(a,b))
elif operation == 3:
    print(f"Multiplication of {a} and {b} is:",multiplication(a,b))
elif operation == 4:
    print(f"Division of {a} and {b} is:",division(a,b))
elif operation == 5:
    print(f"Floor Division of {a} and {b} is:",floor_division(a,b))
elif operation == 6:
    print(f"Exponent/Power of {a} to {b} is:",exponential(a,b))
elif operation == 7:
    print(f"Modulo of {a} and {b} is:",modulo(a,b))
else:
    print("Invalid Input!")
print('Welcome To The Unit Converter')

def meter_feet():
    meters = float(input('Enter meters: '))
    feet = meters * 3.28084
    print(f'{meters} meters : {feet:.2f} feet')

def kilometers_miles():
    kilometers = float(input('Enter kilometers: '))
    miles = kilometers * 0.621371
    print(f'{kilometers} kilometers : {miles:.2f} miles')

def kilograms_pounds():
    kilograms = float(input('Enter kilograms: '))
    pounds = kilograms * 2.20462
    print(f'{kilograms} kilograms : {pounds:.2f} pounds')

def celsius_Fahrenheit():
    celsius = float(input('Enter celsius: '))
    fahrenheit = (celsius * 9/5) + 32
    print(f'{celsius} celsius : {fahrenheit:.2f} fahrenheit')

def Fahrenheit_celsius():
    fahrenheit = float(input('Enter fahrenheit: '))
    celsius = (fahrenheit - 32) * 5/9
    print(f'{fahrenheit} fahrenheit : {celsius:.2f} celsius')

def hours_minutes():
    hours = float(input('Enter hours: '))
    minutes = hours * 60
    print(f'{hours} hours : {minutes:.2f} minutes')

def minutes_hours():
    minutes = int(input('Enter minutes: '))
    hours = minutes / 60
    print(f'{minutes} minutes : {hours:.2f} hours')

while True:
    user_input = int(input('1:meters to feet\n2:kilometers to miles\n3:kilograms to pounds\n4:Celsius to Fahrenheit\n5:Fahrenheit to Celsius\n6:hours to minutes\n7:minutes to hours\n8:Exit // '))

    if user_input == 1 :
        meter_feet()
    elif user_input == 2 :
        kilometers_miles()
    elif user_input == 3 :
        kilograms_pounds()
    elif user_input == 4 :
        celsius_Fahrenheit()
    elif user_input == 5 :
        Fahrenheit_celsius()
    elif user_input == 6 :
        hours_minutes()
    elif user_input == 7 :
        minutes_hours()
    elif user_input == 8 :
        print('Quiting...')
        break
    else:
        print('Invalid input')
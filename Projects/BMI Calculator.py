#first create function for calculate bmi
#inside the funchtion we can calculate bmi
#and give output according to bmi value by using if else
#if user give value of height 0 then raise error height not be zero
#now take the values from user such as weight , height
#if user give invalid error then raise value error

def calculate_bmi(weight,height):
    try:
        bmi = weight/(height*height)
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
            
        return bmi, category
    except ZeroDivisionError:
        return "Height not be zero"
    
#To get user input
try:
    weight = int(input("Enter the weight in Kg: "))
    height = int(input("Enter height in meter: "))

    bmi,category = calculate_bmi(weight,height)

    if bmi :
        print(f"Your BMI is {bmi:.2f}")
        print(f"Category: {category}")
    else:
        print(category)
    
except ValueError:
    print("Invalid input!")
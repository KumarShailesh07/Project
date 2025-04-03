#To get student percentage
marks_percentage = float(input("Enter your percentage:"))
#check the grade according to their percentage obtained
if marks_percentage>90:
    print("You obtain A Grade")
elif marks_percentage>80 and marks_percentage<=90:
    print("You obtain B Grade")
elif marks_percentage>70 and marks_percentage<=80:
    print("You obtain C Grade")
else:
    print("You obtain D Grade")
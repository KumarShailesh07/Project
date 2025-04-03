def age_calculator(y,m,d):  # d -> date , m -> month , y -> year
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y,m,d)
    age = int((today - dob).days/365.25)
    print(f"You are {age} year old.")

print("-----Welcome To Age Calculator-----")
y = int(input("Enter the year:"))
m = int(input("Enter the month:"))
d = int(input("Enter the date:"))

age_calculator(y,m,d)
# Taking the total number of unit used by user
unit_used = int(input("Enter the number of unit used:"))

if unit_used >= 0 and unit_used <= 100:
    total_bill = (unit_used-100)*0
elif unit_used > 100 and unit_used <= 200:
    total_bill = (unit_used-100)*5
elif unit_used > 200:
    total_bill = (unit_used-200)*10
print("Amount Pay",500+total_bill)

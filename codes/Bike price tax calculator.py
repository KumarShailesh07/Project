#To get price of a bike 
bike_price=int(input("Enter the price of a bike:"))
#To check the tax amount
#And print total amount of price of a bike including tax
if bike_price>100000:
    road_tax=(bike_price*15)/100
    print("Road tax is:",road_tax)
    total_price=bike_price+road_tax
    print("Total price of bike including road tax of 15% is:{}".format(total_price))
elif bike_price>50000 and bike_price<=1000000:
    road_tax=(bike_price*10)/100
    print("Road tax is:",road_tax)
    total_price=bike_price+road_tax
    print("Total price of bike including road tax of 10% is:{}".format(total_price))
else:
    road_tax=(bike_price*5)/100
    print("Road tax is:",road_tax)
    total_price=bike_price+road_tax
    print("Total price of bike including road tax of 5% is:{}".format(total_price))
# collection of item in restrurent
menu = {
    'Burger':60,
    'Pizza':120,
    'Coffee':80,
    'Tea':20,
    'Chowmine':70
    }

print('-----Welcome To Shailesh Restrurent-----')
print('Menu:\nBurger\t= Rs60\nPizza\t= Rs120\nCoffee\t= Rs80\nTea\t= Rs20\nChowmine = Rs70')

order_total = 0
while True:
    order = input('Do you want to order anything?[Yes/No]:').title()
    if order == 'Yes':
        item = input('Enter the item:').title()
        if item in menu:
            order_total += menu[item]
            print(f'Your order {item} is placed')
        else:
            print(f'{item} is unavailable.\nPlease order something else from menu.')
    elif order == 'No':
        break
    
print(f'Please pay Rs{order_total} at counter.')
print('--------Thank You--------')
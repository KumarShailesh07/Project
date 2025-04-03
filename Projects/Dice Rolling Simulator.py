import random

while True:
    def roll_die():
        return random.randint(1, 6)

    print('Rolling a die...')
    result = roll_die()
    print(f'You rolled a {result}')

    while True:  # Loop to handle invalid inputs for another roll
        another_roll = input('Want to roll dice again [Y/N]: ').upper()

        if another_roll == 'Y':
            break  # Exit the input loop and roll again
        elif another_roll == 'N':
            print('Thank you for playing...')
            exit()  # Exit the program
        else:
            print('Invalid input, please enter Y for Yes or N for No.')

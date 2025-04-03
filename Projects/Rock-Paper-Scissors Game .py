import random

print('Welcome to Rock-Paper-Scissors Game!')
score = 0
while True:
    #user choose exit to quit game
    user_choice = input('Enter your choice (Rock, Paper, Scissors or Exit): ').title()

    word = ['Rock','Paper','Scissors']
    comp_choose = random.choice(word).title()
    print(f'Computer choice: {comp_choose}')

    if user_choice not in word and user_choice != 'Exit':
        print("Invalid choice! Please choose Rock, Paper, or Scissors.")
        continue
    elif user_choice == 'Rock' and comp_choose == 'Scissors' :
        print('You chose Rock, the computer chose Scissors. You win!')
        score += 1
    elif user_choice == 'Scissors' and comp_choose == 'Paper' :
        print('You chose Scissors, the computer chose Paper. You win!')
        score += 1
    elif user_choice == 'Paper' and comp_choose == 'Rock' :
        print('You chose Paper, the computer chose Rock. You win!')
        score += 1
    elif user_choice == comp_choose:
        print(f"It's a tie! Both chose {user_choice}.")
    elif user_choice == 'Exit':
        break
    else:
        print('You lose!')
        print('Try again.....')
        
print(f'Your score is: {score}')
print('Thank You For Playing Rock-Paper-Scissors Game')

'''
Rock beats Scissors.

Scissors beats Paper.

Paper beats Rock.'
'''

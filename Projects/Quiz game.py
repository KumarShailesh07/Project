print('-----Welcome To The Quiz Game-----')

score = 0
while True:
    user_input = input('Do you want to play game?[Yes/No]:').title()
    if user_input == 'Yes':
        question = print('Which planet is known as the "Red Planet"?')
        answer = input('Answer:').title()
        if answer == 'Mars':
            print('Your answer is correct.')
            score += 1
        else:
            print('Your answer is incorrect.')

        question = print('What is the chemical symbol for water?')
        answer = input('Answer:').title()
        if answer == 'H2O':
            print('Your answer is correct.')
            score += 1
        else:
            print('Your answer is incorrect.')

        question = print('Who wrote the play "Romeo and Juliet"?')
        answer = input('Answer:').title()
        if answer == 'William Shakespeare':
            print('Your answer is correct.')
            score += 1
        else:
            print('Your answer is incorrect.')

        question = print('What is the capital city of Japan?')
        answer = input('Answer:').title()
        if answer == 'Tokyo':
            print('Your answer is correct.')
            score += 1
        else:
            print('Your answer is incorrect.')

        question = print('Which number is the only even prime number?')
        answer = input('Answer:').title()
        if answer == '2':
            print('Your answer is correct.')
            score += 1
            break
        else:
            print('Your answer is incorrect.')
            break

    elif user_input == 'No':
        print('Quiting Quiz Game...')
        break

    else:
        print('Invalid Input!')

print(f'Your score is {score} out of 5.')
print('-------Thank You-------')
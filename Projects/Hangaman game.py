import random

word = ['python','ruby','java','kotlin']

chosen_word = random.choice(word)
display_word = ['_' for _ in chosen_word]
attempts = 8

print('-----Welcome To Hangman Game-----')

while attempts > 0 and '_' in display_word:
    print('\n'+' '.join(display_word))
    guess = input('Guess the letter:').lower()
    if guess in chosen_word:
        for index,letter in enumerate(chosen_word):
            if letter == guess:
                 display_word[index]  = guess #reveal after
    else:
        print('The letter does not appear in word')
        attempts -= 1

if '-' not in chosen_word:
    print('You guessed the word')
    print(''.join(display_word))
    print('You Survived')
else:
    print('You ran out of attempts. The word are: '+ chosen_word)
    print('You Lost!')  
import random
import os  # Importing os to check if file exists

def game():
    print('You are playing the game...')
    score = random.randint(1, 80)
    
    # Check if the file exists
    if not os.path.exists('hiscore.txt'):
        with open('hiscore.txt', 'w') as f:  # Create an empty file
            f.write('0')

    # Read the high score from the file
    with open('hiscore.txt', 'r') as f:
        hiscore = f.read()
        if hiscore.strip():  # Check if the file has content
            hiscore = int(hiscore)
        else:
            hiscore = 0
    
    print(f'Your score is: {score}')
    if score > hiscore:
        print('Congratulations! You set a new high score!')
        with open('hiscore.txt', 'w') as f:
            f.write(str(score))
    else:
        print(f'The high score remains: {hiscore}')

    return score

game()
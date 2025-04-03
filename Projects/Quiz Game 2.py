print('-----Welcome To My Quiz-----')

quiz_questions = [
    {
        'questions': 'What is the largest planet in our solar system?',
        'options': ['a) Earth', 'b) Jupiter', 'c) Saturn', 'd) Neptune'],
        'Answer': 'b'
    },
    {
        'questions': 'Who is known as the Father of Computers?',
        'options': ['a) Alan Turing', 'b) Charles Babbage', 'c) John von Neumann', 'd) Blaise Pascal'],
        'Answer': 'b'
    },
    {
        'questions': 'What is the chemical formula for table salt?',
        'options': ['a) NaCl', 'b) H2SO4', 'c) CO2', 'd) KCl'],
        'Answer': 'a'
    },
    {
        'questions': 'What is the name of the first artificial satellite launched into space?',
        'options': ['a) Voyager', 'b) Apollo 11', 'c) Sputnik 1', 'd) Hubble'],
        'Answer': 'c'
    },
    {
        'questions': 'What is the capital of Australia?',
        'options': ['a) Sydney', 'b) Canberra', 'c) Melbourne', 'd) Brisbane'],
        'Answer': 'b'
    },
    {
        'questions': 'Who painted the famous artwork "The Starry Night"?',
        'options': ['a) Vincent van Gogh', 'b) Pablo Picasso', 'c) Leonardo da Vinci', 'd) Claude Monet'],
        'Answer': 'a'
    },
    {
        'questions': 'In which year did India gain independence?',
        'options': ['a) 1945', 'b) 1947', 'c) 1950', 'd) 1952'],
        'Answer': 'b'
    },
    {
        'questions': 'What is the smallest unit of life in biology?',
        'options': ['a) Atom', 'b) Molecule', 'c) Cell', 'd) Tissue'],
        'Answer': 'c'
    },
    {
        'questions': 'Which instrument is used to measure atmospheric pressure?',
        'options': ['a) Thermometer', 'b) Barometer', 'c) Hygrometer', 'd) Anemometer'],
        'Answer': 'b'
    },
    {
        'questions': 'What is the name of the longest river in the world?',
        'options': ['a) Nile', 'b) Amazon', 'c) Yangtze', 'd) Mississippi'],
        'Answer': 'a'
    }
]

def run_quiz(quiz_questions):
    score = 0
    for question in quiz_questions:
        print(question['questions'])
        for option in question['options']:
            print(option)
        answer = input('Enter the answer from (A,B,C and D): ').lower()
        if answer == question['Answer']:
            print('Your answer is correct!')
            score += 1
        else:
            print(f'Your answer is incorrect!')
            print(f'The correct answer is {question['Answer']}')
    print(f'You score {score} out of {len(quiz_questions)}')
            
run_quiz(quiz_questions)

print('-----Thank You For Playing-----')
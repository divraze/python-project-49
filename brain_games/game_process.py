import prompt


def game_process(question_answer, manual):
    name = prompt.string(
f'''Welcome to the Brain Games!
May I have your name? '''
)
    print(f'Hello, {name}!')
    print(f'{manual}')

    i = 0
    
    while i < 3:
        question, answer = question_answer()
        user_answer = prompt.string(
    f'''Question: {question}
Your answer: '''
        )

        if user_answer == str(answer):
            i += 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}!')









    'Answer "yes" if the number is even, otherwise answer "no".',
    'What is the result of the expression?',
    'Find the greatest common divisor of given numbers.',
    'What number is missing in the progression?',
    'Answer "yes" if given number is prime. Otherwise answer "no".'

import prompt


ROUNDS = 3


def run_game(question_answer, manual):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')

    print(f'Hello, {name}!\n'
          f'{manual}')

    i = 0

    while i < ROUNDS:
        question, answer = question_answer()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')

        if user_answer == str(answer):
            i += 1
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(."
                f" Correct answer was '{answer}'.\nLet's try again, {name}!")
            break
    if i == ROUNDS:
        print(f'Congratulations, {name}!')

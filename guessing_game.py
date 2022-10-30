import random
import statistics


players_name = []

players_score = {}

def start_game():
    print('''\n\t*** WELCOME LADIES AND GENTLEMEN TO THE GUESSING NUMBER GAME ***\n''')
    ranking()
    magic_number = random.randrange(1,101)
    number_guesses = 0
    name = input('Would you be so kind of telling me your name please? ')
    players_name.append(name)
    print(f'Alright {name}!! I hope you are ready... Let is beging!')
    while ValueError or magic_number != guess:
        try:
            guess = int(input('Please enter an integer between 1 and 100: '))
            if guess not in range(1,101):
                print('Please you must enter and integer between 1 and 100')
                guess = int(input('Try again please: '))
        except ValueError:
            print('Please you must enter and integer between 1 and 100')
        else:
            if magic_number > guess:
                print('Try another number, higher this time')
                number_guesses += 1

            elif magic_number < guess:
                print('Try another number, lower this time')
                number_guesses += 1
            else:
                print('Well done you guessed the right number!!!')












def ranking():
    print('''\t\t\tThese are the TOP 3 PLAYERS\n''')
    pass



if __name__ == '__main__':
    start_game()







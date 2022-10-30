import random
import statistics


players_name = []

players_score = {}





def start_game():
    print('''\n\t*** WELCOME LADIES AND GENTLEMEN TO THE GUESSING NUMBER GAME ***\n''')
    ranking(players_score)
    number_guesses = 0
    again = 'y'
    while again == 'y':
        magic_number = random.randrange(1, 101)
        name = input('Would you be so kind of telling me your name please? ')
        players_name.append(name)
        print(f'Alright {name}!! I hope you are ready... Let us beging!')
        while (ValueError or magic_number != guess):
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
                    continue

                elif magic_number < guess:
                    print('Try another number, lower this time')
                    number_guesses += 1
                    continue

                else:
                    print('Well done you guessed the right number!!!')
                    players_score[name] = number_guesses
                    data(number_guesses, players_score)
                    print('\nAfter your performance the current ranking looks like this:\n')
                    ranking(players_score)
                    while ValueError:
                        try:
                            again = input('\nWould you like to play again[y/n]? ')
                            if again != 'y' and again != 'n':
                                raise ValueError("Please enter 'y' for 'yes' or 'n' for 'no' ")
                        except ValueError as err:
                            print(f'{err}')
                        else:
                            if again == 'n':
                                print('\nVery well then... THE GAME IS OVER\n')
                                break
                            else:
                                break
            break













def data(number_guesses, players_score):
    results = []
    for value in players_score.values():
        results.append(value)
    print(f'''Here are some statistics:
     \rNumber of attempts: {number_guesses}
     \rMean: {statistics.mean(results)}
     \rMedian: {statistics.median(results)}
     \rMode: {statistics.mode(results)}''')





def ranking(players_score):
    i = 0
    print('''\t\t\tThese are the TOP 3 PLAYERS\n''')
    sorted(players_score)
    while i < 3:
        if i == 0:
            medal = 'GOLD'
        elif i == 1:
            medal = 'SILVER'
        elif i == 2:
            medal = 'BRONZE'
        for players, score in players_score.items():
            print(f'{i+1}. {players} **\033[1m{score}\033[0m** --> MEDAL OF {medal}')
        i += 1




if __name__ == '__main__':
    start_game()







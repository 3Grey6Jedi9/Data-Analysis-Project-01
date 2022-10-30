import random
import statistics


players_name = []

players_score = {}





def start_game():
    print('''\n\t*** WELCOME LADIES AND GENTLEMEN TO THE GUESSING NUMBER GAME ***\n''')
    ranking(players_score)
    again = 'y'
    while again == 'y':
        number_guesses = 0
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
                            again = input('\nWould you like to play again[y/n]? ').lower()
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
     \rMode: {statistics.multimode(results)}''')





def ranking(players_score):
    i = 1
    print('''\t\t\tThese are the TOP 3 PLAYERS\n''')
    top_players = {}
    while len(top_players) < len(players_score):
        for key, value in players_score.items():
            for k, v in players_score.items():
                if value <= v:
                    continue
                else:
                    break
            for kt, vt in top_players.items():
                if value >= vt:
                    continue
                else:
                    break
            top_players[key] = value
    for players, score in top_players.items():
        if i == 1:
            medal = 'GOLD'
        elif i == 2:
            medal = 'SILVER'
        elif i == 3:
            medal = 'BRONZE'
        print(f'{i}. {players} **\033[1m{score}\033[0m** --> MEDAL OF {medal}')
        i += 1
        if i > 3:
            break




if __name__ == '__main__':
    start_game()







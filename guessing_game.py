import random
import statistics


players_name = []

players_score = {}





def start_game():
    '''This is the main function that runs the game'''
    print('''\n\t*** WELCOME LADIES AND GENTLEMEN TO THE GUESSING NUMBER GAME ***\n''')
    ranking(players_score)
    again = 'y'
    while again == 'y':
        number_guesses = 0
        magic_number = random.randrange(1, 101)
        name = input('Would you be so kind of telling me your name please? ')
        players_name.append(name)
        print(f'\nAlright {name}!! I hope you are ready... Let us beging!\n')
        while (ValueError or magic_number != guess):
            try:
                guess = int(input('Please enter an integer between 1 and 100: '))
                if guess not in range(1,101):
                    print('\nPlease you must enter and integer between 1 and 100\n')
                    continue
            except ValueError:
                print('\nPlease you must enter and integer between 1 and 100\n')
            else:
                if magic_number > guess:
                    print('\nTry another number, higher this time\n')
                    number_guesses += 1
                    continue

                elif magic_number < guess:
                    print('\nTry another number, lower this time\n')
                    number_guesses += 1
                    continue

                else:
                    number_guesses += 1
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
    '''This function manages the statistical data'''
    results = []
    for value in players_score.values():
        results.append(value)
    print(f'''Here are some statistics:
     \rNumber of attempts: {number_guesses}
     \rMean: {statistics.mean(results)}
     \rMedian: {statistics.median(results)}
     \rMode: {statistics.multimode(results)}''')






# RANKING FUNCTION

def ranking(players_score):
    '''This function was created for managing the ranking'''
    i = 1
    print('''\t\t\tThese are the TOP 3 PLAYERS\n''')
    top_players = {}
    L = []
    K = []
    for values in players_score.values():
        L.append(values)
    for keys in players_score.keys():
        K.append(keys)
    SL = sorted(L)
    SLT = sorted(list(set(SL)))
    I = {}
    j = 1

    for x in SLT:
        b = 0
        for y in L:
            if x == y:
                I[j] = K[b]
                j += 1
                b += 1
                continue
            else:
                b += 1
                continue

    for value in I.values():
        top_players[value] = 0

    a = 0
    for key in top_players.keys():
        top_players[key] = SL[a]
        a += 1

    for players, score in top_players.items():
        if i == 1:
            medal = 'MEDAL OF GOLD'
        elif i == 2:
            medal = 'MEDAL OF SILVER'
        elif i == 3:
            medal = 'MEDAL OF BRONZE'
        else:
            medal = 'Not good enough for a medal'
        print(f'{i}. {players} **\033[1m{score}\033[0m** --> {medal}')
        i += 1

# END OF THE RANKING FUNCTION the names are not well sorted






if __name__ == '__main__':
    start_game()







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
    print(SL)
    print(SLT)
players_score = {'alfa': 3, 'beta': 4, 'gamma': 9, 'omega': 9,'pedro': 2}

ranking(players_score)


# it only works with even players


import choix
import numpy as np
from fetchPlayers import getWeekOneStarters

def rank(comparisons, players):
    # ratings, ranked = elo_rank(players, comparisons)
    elo_rank(players, comparisons)
    
    count = 1
    # for item in ranked:
    #     print(f'{count}: {players.iloc[item[0]].name} - {item[1]}')
    #     count += 1

    players.sort(key=lambda p: p.elo, reverse=True)

    for p in players:
        print(f'{count}: {p.name}')
        count += 1

    return players



def elo_rank(players, comparisons, K=50):
    for winner, loser in comparisons:
        players[winner].elo, players[loser].elo = elo_update(players[winner].elo, players[loser].elo, K)

    # ranked = sorted(enumerate(ratings), key=lambda x: x[1], reverse=True)
    # return ratings, ranked

def elo_update(rating_winner, rating_loser, K=50):
    expected_win = 1 / (1 + 10 ** ((rating_loser - rating_winner) / 400))
    new_rating_winner = rating_winner + K * (1 - expected_win)
    new_rating_loser = rating_loser + K * (0 - (1 - expected_win))
    return new_rating_winner, new_rating_loser

comparisons = [
    (1, 0), (3, 2), (5, 4), (6, 7), (9, 8), (10, 11), (12, 13), (14, 15), (17, 16), (19, 18), (21, 20), (23, 22),
    (24, 25), (27, 26), (29, 28), (30, 31), (2, 22), (22, 26), (6, 17), (5, 26), (10, 9), (12, 28), (11, 5), (19, 5),
    (6, 31), (10, 21), (9, 23), (12, 0), (19, 1), (31, 26), (14, 26), (25, 16), (27, 13), (1, 16),
    (16, 28), (19, 25), (6, 18), (6, 4), (24, 23), (19, 20), (16, 7), (1, 17), (12, 19), (3, 11), (13, 5),
    (5, 2), (17, 2), (6, 11), (24, 26), (27, 30), (23, 17), (10, 28), (15, 4), (7, 8), (21, 22), (18, 28), 
    (1, 23), (31, 7), (16, 15), (13, 2), (10, 24), (24, 7), (6, 5), (30, 8), (30, 28), (12, 29), (3, 28), (6, 24), 
    (28, 15), (9, 5), (27, 6), (20, 31), (7, 0), (0, 4), (1, 7), (20, 25), (25, 7), (1, 5), (21, 31), (14, 22), (13, 7), 
    (17, 26), (21, 4), (25, 4), (18, 25), (24, 5), (1, 13), (29, 25), (11, 8), (9, 11), (21, 27), (0, 26), (21, 2), 
    (14, 28), (11, 4), (19, 26)
    ]
players = getWeekOneStarters([2024],['QB'])
rank(comparisons, players)

# print("Ratings:", ratings)
# print()
# print("Ranked order:", ranked)


# --------------------------- Example usage -------------------------------
# First number beats second number

# comparisons = [    
#     (0, 1), (0, 1), (0, 1),  
#     (1, 2), (1, 2),          
#     (0, 2),                  
#     (2, 0),                  
#     (3, 0), (3, 2), (1, 3)
# ]

# strengths, ranking = rank(comparisons)

# print("Normalized strengths:", strengths)
# print("Ranking (best to worst):", ranking)
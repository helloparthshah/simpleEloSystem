import random
from player import Player
from match_handler import MatchHandler
import csv
""" players = [Player("a"), Player("b"), Player("c"), Player("d"), Player(
    "e"), Player("f"), Player("g"), Player("h"), Player("i"), Player("j")]


for i in range(100):
    random.shuffle(players)
    team1 = players[:5]
    team2 = players[5:]
    score1 = [random.randint(0, 20) for i in range(5)]
    score2 = [random.randint(0, 20) for i in range(5)]
    winner = random.randint(0, 1)
    match = MatchHandler(team1, team2, score1, score2, winner)
    match.play_team()

players = sorted(players, key=lambda x: x.elo, reverse=True)

for i in range(10):
    print(players[i]) """

players = {}
with open('games.csv', newline='', encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        if(row[5] not in players):
            players[row[5]] = Player(row[5])
            """ if row[9] != '':
                players[row[6]].elo = int(row[9]) """
        if(row[6] not in players):
            players[row[6]] = Player(row[6])
            """ if row[11] != '':
                players[row[7]].elo = int(row[11]) """

match_handler = MatchHandler([], [], [], [], 0)

with open('games.csv', newline='', encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        winner = -1
        mov = 1
        if(row[7] == row[5]):
            winner = 0
        elif(row[7] == row[6]):
            winner = 1
        else:
            print("error")
        match_handler = MatchHandler([players[row[5]]], [players[row[6]]],
                                     [int(row[8])], [int(row[9])], winner)
        match_handler.play_team()

players = sorted(players.values(), key=lambda x: x.elo, reverse=True)

# print first 10 players
for i in range(10):
    print(players[i])

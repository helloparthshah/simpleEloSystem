from player import Player
from match_handler import MatchHandler
import csv

players = {}
with open('chess_games.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in csvreader:
        if line_count == 0:
            line_count += 1
        else:
            if(row[6] not in players):
                players[row[8]] = Player(row[8])
                if row[9] != '':
                    players[row[8]].elo = int(row[9])
            if(row[10] not in players):
                players[row[10]] = Player(row[10])
                if row[11] != '':
                    players[row[10]].elo = int(row[11])
        line_count += 1
test = sorted(players.values(), key=lambda x: x.elo, reverse=True)

for i in range(10):
    print(test[i])

print("------------------")

match_handler = MatchHandler([], [], [], [], 0)

with open('chess_games.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in csvreader:
        if line_count == 0:
            line_count += 1
        else:
            winner = -1
            mov = 1
            if(row[6] == "white"):
                winner = 0
            elif(row[8] == "black"):
                winner = 1
            else:
                winner = row[9] < row[11]
                mov = 0.5
            if(winner != -1):
                a, b = match_handler.play(
                    players[row[8]].elo, players[row[10]].elo, winner, mov, winner)
                players[row[8]].elo = a
                players[row[10]].elo = b
        line_count += 1

players = sorted(players.values(), key=lambda x: x.elo, reverse=True)

# print first 10 players
for i in range(10):
    print(players[i])

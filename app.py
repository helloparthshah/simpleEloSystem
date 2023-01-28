from player import Player
from match_handler import MatchHandler
import csv

players = {}
with open('Carlsen_game_info.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in csvreader:
        if line_count == 0:
            line_count += 1
        else:
            if(row[6] not in players):
                players[row[6]] = Player(row[6])
                if row[9] != '':
                    players[row[6]].elo = int(row[9])
            if(row[7] not in players):
                players[row[7]] = Player(row[7])
                if row[11] != '':
                    players[row[7]].elo = int(row[11])
        line_count += 1

match_handler = MatchHandler([], [], [], [], 0)

with open('Carlsen_game_info.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in csvreader:
        if line_count == 0:
            line_count += 1
        else:
            winner = -1
            mov = 1
            if(row[8] == "1-0"):
                winner = 0
            elif(row[8] == "0-1"):
                winner = 1
            else:
                winner = row[9] < row[11]
                mov = 0.5
            if(winner != -1):
                a, b = match_handler.play(
                    players[row[6]].elo, players[row[7]].elo, winner, mov)
                players[row[6]].elo = a
                players[row[7]].elo = b
        line_count += 1

players = sorted(players.values(), key=lambda x: x.elo, reverse=True)

# print first 10 players
for i in range(10):
    print(players[i])

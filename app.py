import random
from player import Player
from match_handler import MatchHandler

players = [Player("a"), Player("b"), Player("c"), Player("d"), Player(
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

print(sorted(players, key=lambda x: x.elo, reverse=True))

import math


class MatchHandler:
    def __init__(self, team_a, team_b, score_a, score_b, winner):
        self.team_a = team_a
        self.team_b = team_b
        self.score_a = score_a
        self.score_b = score_b
        self.winner = winner

    def Probability(self, rating1, rating2):
        return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating2 - rating1) / 400))

    def play(self, a, b, winner, mov=1, pNumber=0):
        Pa = self.Probability(a, b)
        Pb = self.Probability(b, a)

        factor = math.log(abs(mov)+1)*1.5
        if (mov > 0 and pNumber != winner) or (mov < 0 and pNumber == winner):
            factor = 1/factor
        elif (mov < 0 and pNumber != winner) or (mov > 0 and pNumber == winner):
            factor = factor
        if mov == 1:
            factor = 1
        new_a = a + 32 * (1-winner - Pa)*factor
        new_b = b + 32 * (winner - Pb)*factor
        # elo can't be less than 0
        if new_a < 0:
            new_a = 0
        if new_b < 0:
            new_b = 0
        return new_a, new_b

    def play_team(self):
        point_diff = (sum(self.score_a)+sum(self.score_b)) / \
            (len(self.score_a)+len(self.score_b))
        a_total = 0
        for i in range(len(self.team_a)):
            a_total += self.team_a[i].elo
        avg_a = a_total/len(self.team_a)
        b_total = 0
        for i in range(len(self.team_b)):
            b_total += self.team_b[i].elo
        avg_b = b_total/len(self.team_b)
        for i in range(len(self.team_a)):
            self.team_a[i].elo = self.play(self.team_a[i].elo, avg_b, self.winner,
                                           self.score_a[i]-point_diff+1-self.winner, 0)[0]
            self.team_b[i].elo = self.play(avg_a, self.team_b[i].elo, self.winner,
                                           self.score_b[i]-point_diff+1-self.winner, 1)[1]

class Player:
    def __init__(self, name, elo=100):
        self.name = name
        self.elo = elo

    def __str__(self):
        return self.name + " " + str(self.elo)

    def __repr__(self):
        return str(self)

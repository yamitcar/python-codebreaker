class Game:

    POINTS = [0,15,30,40]
    WINJ1 = 'WINJ1'
    WINJ2 = 'WINJ2'

    def __init__(self):
        self.players = {'J1': 0, 'J2': 0}
        self.deuce_conditions = {1: 'ADVJ1', -1: 'ADVJ2', 0: 'DEUCE', -2: self.WINJ2, 2: self.WINJ1}
    
    def pointTo(self,player):
        self.players[player] += 1

    @property
    def score(self):
        if self.is_deuce():
            return self.deuce_conditions[self.players['J1'] - self.players['J2']]

        if self.has_won('J2'):
            return self.WINJ2
        
        if self.has_won('J1'):
            return self.WINJ1

        points_j1 = self.POINTS[self.players['J1']]
        points_j2 = self.POINTS[self.players['J2']]

        return f'{points_j1}-{points_j2}'

    def is_deuce(self):
        return self.players['J1'] >= len(self.POINTS)-1 and self.players['J2'] >= len(self.POINTS)-1

    def has_won(self, player):
        return self.players[player] == len(self.POINTS)
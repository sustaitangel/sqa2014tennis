# -*- coding: utf-8 -*-
class Match:

    def __init__(self, j1, j2, sets):
        self.p1 = j1
        self.p2 = j2
        self.sets = sets
        self.p1_wins = 0
        self.p2_wins = 0
        self.p1_sets = ['', '', '', '', '']
        self.p2_sets = ['', '', '', '', '']
        self.result= (self.p1_wins)-(self.p2_wins)
        self.result1= (self.p2_wins)-(self.p2_wins)

    def score(self):
        if self.p1_wins == 0 and self.p2_wins == 0:
            return "{0} j1 and j2 {1} | 0-0".format(self.p1, self.p2)

        if self.sets == 3:

            if (result==2):
                return "{0} defeated {1} | {2}, {3}".format(self.p1, self.p2, self.p1_sets[0], self.p1_sets[1])
            if (result== 1):
                return "{0} defeated {1} | {2}, {3}, {4}".format(self.p1, self.p2, self.p1_sets[0], self.p1_sets[1], self.p1_sets[2])
            if (result1== 2):
                return "{0} defeated {1} | {2}, {3}".format(self.p2, self.p1, self.p2_sets[0], self.p2_sets[1])
            if (result1 == 1):
                return "{0} defeated {1} | {2}, {3}, {4}".format(self.p2, self.p1, self.p2_sets[0], self.p2_sets[1], self.p2_sets[2])

        elif self.sets == 5:
            if (result == 3):
                return "{0} defeated {1} | {2}, {3}, {4}".format(self.p1, self.p2, self.p1_sets[0], self.p1_sets[1], self.p1_sets[2])
            if (result == 2):
                return "{0} defeated {1} | {2}, {3}, {4}, {5}".format(self.p1, self.p2, self.p1_sets[0], self.p1_sets[1], self.p1_sets[2], self.p1_sets[3])
            if (result == 1):
                return "{0} defeated {1} | {2}, {3}, {4}, {5}, {6}".format(self.p1, self.p2, self.p1_sets[0], self.p1_sets[1], self.p1_sets[2], self.p1_sets[3], self.p1_sets[4])

            if (result1 == 3):
                return "{0} defeated {1} | {2}, {3}, {4}".format(self.p2, self.p1, self.p2_sets[0], self.p2_sets[1], self.p2_sets[2])
            if (result1 == 2):
                return "{0} defeated {1} | {2}, {3}, {4}, {5}".format(self.p2, self.p1, self.p2_sets[0], self.p2_sets[1], self.p2_sets[2], self.p2_sets[3])
            if (result1 == 1):
                return "{0} defeated {1} | {2}, {3}, {4}, {5}, {6}".format(self.p2, self.p1, self.p2_sets[0], self.p2_sets[1], self.p2_sets[2], self.p2_sets[3], self.p2_sets[4])

    def winer(self, jugador, set_num, points1, points2):
        if self.p1 == jugador:
            self.p1_wins = self.p1_wins + 1
            self.p1_sets[set_num - 1] = points1 + '-' + points2
            self.p2_sets[set_num - 1] = points2 + '-' + points1

        else:
            self.p2_wins = self.p2_wins + 1
            self.p2_sets[set_num - 1] = points1 + '-' + points2
            self.p1_sets[set_num - 1] = points2 + '-' + points1

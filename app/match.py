# -*- coding: utf-8 -*-
class Match:

    def __init__(self, p1, p2, pacted_sets):
        self.p1 = p1
        self.p2 = p2
        self.pacted_sets = pacted_sets
        self.count_p1 = 0
        self.count_p2 = 0
        self.score_p1 = ['', '', '', '', '']
        self.score_p2 = ['', '', '', '', '']
        self.points = ""

    def show_score(self):
        if self.count_p1 == 0 and self.count_p2 == 0:
            return "{0} plays with {1} | 0-0".format(self.p1, self.p2)
        elif self.count_p1 > self.count_p2:
            return "{0} defeated {1} | {2}".format(self.p1, self.p2, self.get_points(self.p1))
        else:
            return "{0} defeated {1} | {2}".format(self.p2, self.p1, self.get_points(self.p2))

    def add_points(self, player, set_num, num1, num2):
        if player == self.p1:
            self.count_p1 += 1
            self.score_p1[set_num - 1] = num1
            self.score_p2[set_num - 1] = num2
        else:
            self.count_p2 += 1
            self.score_p1[set_num - 1] = num2
            self.score_p2[set_num - 1] = num1

    def get_points(self, player):

        points = ""
        total = self.count_p1 + self.count_p2
        i = 0

        while i < total:
            if player == self.p1:
                points += str(self.score_p1[i]) + \
                    "-" + str(self.score_p2[i]) + ", "
            else:
                points += str(self.score_p2[i]) + \
                    "-" + str(self.score_p1[i]) + ", "
            i += 1
        return points[:-2]

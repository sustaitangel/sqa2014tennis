# -*- coding: utf-8 -*-
class Match:
    def __init__(self,player1,player2,pacted_sets):
        self.p1 = player1
        self.p2 = player2
        self.pacted_sets = pacted_sets
        self.p1_wins = 0
        self.p2_wins = 0
        self.p1_sets = ['', '', '', '', '']
        self.p2_sets = ['', '', '', '', '']

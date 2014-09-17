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
        lista=[self.p1_wins,self.p2_wins]
        lista1=[]
        lisreturn=[lista,lista1]
        if self.p1_wins == 0 and self.p2_wins == 0:
            return lista

        if self.sets == 3:

            if (result==2):
                lista1=[self.p1_sets[0], self.p1_sets[1]]
                return lisreturn
            if (result== 1):
                lista1=[self.p1_sets[0], self.p1_sets[1], self.p1_sets[2]]
                return lisreturn
            if (result1== 2):
                lista1=[self.p2_sets[0], self.p2_sets[1]]
                return lisreturn
            if (result1 == 1):
                lista1=[self.p2_sets[0], self.p2_sets[1], self.p2_sets[2]]
                return lisreturn

        elif self.sets == 5:
            if (result == 3):
                lista1=[self.p1_sets[0], self.p1_sets[1], self.p1_sets[2]]
                return lisreturn
            if (result == 2):
                lista1=[self.p1_sets[0], self.p1_sets[1], self.p1_sets[2], self.p1_sets[3]]
                return lisreturn
            if (result == 1):
                lista1=[self.p1_sets[0], self.p1_sets[1], self.p1_sets[2], self.p1_sets[3], self.p1_sets[4]]
                return lisreturn 
            if (result1 == 3):
                lista1=[self.p2_sets[0], self.p2_sets[1], self.p2_sets[2]]
                return lisreturn
            if (result1 == 2):
                lista1=[self.p2_sets[0], self.p2_sets[1], self.p2_sets[2], self.p2_sets[3]]
                return lisreturn
            if (result1 == 1):
                lista1=[self.p2_sets[0], self.p2_sets[1], self.p2_sets[2], self.p2_sets[3], self.p2_sets[4]]
                return lisreturn

    def winer(self, jugador, set_num, points1, points2):
        ganador=1
        if self.p1 == jugador:
            self.p1_wins = self.p1_wins + ganador
            self.p1_sets[set_num - 1] = points1 + '-' + points2
            self.p2_sets[set_num - 1] = points2 + '-' + points1

        else:
            self.p2_wins = self.p2_wins + ganador
            self.p2_sets[set_num - 1] = points1 + '-' + points2
            self.p1_sets[set_num - 1] = points2 + '-' + points1

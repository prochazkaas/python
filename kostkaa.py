#!/usr/bin/env python3
#Prochazka

import random

class Kostka :

    def __init__(self, pocet_sten=6):
        try:
            self.setPocetSten(pocet_sten)
        except:
            print("Chyba v poctu sten, nastavuji 6 .")
        self.__pocetSten = 6
    
    def hod(self):
        return random.randint(1, self.__pocetSten)
    def getPocetSten(self) :
        return self.__pocetSten
    
    def setPocetSten(self, pocet_sten):
        if pocet_sten > 0:
            self.__pocetSten = pocet_sten
        else:
            print(f'pocet_sten musi byt > 0, ponechavam: {self.__pocetSten}.')



k1 = Kostka (6)
print (k1.hod())

k2 = Kostka (12)
print(k2.hod())


# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 21:52:09 2024

@author: bebo
"""

# coding: utf-8
class Voiture:
    roues = 4
    moteur = 1
    def __init__(self):
        self.nom = "A déterminer"
    def allumer(self):
        print ("La voiture démarre")
        print(self.nom)
        print(self.roues)

class VoitureSport(Voiture):
    def __init__(self):
        self.nom = "Ferrari"
    def allumer(self):
        print ("La voiture de sport démarre")
        print(self.nom)
        print(self.roues)
        
ma_voiture_sport = VoitureSport()
ma_voiture_sport.allumer()
ma_voiture = Voiture()
ma_voiture.allumer()




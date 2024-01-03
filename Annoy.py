# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 15:49:30 2024

@author: sebay
"""

import tkinter as tk
import time

class Forme:
    def __init__(self, x, y, w, h, couleur, canva):
        #Réglage des dimensions, couleur et positions centrales de la forme
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.couleur = couleur
        
        #Création de la forme
        canva.create_rectangle(self.x - self.w / 2, self.y - self.h / 2, self.x + self.w / 2, self.y + self.h / 2, width = 2, fill = couleur)
        
    #Getters pour les données nécessaires de la forme
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_width(self):
        return self.w
    
    def get_height(self):
        return self.h

class Jeu:
    def __init__(self):
        #Variable servant à savoir si le jeu est lancé ou non
        self.launched = False

        #Réglage des dimensions du canva
        self.wwin = 400
        self.hwin = 200
        #Création de la fenêtre
        self.window = tk.Tk()

        #Création du canva dans la fenêtre avec les dimensions définies
        self.canvas = tk.Canvas(self.window, width = self.wwin, height = self.hwin, background = "white")
        #Réglage de l'emplacement et de l'affichage du canva dans la fenêtre
        self.canvas.pack(fill = "both", expand = True)
        
        #initialisation des boutons
        self.init_boutons()

        #Réglage des dimensions des barres, de leur position sur l'axe y et de leur couleur
        wpole = 10
        hpole = 75
        ypole = 100
        cpole = "grey"

        #Création des barres pour le jeu, avec les dimensions établies
        self.pole0 = Forme(125, ypole, wpole, hpole, cpole, self.canvas)
        self.pole1 = Forme(225, ypole, wpole, hpole, cpole, self.canvas)
        self.pole2 = Forme(325, ypole, wpole, hpole, cpole, self.canvas)

    def init_boutons(self):
        #Création d'une frame pour accueillir les boutons dans la fenêtre
        btnFrame = tk.Frame()
        #Réglage de l'emplacement de la fenêtre
        btnFrame.pack(side = 'bottom', fill = 'x')

        #Création de 3 colonnes et 2 lignes pour accueillir les boutons pour lancer le jeu et le quitter
        btnFrame.columnconfigure(0, weight=1)
        btnFrame.columnconfigure(1, weight=1)
        btnFrame.columnconfigure(2, weight=1)
        btnFrame.rowconfigure(0, weight=1)
        btnFrame.rowconfigure(1, weight=1)
        
        #Création de 3 bouton, chacun lançant le jeu depuis une barre différente
        btn1 = tk.Button(btnFrame,text = "1", width = 5, command = self.lancement_1)
        btn2 = tk.Button(btnFrame,text = "2", width = 5, command = self.lancement_2)
        btn3 = tk.Button(btnFrame,text = "3", width = 5, command = self.lancement_3)

        #Placement des boutons sur la frame selon la grille établie plus tôt
        btn1.grid(row=0, column=0, pady = 3, padx = 50, sticky='W')
        btn2.grid(row=0, column=1, pady = 3, padx = 3)
        btn3.grid(row=0, column=2, pady = 3, padx = 50, sticky='E')

        #Création et placement du bouton quitter
        bouton_quitter = tk.Button(btnFrame,text = "Quitter", width = 20, command=self.window.destroy)
        bouton_quitter.grid(row=1, column=1, pady = 3)
    
    def lancement_1(self):
        return
    
    def lancement_2(self):
        return
    
    def lancement_3(self):
        return
    
    def boucle(self):
        self.window.mainloop()
        

if __name__ == '__main__':
    Jeu().boucle()
    
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 15:49:30 2024

@author: sebay
"""

import tkinter as tk
import time

class Forme:
    def __init__(self, id, x, y, w, h, couleur, canvas):
        #Réglage des dimensions, couleur et positions centrales de la forme
        self.id = id
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.couleur = couleur

        #Création de la forme
        self.forme = canvas.create_rectangle(self.x - self.w / 2, self.y - self.h / 2, self.x + self.w / 2, self.y + self.h / 2, width = 2, fill = couleur)

class Barre(Forme):
    def __init__(self, id, x, y, w, h, couleur, canvas):
        Forme.__init__(self, id, x, y, w, h, couleur, canvas)
        self.disques = []
        self.count = 0

    def ajouter_disque(self, disque):
        self.disques.append(disque)
        self.count += 1
        print('Le disque numéro ' + disque.id + ' se place sur la barre ' + self.id)

    def retirer_disque(self, disque):
        self.disques.remove(disque)
        self.count -= 1
        print('Le disque numéro ' + disque.id + ' se retire de la barre ' + self.id)

class Disque(Forme):
    def set_coords(self, x, y, pole, canvas, is_moving = False):
        #Modification des coordonnées
        self.x = x
        self.y = y
        self.pole = pole
        self.is_moving = is_moving

        #Modification des coordonnées dans le canvas
        canvas.coords(self.forme, self.x - self.w / 2, self.y - self.h / 2, self.x + self.w / 2, self.y + self.h / 2)

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
        self.pole0 = Barre('1', 100, ypole, wpole, hpole, cpole, self.canvas)
        self.pole1 = Barre('2', 200, ypole, wpole, hpole, cpole, self.canvas)
        self.pole2 = Barre('3', 300, ypole, wpole, hpole, cpole, self.canvas)

        #Réglage de la couleur et de la hauteur des disques
        hdisk = 10
        cdisk = "red"

        #Création des disques
        self.disk0 = Disque('1', self.pole1.x, self.pole1.y + 5, self.pole1.w + 10, hdisk, cdisk, self.canvas)
        self.disk1 = Disque('2', self.pole1.x, self.pole1.y + 15, self.pole1.w + 20, hdisk, cdisk, self.canvas)
        self.disk2 = Disque('3', self.pole1.x, self.pole1.y + 25, self.pole1.w + 30, hdisk, cdisk, self.canvas)
        self.disk3 = Disque('4', self.pole1.x, self.pole1.y + 35, self.pole1.w + 40, hdisk, cdisk, self.canvas)
        
        self.pole1.ajouter_disque(self.disk0)
        self.pole1.ajouter_disque(self.disk1)
        self.pole1.ajouter_disque(self.disk2)
        self.pole1.ajouter_disque(self.disk3)

    def init_boutons(self):
        #Création d'une frame pour accueillir les boutons dans la fenêtre
        btnFrame = tk.Frame()
        #Réglage de l'emplacement de la fenêtre
        btnFrame.pack(side = 'bottom', fill = 'x')

        #Création de 3 colonnes et 2 lignes pour accueillir les boutons pour lancer le jeu et le quitter
        btnFrame.columnconfigure(0, weight = 1)
        btnFrame.columnconfigure(1, weight = 1)
        btnFrame.columnconfigure(2, weight = 1)
        btnFrame.rowconfigure(0, weight = 1)
        btnFrame.rowconfigure(1, weight = 1)

        #Création de 3 bouton, chacun lançant le jeu depuis une barre différente
        btn1 = tk.Button(btnFrame,text = "1", width = 5, command = self.lancement_1)
        btn2 = tk.Button(btnFrame,text = "2", width = 5, command = self.lancement_2)
        btn3 = tk.Button(btnFrame,text = "3", width = 5, command = self.lancement_3)

        #Placement des boutons sur la frame selon la grille établie plus tôt
        btn1.grid(row=0, column=0, pady = 3, padx = 3)
        btn2.grid(row=0, column=1, pady = 3, padx = 3)
        btn3.grid(row=0, column=2, pady = 3, padx = 3)

        #Création et placement du bouton quitter
        bouton_quitter = tk.Button(btnFrame, text = "Quitter", width = 20, command = self.window.destroy)
        bouton_quitter.grid(row = 1, colum = 1, pady = 3)

    def choix_mouvement(self):
        return
    
    def mouvement(self):
        return

    def test_fin(self):
        if (self.pole0.count == 4 or self.pole1.count == 4 or self.pole2.count == 4):
            self.launched = False

    def boucle(self):
        self.launched = True

        while (self.launched):
            self.choix_mouvement()
            self.mouvement()
            self.test_fin()

    def lancement_1(self):
        if (self.launched):
            return
        
        if (self.pole1.count > 0):
            self.pole1.retirer_disque(self.disk0)
            self.pole1.retirer_disque(self.disk1)
            self.pole1.retirer_disque(self.disk2)
            self.pole1.retirer_disque(self.disk3)

        if (self.pole2.count > 0):
            self.pole2.retirer_disque(self.disk0)
            self.pole2.retirer_disque(self.disk1)
            self.pole2.retirer_disque(self.disk2)
            self.pole2.retirer_disque(self.disk3)

        if (self.pole0.count == 0):
            self.disk0.set_coords(self.pole0.x, self.disk0.y, self.pole0, self.canvas)
            self.disk1.set_coords(self.pole0.x, self.disk1.y, self.pole0, self.canvas)
            self.disk2.set_coords(self.pole0.x, self.disk2.y, self.pole0, self.canvas)
            self.disk3.set_coords(self.pole0.x, self.disk3.y, self.pole0, self.canvas)
        
            self.pole0.ajouter_disque(self.disk0)
            self.pole0.ajouter_disque(self.disk1)
            self.pole0.ajouter_disque(self.disk2)
            self.pole0.ajouter_disque(self.disk3)

        print('Lancement du jeu depuis la barre 1')

        self.boucle()

    def lancement_2(self):
        if (self.launched):
            return

        if (self.pole0.count > 0):
            self.pole0.retirer_disque(self.disk0)
            self.pole0.retirer_disque(self.disk1)
            self.pole0.retirer_disque(self.disk2)
            self.pole0.retirer_disque(self.disk3)

        if (self.pole2.count > 0):
            self.pole2.retirer_disque(self.disk0)
            self.pole2.retirer_disque(self.disk1)
            self.pole2.retirer_disque(self.disk2)
            self.pole2.retirer_disque(self.disk3)

        if (self.pole1.count == 0):
            self.disk0.set_coords(self.pole1.x, self.disk0.y, self.pole1, self.canvas)
            self.disk1.set_coords(self.pole1.x, self.disk1.y, self.pole1, self.canvas)
            self.disk2.set_coords(self.pole1.x, self.disk2.y, self.pole1, self.canvas)
            self.disk3.set_coords(self.pole1.x, self.disk3.y, self.pole1, self.canvas)
        
            self.pole1.ajouter_disque(self.disk0)
            self.pole1.ajouter_disque(self.disk1)
            self.pole1.ajouter_disque(self.disk2)
            self.pole1.ajouter_disque(self.disk3)

        print('Lancement du jeu depuis la barre 2')

        self.boucle()

    def lancement_3(self):
        if (self.launched):
            return

        if (self.pole0.count > 0):
            self.pole0.retirer_disque(self.disk0)
            self.pole0.retirer_disque(self.disk1)
            self.pole0.retirer_disque(self.disk2)
            self.pole0.retirer_disque(self.disk3)

        if (self.pole1.count > 0):
            self.pole1.retirer_disque(self.disk0)
            self.pole1.retirer_disque(self.disk1)
            self.pole1.retirer_disque(self.disk2)
            self.pole1.retirer_disque(self.disk3)

        if (self.pole2.count == 0):
            self.disk0.set_coords(self.pole2.x, self.disk0.y, self.pole2, self.canvas)
            self.disk1.set_coords(self.pole2.x, self.disk1.y, self.pole2, self.canvas)
            self.disk2.set_coords(self.pole2.x, self.disk2.y, self.pole2, self.canvas)
            self.disk3.set_coords(self.pole2.x, self.disk3.y, self.pole2, self.canvas)

            self.pole2.ajouter_disque(self.disk0)
            self.pole2.ajouter_disque(self.disk1)
            self.pole2.ajouter_disque(self.disk2)
            self.pole2.ajouter_disque(self.disk3)

        print('Lancement du jeu depuis la barre 3')

        self.boucle()

    
    def lancer(self):
        self.window.mainloop()
        
#Si le script est lancé directement, on lance le jeu avec la fonction lancer()
if __name__ == '__main__':
    Jeu().lancer()
    
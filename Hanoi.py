# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 15:49:30 2024

@author: Sébastien LAMARD
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
        #Initialisation de la forme
        Forme.__init__(self, id, x, y, w, h, couleur, canvas)
        #Initialisation du nombre de disques sur la barre
        self.count = 0

    def ajouter_disque(self, disque):
        #Ajout d'un disque au compte de la barre et notification du mouvement du disque
        self.count += 1
        print('Le disque numéro ' + disque.id + ' se place sur la barre ' + self.id)

    def retirer_disque(self, disque):
        #Retrait d'un disque au compte de la barre et notification du mouvement du disque
        self.count -= 1
        print('Le disque numéro ' + disque.id + ' se retire de la barre ' + self.id)

class Disque(Forme):
    def set_coords(self, x, y, pole, canvas):
        #Modification des coordonnées
        self.x = x
        self.y = y
        self.pole = pole

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
        self.poles = [
            Barre('1', 100, ypole, wpole, hpole, cpole, self.canvas), 
            Barre('2', 200, ypole, wpole, hpole, cpole, self.canvas),
            Barre('3', 300, ypole, wpole, hpole, cpole, self.canvas),
        ]

        #Réglage de la couleur, de l'emplacement vertical et des dimensions de base des disques
        hdisk = 10
        wdisk = self.poles[1].w + 80
        ydisk = self.poles[1].y + 35
        cdisk = "red"
        
        #Le nombre de disque peut être modifié de 0 à 8
        self.nb_disks = int(input('Choisissez le nombre de disques. Merci de donner un nombre entre 2 et 8: '))

        if (self.nb_disks < 2 or self.nb_disks > 8):
            print('Veuillez choisir un nombre compris entre 2 et 8.')
            return

        #Création des disques
        self.disks = []
        for i in range(self.nb_disks):
            self.disks.insert(0, Disque(str(self.nb_disks), self.poles[1].x, ydisk, wdisk, hdisk, cdisk, self.canvas))
            ydisk -= 10
            wdisk -= 10


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
        bouton_quitter.grid(row = 1, column = 1, pady = 3)

    def choix_mouvement(self):
        #Si le tour est impair, on bouge la petite pièce
        if self.tour % 2 != 0:
            #On retire la pièce de sa barre
            self.poles[self.disks[0].pole].retirer_disque(self.disks[0])
            #Si le nombre de pièces est pair, la petite pièce bouge selon ce patterne sur les barres : 0 -> 1 -> 2 -> 0
            if self.nb_disks % 2 == 0:
                if self.disks[0].pole == 0:
                    self.disks[0].pole = 1
                elif self.disks[0].pole == 1:
                    self.disks[0].pole = 2
                else:
                    self.disks[0].pole = 0
            #Si le nombre de pièces est impair, la petite pièce bouge selon ce patterne sur les barres : 0 -> 2 -> 1 -> 0
            else:
                if self.disks[0].pole == 0:
                    self.disks[0].pole = 2
                elif self.disks[0].pole == 1:
                    self.disks[0].pole = 0
                else:
                    self.disks[0].pole = 1
            #Une fois la dstination choisie, on fait bouger la pièce et on sort de la méthode
            self.mouvement(0)
            return
        #Si le tour est pair, on bouge la deuxième plus petite pièce qui se trouve en haut d'un tas. On commence donc au second index
        for i in range(1, self.nb_disks, 1):
            #On ignore les pièces se situant en dessous de la petite pièce
            if self.disks[i].pole == self.disks[0].pole:
                continue
            #Les pièces étant classées de la plus petite à la plus grande, on tombe directement sur la deuxième pièce la plus petite qui soit utilisable.
            #On la retire de sa barre
            self.poles[self.disks[i].pole].retirer_disque(self.disks[i])
            #On recherche la barre sur laquelle la pièce doit aller : Il s'agit de celle où ni la petite pièce, ni elle-même ne se trouve
            if self.disks[0].pole == 0:
                if self.disks[i].pole == 1:
                    self.disks[i].pole = 2
                else:
                    self.disks[i].pole = 1
            elif self.disks[0].pole == 1:
                if self.disks[i].pole == 0:
                    self.disks[i].pole = 2
                else:
                    self.disks[i].pole = 0
            else:
                if self.disks[i].pole == 1:
                    self.disks[i].pole = 0
                else:
                    self.disks[i].pole = 1
            #Une fois la destination choisie, on lance le mouvement, puis on sort de la fonction afin d'ignorer les prochaines pièces
            self.mouvement(i)
            return

    def mouvement(self, disk_index):
        #y est égale à la plus grande valeur possible afin de placer la pièce le plus bas possible sur la barre
        y = 135
        #Pour chaque disque déjà placé sur la barre, on retire la taille d'une pièce à y
        for i in range(self.poles[self.disks[disk_index].pole].count):
            y -= self.disks[disk_index].h5
        
        #On remplace les coordonnées du disque dans l'objet et sur le canvas, puis on l'ajoute au compte de la barre
        self.disks[disk_index].set_coords(self.poles[self.disks[disk_index].pole].x, y, self.disks[disk_index].pole, self.canvas)
        self.poles[self.disks[disk_index].pole].ajouter_disque(self.disks[disk_index])

    def test_fin(self):
        #Si l'une des barres comprend la totalité des pièces, la partie est finie
        if self.poles[0].count == self.nb_disks or self.poles[1].count == self.nb_disks or self.poles[2].count == self.nb_disks:
            self.launched = False

    def boucle(self):
        #On lance la partie et on initialise le nombre de tours à 0
        self.launched = True
        self.tour = 0

        #A chaque tour, on ajoute 1 au nombre de tours, on rafraîchit la fenêtre, on attend une demi-seconde
        #On réalise ensuite un nouveau mouvement et on teste les conditions de fin
        while (self.launched):
            self.tour += 1
            self.window.update()
            time.sleep(0.5)
            self.choix_mouvement()
            self.test_fin()

    def lancement_1(self):
        #Si le jeu est lancé, on ignore le clic sur le bouton
        if self.launched:
            return

        #On retire les disques des autres barres (index 1 et 2)
        for i in range(1, 3, 1):
            if self.poles[i].count > 0:
                for j in range(self.nb_disks):
                    self.poles[i].retirer_disque(self.disks[j])

        #On place les disques sur la barre 1 (index 0)
        if self.poles[0].count == 0:
            for i in range(self.nb_disks):
                self.disks[i].set_coords(self.poles[0].x, self.disks[i].y, 0, self.canvas)
                self.poles[0].ajouter_disque(self.disks[i])

        #On notifie le lancement du jeu
        print('Lancement du jeu depuis la barre 1')

        #On lance la boucle principale
        self.boucle()

    def lancement_2(self):
        #Si le jeu est lancé, on ignore le clic sur le bouton
        if self.launched:
            return

        #On retire les disques des autres barres (index 0 et 2)
        for i in range(0, 3, 1):
            if i != 1 and self.poles[i].count > 0:
                for j in range(self.nb_disks):
                    self.poles[i].retirer_disque(self.disks[j])

        #On place les disques sur la barre 2 (index 1)
        if self.poles[1].count == 0:
            for i in range(self.nb_disks):
                self.disks[i].set_coords(self.poles[1].x, self.disks[i].y, 1, self.canvas)
                self.poles[1].ajouter_disque(self.disks[i])

        #On notifie le lancement du jeu
        print('Lancement du jeu depuis la barre 2')

        #On lance la boucle principale
        self.boucle()

    def lancement_3(self):
        #Si le jeu est lancé, on ignore le clic sur le bouton
        if self.launched:
            return

        #On retire les disques des autres barres (index 0 et 1)
        for i in range(0, 2, 1):
            if self.poles[i].count > 0:
                for j in range(self.nb_disks):
                    self.poles[i].retirer_disque(self.disks[j])

        #On place les disques sur la barre 3 (index 2)
        if self.poles[2].count == 0:
            for i in range(self.nb_disks):
                self.disks[i].set_coords(self.poles[2].x, self.disks[i].y, 2, self.canvas)
                self.poles[2].ajouter_disque(self.disks[i])

        #On notifie le lancement du jeu
        print('Lancement du jeu depuis la barre 3')

        #On lance la boucle principale
        self.boucle()
    
    def lancer(self):
        #On lance la fenêtre
        self.window.mainloop()
        
#Si le script est lancé directement, on lance le jeu avec la fonction lancer()
if __name__ == '__main__':
    Jeu().lancer()
    
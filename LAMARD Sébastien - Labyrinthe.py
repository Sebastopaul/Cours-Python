# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 16:13:30 2024

@author: LAMARD Sébastien
"""

import tkinter as tk
from random import randint, seed
from time import sleep
from datetime import datetime

class Labyrinthe:
    def __init__(self):
        #On set une grille vide et deux booléen servant à savoir si le labyrinthe a été construit ou non, résolu ou non
        self.built = False
        self.solved = False
        self.grid = []

    def generate_lab(self, w, h):
        #A chaque regénération, on reset la grille vide et deux booléen servant à savoir si le labyrinthe a été construit ou non, résolu ou non
        self.grid = []
        self.built = False
        self.solved = False
        
        #On set également la taille du labytinthe
        self.w = w
        self.h = h
        
        #On choisi un début et une fin
        self.choose_begin_end()

        #On crée une grille avec 4 côtés côtés fermés, avec une alternance entre mur (0) et case vide inexplorée (1) à chaque ligne et colonne
        for i in range(self.h + 1):
            #A chaque nouvel index, on ajoute une liste à la grille, une ligne pour accueillir les valeurs des colonnes
            self.grid.append([])
            for j in range(self.w + 1):
                #On place les entrées et sorties à l'avance, en haut à gauche et en bas à droite
                if (i == self.starty and j == self.startx) or (i == self.stopy and j == self.stopx):
                    self.grid[i].append(1)
                elif i % 2 == 0:
                    self.grid[i].append(0)
                elif j % 2 == 0:
                    self.grid[i].append(0)
                else:
                    self.grid[i].append(1)

        #On génère un passage dans la grille créée en retirant des murs au fur et à mesure
        #On donne la case devant l'entrée comme paramètre de départ
        if self.startx == 0 and self.starty == 0:
            self.generate_paths(self.starty + 1, self.startx + 1)
        elif self.startx == 0:
            self.generate_paths(self.starty, self.startx + 1)
        elif self.starty == 0:
            self.generate_paths(self.starty + 1, self.startx)
        else:
            raise Exception('Start generation issue')

        #On affiche la grille du labyrinthe sous forme logique (liste de liste avec l'état logique des cases : 0 = mur, 1 = entrée/sortie, 2 = vide)
        for i in range(self.h + 1):
            print(self.grid[i])
        print('--------------------------------')
        self.built = True
        
    def choose_begin_end(self):
        #On choisi si l'entré se trouvera sur un mur vertical ou horizontal
        start_hv = randint(1, 2)

        #Si c'est un mur horizontal, on choisi le x au hasard et on prend le mur du haut
        if start_hv == 1:
            self.startx = randint(1, self.w - 1)
            self.starty = 0
            #Si on tombe sur un nombre pair, l'entrée risque de tomber sur un mur. On évite cela en ajoutant ou retirant 1 selon la position
            if self.startx % 2 == 0:
                if(self.startx == self.w - 1):
                    self.startx -= 1
                else:
                    self.startx += 1
        else:
            #Dans le cas contraire, on inverse les x et y
            self.starty = randint(1, self.h - 1)
            self.startx = 0
            #Si on tombe sur un nombre pair, l'entrée risque de tomber sur un mur. On évite cela en ajoutant ou retirant 1 selon la position
            if self.starty % 2 == 0:
                if(self.starty == self.h - 1):
                    self.starty -= 1
                else:
                    self.starty += 1

        #On choisi si la sortie se trouvera sur un mur vertical ou horizontal
        stop_hv = randint(1, 2)

        #Si c'est un mur horizontal, on choisi le x au hasard et on prend le mur du bas
        if stop_hv == 1:
            self.stopx = randint(1, self.w - 1)
            self.stopy = self.h
            #Si on tombe sur un nombre pair, la sortie risque de tomber sur un mur. On évite cela en ajoutant ou retirant 1 selon la position
            if self.stopx % 2 == 0:
                if(self.stopx == self.w - 1):
                    self.stopx -= 1
                else:
                    self.stopx += 1
        else:
            #Dans le cas contraire, on inverse les x et y
            self.stopy = randint(1, self.h - 1)
            self.stopx = self.w
            #Si on tombe sur un nombre pair, la sortie risque de tomber sur un mur. On évite cela en ajoutant ou retirant 1 selon la position
            if self.stopy % 2 == 0:
                if(self.stopy == self.h - 1):
                    self.stopy -= 1
                else:
                    self.stopy += 1

    def generate_paths(self, i, j):
        #On cherche le nombre de chemins pas encore explorés autour du point actuel
        paths = self.find_paths(i, j)
        #On remplace le point actuel par un 2 pour signaler qu'il est exploré
        self.grid[i][j] = 2

        #Tant qu'il reste une direction explorable, on recommence
        while (paths > 0):
            #On choisi un chemin à explorer parmis les chemins disponibles
            inext, jnext = self.choose_path(i, j, paths)
            #On casse le mur entre le point actuel et le point choisi
            self.break_wall(i, j, inext, jnext)
            #On fait fait la même chose pour le point suivant
            self.generate_paths(inext, jnext)
            #On recalcule le nombre de chemins disponibles lorsque l'on est de retour dans la fonction
            paths = self.find_paths(i, j)

    def find_paths(self, i, j):
        #On recherche le nombre de directions qu'il est possible de prendre à partir du point actuel
        paths = 4
        if i == self.h - 1 or (i != self.h - 1 and self.grid[i + 2][j] == 2):
            paths -= 1
        if i == 1 or (i != 1 and self.grid[i - 2][j] == 2):
            paths -= 1
        if j == self.w - 1 or (j != self.w - 1 and self.grid[i][j + 2] == 2):
            paths -= 1
        if j == 1 or (j != 1 and self.grid[i][j - 2] == 2):
            paths -= 1
            
        return paths

    def choose_path(self, i, j, paths):
        #On recherche quelles directions il est possible de prendre depuis le point actuel
        possible_paths = ['N', 'S', 'E', 'W']
        if i == self.h - 1 or (i != self.h - 1 and self.grid[i + 2][j] == 2):
            possible_paths.remove('S')
        if i == 1 or (i != 1 and self.grid[i - 2][j] == 2):
            possible_paths.remove('N')
        if j == self.w - 1 or (j != self.w - 1 and self.grid[i][j + 2] == 2):
            possible_paths.remove('E')
        if j == 1 or (j != 1 and self.grid[i][j - 2] == 2):
            possible_paths.remove('W')

        #On choisi une direction en fonction des directions qu'il est possible de prendre
        if paths == 0:
            return i, j
        if paths == 1:
            next_path = 0
        else:
            next_path = randint(0, paths - 1)

        #Selon la direction choisie, on renvoie des coordonnées différentes
        if possible_paths[next_path] == 'N':
            return i - 2, j
        if possible_paths[next_path] == 'S':
            return i + 2, j
        if possible_paths[next_path] == 'E':
            return i, j + 2
        if possible_paths[next_path] == 'W':
            return i, j - 2

    def break_wall(self, i, j, inext, jnext):
        #On remplace le 0 entre le point actuel et le prochain par un 2 pour signifier qu'il est fait
        if inext - i < 0:
            self.grid[i - 1][j] = 2
        if inext - i > 0:
            self.grid[i + 1][j] = 2
        if jnext - j < 0:
            self.grid[i][j - 1] = 2
        if jnext - j > 0:
            self.grid[i][j + 1] = 2

class Solver:
    def __init__(self, canvas):
        #On passe le labyrinthe au solver ainsi que le canva pour dessiner les chemins empruntés
        self.canvas = canvas

    def start_solving(self, lab, xmargin, ymargin):
        #On importe les données des marges et le labyrinthe pour dessiner les lignes et explorer le labyrinthe
        self.lab = lab
        self.xmargin = xmargin
        self.ymargin = ymargin

        self.solve_lab(self.lab.starty, self.lab.startx)
        
        #On affiche la grille du labyrinthe sous forme logique (liste de liste avec l'état logique des cases : 0 = mur, 2 = vide, 3 = exploré)
        for i in range(self.lab.h + 1):
            print(self.lab.grid[i])
        print('--------------------------------')

    def solve_lab(self, i, j):
        if i == self.lab.stopy and j == self.lab.stopx:
            self.lab.solved = True
            return
        
        #On cherche le nombre de chemins pas encore explorés autour du point actuel
        paths = self.find_paths(i, j)
        #On remplace le point actuel par un 3 pour signaler qu'il est exploré
        self.lab.grid[i][j] = 3

        while paths > 0 and self.lab.solved == False:
            #On choisi un chemin à explorer parmis les chemins disponibles
            inext, jnext = self.choose_path(i, j, paths)
            #On dessine une ligne du point actuel au point choisi et on attend 0.5 seconde pour la visibilité
            self.draw_line(i, j, inext, jnext)
            sleep(0.1)
            #On fait fait la même chose pour le point suivant
            self.solve_lab(inext, jnext)
            #On recalcule le nombre de chemins disponibles lorsque l'on est de retour dans la fonction
            paths = self.find_paths(i, j)

    def find_paths(self, i, j):
        #Pour chaque direction, on vérifie si le point suivant est un mur ou un point déjà exploré. Si c'est le cas, on retire 1 au possibilités de déplacement
        paths = 4
        if i == self.lab.h or (i != self.lab.h and (self.lab.grid[i + 1][j] == 3 or self.lab.grid[i + 1][j] == 0)):
            paths -= 1
        if i == 0 or (i != 0 and (self.lab.grid[i - 1][j] == 3 or self.lab.grid[i - 1][j] == 0)):
            paths -= 1
        if j == self.lab.w or (j != self.lab.w and (self.lab.grid[i][j + 1] == 3 or self.lab.grid[i][j + 1] == 0)):
            paths -= 1
        if j == 0 or (j != 0 and (self.lab.grid[i][j - 1] == 3 or self.lab.grid[i][j - 1] == 0)):
            paths -= 1
            
        return paths

    def choose_path(self, i, j, paths):
        #On recherche quelles directions il est possible de prendre depuis le point actuel
        possible_paths = ['N', 'S', 'E', 'W']
        if i == self.lab.h or (i != self.lab.h and (self.lab.grid[i + 1][j] == 3 or self.lab.grid[i + 1][j] == 0)):
            possible_paths.remove('S')
        if i == 0 or (i != 0 and (self.lab.grid[i - 1][j] == 3 or self.lab.grid[i - 1][j] == 0)):
            possible_paths.remove('N')
        if j == self.lab.w or (j != self.lab.w and (self.lab.grid[i][j + 1] == 3 or self.lab.grid[i][j + 1] == 0)):
            possible_paths.remove('E')
        if j == 0 or (j != 0 and (self.lab.grid[i][j - 1] == 3 or self.lab.grid[i][j - 1] == 0)):
            possible_paths.remove('W')

        #On choisi une direction en fonction des directions qu'il est possible de prendre
        if paths == 0:
            return i, j
        if paths == 1:
            next_path = 0
        else:
            next_path = randint(0, paths - 1)

        #Selon la direction choisie, on renvoie des coordonnées différentes
        if possible_paths[next_path] == 'N':
            return i - 1, j
        if possible_paths[next_path] == 'S':
            return i + 1, j
        if possible_paths[next_path] == 'E':
            return i, j + 1
        if possible_paths[next_path] == 'W':
            return i, j - 1

    def draw_line(self, i, j, inext, jnext):
        #On dessine la ligne avec pour point de départ le point actuel et pour point d'arrivée celui qui a été choisi comme prochain
        self.canvas.create_line((j + 1) * self.xmargin, (i + 1) * self.ymargin, (jnext + 1) * self.xmargin, (inext + 1) * self.ymargin, fill="red")
        #On rafraichit le canvas pour afficher la ligne
        self.canvas.update()

class Jeu:
    def __init__(self):
        #On initialise la taille du canva
        self.w = 800
        self.h = 600
        self.lab = Labyrinthe()
        
        #On crée la fenêtre
        self.window = tk.Tk()

        #On crée le Canva avec les dimensions prévues et on le place
        self.canvas = tk.Canvas(self.window, width = self.w, height = self.h, background = "white")
        self.canvas.pack(fill = "both", expand = True)
        
        #On crée le solver et on lui donne le canvas
        self.solver = Solver(self.canvas)

        #On crée un emplacement pour les inputs et boutons
        frame = tk.Frame()
        frame.pack(side = 'bottom', fill = 'x')

        #On configure les colonnes et lignes de l'emplacement poues les entry et boutons
        frame.columnconfigure(0, weight = 1)
        frame.columnconfigure(1, weight = 1)
        frame.columnconfigure(2, weight = 1)
        frame.columnconfigure(3, weight = 1)
        frame.rowconfigure(0, weight = 1)
        frame.rowconfigure(1, weight = 1)

        #On crée deux labels pour signaler l'utilité des entries        
        wlabel = tk.Label(frame, text="Largeur:")
        hlabel = tk.Label(frame, text="Hauteur:")

        #On crée deux entry pour la largeur et la longueur du labyrinthe
        self.winput = tk.Entry(frame, width = 10)
        self.hinput = tk.Entry(frame, width = 10)
        self.winput.insert(0, '20')
        self.hinput.insert(0, '20')

        #On crée deux boutons pour générer le labyrinthe, le résoudre et quitter la fenêtre
        btn_generate = tk.Button(frame,text = "Générer", width = 20, command = self.generate_lab)
        btn_solve = tk.Button(frame,text = "Résoudre", width = 20, command = self.solve_lab)
        btn_quit = tk.Button(frame,text = "Quitter", width = 20, command = self.window.destroy)

        #On place les entry et les boutons sur la grid de la frame, ainsi que les labels
        wlabel.grid(row=0, column=0, padx = 3, pady = 3)
        hlabel.grid(row=0, column=2, padx = 3, pady = 3)
        self.winput.grid_configure(row=0, column=1)
        self.hinput.grid_configure(row=0, column=3)
        btn_generate.grid(row=1, column=1, pady = 3, padx = 3)
        btn_solve.grid(row=1, column=2, pady = 3, padx = 3)
        btn_quit.grid(row=1, column=3, pady = 3, padx = 3)

    def generate_lab(self):
        #On récupère la taille voulue
        width = int(self.winput.get())
        height = int(self.hinput.get())

        #On vérifie qu'elle est valide (entre 5 et 20)
        if height < 5 or height > 100 or width < 5 or width > 100:
            print('Veuillez choisir des nombres entre 5 et 100.')
            return

        #Si le nombre est impair, on ajoute 1 à la taille afin d'éviter les doubles murs
        if height % 2 != 0:
            height += 1
        if width % 2 != 0:
            width += 1

        #On calcule une marge selon la taille de la fenêtre et la taille du labyrinthe
        self.xmargin = self.w / (width + 2)
        self.ymargin = self.h / (height + 2)

        #On crée le labyrinthe puis on le dessine
        self.lab.generate_lab(width, height)
        self.draw_lab()

    def draw_lab(self):
        #On nettoie le canvas
        self.canvas.delete("all")

        #Pour chaque case du labyrinthe, si la case est égale à 0, autrement dit s'il s'agit d'un mur, on dessine les traits le reliant à d'autres murs
        for i in range(self.lab.h + 1):
            for j in range(self.lab.w + 1):
                if self.lab.grid[i][j] == 0:
                    self.draw_line(i, j)

    def draw_line(self, i, j):
        #On vérifie le premier point vers les directions Est et Sud. S'il s'agit d'un mur également, on dessine une ligne entre les deux points
        if (i != self.lab.h and self.lab.grid[i + 1][j] == 0):
            self.canvas.create_line((j + 1) * self.xmargin, (i + 1) * self.ymargin, (j + 1) * self.xmargin, (i + 2) * self.ymargin)
        if (j != self.lab.w and self.lab.grid[i][j + 1] == 0):
            self.canvas.create_line((j + 1) * self.xmargin, (i + 1) * self.ymargin, (j + 2) * self.xmargin, (i + 1) * self.ymargin)

    def solve_lab(self):
        #Si le labyrinthe n'a pas été construit ou qu'il est déjà résolu, on affiche un message et on sort
        if self.lab.built == False or self.lab.solved == True:
            print('La labyrinthe n\'est pas instancié ou a déjà été résolu.')
            return

        #On lance la résolution avec le labyrinthe et les marges de dessin pour l'afficher au fur et à mesure
        self.solver.start_solving(self.lab, self.xmargin, self.ymargin)

    def lancer(self):
        #On change la seed au lancement du programme avec en paramètre les milisecondes tu temps actuel (valeur la plus aléatoire que j'ai trouvé)
        seed(datetime.now().microsecond)
        #On lance la fenêtre
        self.window.mainloop()

#Si le script est lancé directement, on lance le jeu avec la fonction lancer()
if __name__ == '__main__':
    Jeu().lancer()

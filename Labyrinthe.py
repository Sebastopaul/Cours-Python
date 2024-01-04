# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 16:13:30 2024

@author: sebay
"""

import tkinter as tk
from random import randint
#from time import sleep

class Labyrinthe:
    def __init__(self, w, h):
        self.w = w
        self.h = h

        #On crée une grille avec 4 côtés côtés fermés, avec une alternance entre mur (0) et case vide inexplorée (1) à chaque ligne et colonne
        self.grid = []
        for i in range(self.h + 1):
            self.grid.append([])
            for j in range(self.w + 1):
                if (i == 1 and j == 0) or (i == self.h - 1 and j == self.w):
                    self.grid[i].append(1)
                elif i % 2 == 0:
                    self.grid[i].append(0)
                elif j % 2 == 0:
                    self.grid[i].append(0)
                else:
                    self.grid[i].append(1)

        #On génère un passage dans la grille créée en retirant des murs au fur et à mesure
        self.generate_paths(1, 1)

        #On affiche la grille du labyrinthe sous forme logique (liste de liste avec l'état logique des cases : 0 = mur, 1 = entrée/sortie, 2 = vide)
        for i in range(self.h + 1):
            print(self.grid[i])
        print('-----------------------------------------------------------------')

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
            possible_paths.remove('E')
        if i == 1 or (i != 1 and self.grid[i - 2][j] == 2):
            possible_paths.remove('W')
        if j == self.w - 1 or (j != self.w - 1 and self.grid[i][j + 2] == 2):
            possible_paths.remove('S')
        if j == 1 or (j != 1 and self.grid[i][j - 2] == 2):
            possible_paths.remove('N')

        #On choisi une direction en fonction des directions qu'il est possible de prendre
        if paths == 0:
            return i, j
        if paths == 1:
            next_path = 0
        else:
            next_path = randint(0, paths - 1)

        #Selon la direction choisie, on renvoie des coordonnées différentes
        if possible_paths[next_path] == 'N':
            return i, j - 2
        if possible_paths[next_path] == 'S':
            return i, j + 2
        if possible_paths[next_path] == 'E':
            return i + 2, j
        if possible_paths[next_path] == 'W':
            return i - 2, j

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

class Jeu:
    def __init__(self):
        #On initialise la taille du canva
        self.w = 800
        self.h = 600
        
        #On crée la fenêtre
        self.window = tk.Tk()

        #On crée le Canva avec les dimensions prévues et on le place
        self.canvas = tk.Canvas(self.window, width = self.w, height = self.h, background = "white")
        self.canvas.pack(fill = "both", expand = True)

        #On crée un emplacement pour les inputs et boutons
        frame = tk.Frame()
        frame.pack(side = 'bottom', fill = 'x')

        #On configure les colonnes et lignes de l'emplacmeent poues les entry et boutons
        frame.columnconfigure(0, weight = 1)
        frame.columnconfigure(1, weight = 1)
        frame.rowconfigure(0, weight = 1)
        frame.rowconfigure(1, weight = 1)

        #On crée deux entry pour la largeur et la longueur du labyrinthe
        self.winput = tk.Entry(frame, width = 10)
        self.hinput = tk.Entry(frame, width = 10)
        self.winput.insert(0, 'Largeur')
        self.hinput.insert(0, 'Hauteur')
        #On crée deux boutons pour générer le labyrinthe et quitter la fenêtre
        btn_generate = tk.Button(frame,text = "Générer", width = 20, command = self.generate_lab)
        btn_quit = tk.Button(frame,text = "Quitter", width = 20, command = self.window.destroy)

        #On place les entry et les boutons sur la grid de la frame
        self.winput.grid_configure(row=0, column=0)
        self.hinput.grid_configure(row=0, column=1)
        btn_generate.grid(row=1, column=0, pady = 3, padx = 3)
        btn_quit.grid(row=1, column=1, pady = 3, padx = 3)

    def generate_lab(self):
        #On récupère la taille voulue
        width = int(self.winput.get())
        height = int(self.hinput.get())

        #On vérifie qu'elle est valide (entre 5 et 20)
        if height < 5 or height > 20 or width < 5 or width > 20:
            print('Veuillez choisir des nombres entre 5 et 20.')
            raise AssertionError

        #Si le nombre est impair, on ajoute 1 à la taille afin d'éviter les doubles murs
        if height % 2 != 0:
            height += 1
        if width % 2 != 0:
            width += 1

        #On calcule une marge selon la taille de la fenêtre et la taille du labyrinthe
        self.xmargin = self.w / (width + 2)
        self.ymargin = self.h / (height + 2)

        #On crée le labyrinthe puis on le dessine
        self.lab = Labyrinthe(width, height)
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

    def lancer(self):
        #On lance la fenêtre
        self.window.mainloop()

#Si le script est lancé directement, on lance le jeu avec la fonction lancer()
if __name__ == '__main__':
    Jeu().lancer()

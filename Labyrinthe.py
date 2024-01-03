# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 16:13:30 2024

@author: sebay
"""

from random import randint

class Labyrinthe:
    def __init__(self, w, h):
        self.w = w
        self.h = h

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

        self.generate_paths(1, 1)

        for i in range(self.h + 1):
            print(self.grid[i])

    def generate_paths(self, i, j):
        

class Jeu:
    def __init__(self):
        self.init_lab()
        self.init_window()

    def init_window(self):
        return

    def init_lab(self):
        height = int(input('Choisissez un nombre entre 5 et 20 pour la hauteur du labyrinthe: '))
        width = int(input('Choisissez un nombre entre 5 et 20 pour la largeur du labyrinthe: '))

        if height < 5 or height > 20 or width < 5 or width > 20:
            print('Veuillez choisir des nombres entre 5 et 20.')
            raise AssertionError

        if height % 2 != 0:
            height += 1
        if width % 2 != 0:
            width += 1

        self.lab = Labyrinthe(width, height)

if __name__ == '__main__':
    Jeu()

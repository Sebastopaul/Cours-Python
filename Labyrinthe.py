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
        paths = self.find_paths(i, j)
        
        while (paths > 0):
            inext, jnext = self.choose_path(i, j, paths)
            self.break_wall(i, j, inext, jnext)
            self.generate_paths(inext, jnext)
            paths = self.find_paths(i, j)

    def find_paths(self, i, j):
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
        possible_paths = ['N', 'S', 'E', 'W']
        if i == self.h - 1 or (i != self.h - 1 and self.grid[i + 2][j] == 2):
            possible_paths.remove('E')
        if i == 1 or (i != 1 and self.grid[i - 2][j] == 2):
            possible_paths.remove('W')
        if j == self.w - 1 or (j != self.w - 1 and self.grid[i][j + 2] == 2):
            possible_paths.remove('S')
        if j == 1 or (j != 1 and self.grid[i][j - 2] == 2):
            possible_paths.remove('N')

        rand = randint(1, paths)
        if possible_paths[rand] == 'N':
            return i, j - 2
        if possible_paths[rand] == 'S':
            return i, j + 2
        if possible_paths[rand] == 'E':
            return i + 2, j
        if possible_paths[rand] == 'W':
            return i - 2, j

    def break_wall(self, i, j, inext, jnext):
        return

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

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 11:39:03 2023

@author: bebo
"""

# Fonction pour la 3D
import time
import numpy as np
import matplotlib.pyplot as plt


# Tableau pour les 3 axes
# Création d'un tableau de 100 points entre -4*pi et 4*pi
for i in range(100) :
    theta = np.linspace(-4 * np.pi, 4 * np.pi, i)
    z = np.linspace(-2, 2, i)  # Création du tableau de l'axe z entre -2 et 2
    r = z**2 + 1
    x = r * np.sin(theta)  # Création du tableau de l'axe x
    y = r * np.cos(theta)  # Création du tableau de l'axe y

# Tracé du résultat en 3D
    fig = plt.figure()
    ax = fig.add_subplot(projection = '3d')  # Affichage en 3D
    ax.plot(x, y, z, label='Courbe')  # Tracé de la courbe 3D
    plt.title("Courbe 3D")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.tight_layout()
    plt.show()
    time.sleep(0.2)
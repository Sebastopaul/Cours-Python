# -*- coding: utf-8 -*-
"""
Created on Sun May  2 22:05:45 2021

@author: bebo
"""
# http://tkinter.fdex.eu/doc/caw.html#Canvas

# Importation de la librairie tkinter
# Cette librairie est utilisé pour développer des interfaces graphiques avec python
import tkinter as tk

# Un autre façons d'importer la librairie tkinter
# Dans la première façon on importe toute la librairie sous le nom tk
# Dans la deuxième façon on importe toute la librairie sans la renommer
#from tkinter import *

# Définition de la variable de largeur en pixel
largeur = 400
# Définition de la variable de hauteur en pixel
hauteur = 200
# Instanciation de la classe
fenetre = tk.Tk()

# Constructeur du widget canvas, en paramètre la fenêtre et en option la largeur, la hauteur et la couleur du fond
widget = tk.Canvas(fenetre,width = largeur, height = hauteur, background = "white")
# Créer le block du widget, en option le remplissage (ici horizontale et vertical), et s'il remplit le composant parent
widget.pack(fill = "both",expand = True)
# Variable de position x0 et y0, initialisé a 100 chacune pour le rectangle 1
x0,y0 = 100,100
# Variable de position x1 et y1, initialisé a 100 chacune pour le rectangle 2
x1,y1 = 300,100
# Vitesse de déplacement x initialisé à 5
dx = +5  # mettre un random fonction des clics sur le bouton "activer/accelere"
# Vitesse de déplacement y initialisé à 5
dy = +5  # mettre un random fonction des clics sur le bouton "activer/accelere"

# Vitesse de déplacement x du rectangle 2 initialisé à 5
dx1 = +5
# Vitesse de déplacement y du rectangle 2 initialisé à 5
dy1 = +5

# Création d'un rectangle, en paramètre x0 et y0 qui représente le haut gauche
# et x0+20 et y0 + 20 qui représente le coins inférieur droit, en option la largeur et la couleur de remplissage
rect = widget.create_rectangle(x0,y0,x0+20,y0+20,width = 2,fill = "red")
# Création du deuxième rectangle
rect2 = widget.create_rectangle(x1,y1,x1+20,y1+20,width = 2,fill = "blue")

# Définition de la fonction activer
def activer():
    # Permet de modifier les variables x0, y0, dx et dy en dehors de leurs portés
    global x0, y0, dx, dy, x1, y1, dx1, dy1
    # Ajoute dx à x0
    x0 = x0 + dx
    # Ajoute dy à y0
    y0 = y0 + dy

    # Ajout des variables du rectangle 2
    x1 = x1 + dx1
    y1 = y1 + dy1

    # Déplace le widget
    widget.coords(rect,x0,y0,x0+20,y0+20)
    widget.coords(rect2,x1,y1,x1+20,y1+20)

    # Si x0 est inférieur ou égal à 0 ou supérieur ou égal à la largeur
    if x0 <= 0 or x0 >= largeur:
        # dx prend la valeur inverse
        dx = -dx
    # Si y0 est inférieur ou égal à 0 ou supérieur ou égal à la hauteur
    if y0 <= 0 or y0 >= hauteur:
        # dy prend la valeur inverse
        dy = -dy

    # Même condition pour le rectangle 2
    if x1 <= 0 or x1 >= largeur:
        dx1 = -dx1
    if y1 <= 0 or y1 >= hauteur:
        dy1 = -dy1

    # Si détection d'une collision, un carré rentre dans l'autre
    if x0 < x1 + 20 and x0 + 20 > x1 and y0 < y1 + 20 and y0 + 20 > y1:
        # Inverse les trajectoires pour simuler le choc et le rebondissement
        dx = -dx
        dy = -dy
        dx1 = -dx1
        dy1 = -dy1

    # Après un délai de 50 millisecondes on appelle la fonction activer
    widget.after(50,activer) # fait deplacer le carre apres 50 milli seconde
    # Ne retourne rien
    return

# Définition de la fonction action_activer
def action_activer():
    # Appel la fonction activer
      activer()
    # Ne retourne rien
      return

# Création du bouton activer-accélerer avec en paramètre la fenêtre et en options le texte du bouton,
# la largeur et la fonction à appeler, ici action_activer
bouton_couleur = tk.Button(fenetre,text = "activer-accélérer", width = 20, command = action_activer)
# Créer le widget avec en option la taille du remplissage
bouton_couleur.pack(pady = 10)

# Création du bouton quitter avec en paramètre la fenêtre et en option le test du bouton, la largeur et
# la fonction à appeler, ici fenetre.destroy pour quitter
bouton_quitter = tk.Button(fenetre,text = "Quitter" ,width = 20, command=fenetre.destroy)
# Créer le widget avec en option le côté du parent sur lequel il va être placé et la taille du remplissage
bouton_quitter.pack(side = tk.BOTTOM,pady = 10)

# Permet de lancer le programme et attend les actions de l'utilisateur afin de réagir à celle-ci, elle permet
# au programme de ne pas se fermer tant que l'utilisateur ne l'a pas demandé.
fenetre.mainloop()  # exécution de la fenetre hors "plots" sous spyder (derrière la fenetre de spyder)
 
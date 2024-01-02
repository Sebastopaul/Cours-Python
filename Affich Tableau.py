# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 16:58:15 2022

@author: BEBO
"""

from numpy import zeros,array

#déclaration d'une variable de type tableau de 10 entiers
monTableau = zeros(10, int)

#déclaration d'une matrice 5 x 3 (tableau de tableaux) de réels
maMatrice = zeros((5,3), float)

#déclaration d'une variable de type tableau de 4 entiers
unTableau = array([12, 15, 11, 18])
#déclaration d'une matrice de 2x3 réels
uneMatrice = array([[1.2, 3.4,5.6],[7.8, 8.9, 9.0]])

unTableau = array([12, 15, 11, 18])
print("taille du tableau unTableau = " + str(len(unTableau )))

uneMatrice = array([[1.2, 3.4,5.6],[7.8, 8.9, 9.0]])
dim = uneMatrice.shape

print("nb de lignes de uneMatrice=" + str(dim[0]))
print("nb de colonnes de uneMatrice=" + str(dim[1]))

def afficherTab(tab, n):
   for i in range(0,n):
      print(str(tab[i]), ", afficher tab ")
   print()
##demande n entiers à l'utilisateur et les stocke dans le tableau t
def stockerDansTab(tab, n):
   for i in range(0,n):
      print("Entrez la valeur " +str( i+1) + " : ")
      
      tab[i] = int(input())  ######### pb input
      
##affiche les n premiers entiers du tableau t

   

def afficherTab2(tab):
   for elt in tab:
      print(str(elt), ", afficher elt ");
   print()
   
matrice = array([[2,7,6],[9,5,1],[4,3,8]])
for i in range(0,3):
   for j in range(0,3):
      print(str(matrice[i][j]),", afficher array ")
print()
  
for ligne in matrice: #pour chaque ligne de la matrice
   for elt in ligne: #pour chaque élément de la ligne
      print(elt, end=", ")
   print()
tab = array([2,7,6,9,5,1,4,3,8])
petit_tab = tab[1:4]
#petit_tab reçoit les valeurs tab[1], tab[2] et tab[3]
#-> petit_tab=[7,6,9]
#n =  int(input('rentrez n : '))  ########### pb input
#=afficherTab(tab, n)
  
  
  
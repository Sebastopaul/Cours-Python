# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 15:49:30 2024

@author: sebay
"""

import tkinter as tk

launched = False

largeur = 400
hauteur = 200
fenetre = tk.Tk()

widget = tk.Canvas(fenetre,width = largeur, height = hauteur, background = "white")
widget.pack(fill = "both",expand = True)

btnFrame = tk.Frame()
btnFrame.pack(side = 'bottom', fill = 'x')

px0, py0 = 100, 100
px1, py1 = 200, 100
px2, py2 = 300, 100

pole0 = widget.create_rectangle(px0,py0,px0+10,py0+50,width = 2,fill = "grey")
pole1 = widget.create_rectangle(px1,py1,px1+10,py1+50,width = 2,fill = "grey")
pole2 = widget.create_rectangle(px2,py2,px2+10,py2+50,width = 2,fill = "grey")

def launch_1():
    return

def launch_2():
    return

def launch_3():
    return

btn1 = tk.Button(btnFrame,text = "1", width = 5, command = launch_1)
btn2 = tk.Button(btnFrame,text = "2", width = 5, command = launch_2)
btn3 = tk.Button(btnFrame,text = "3", width = 5, command = launch_3)

btnFrame.columnconfigure(0, weight=1)
btnFrame.columnconfigure(1, weight=1)
btnFrame.columnconfigure(2, weight=1)
btnFrame.rowconfigure(0, weight=1)
btnFrame.rowconfigure(1, weight=1)

btn1.grid(row=0, column=0, pady = 3, padx = 50, sticky='W')
btn2.grid(row=0, column=1, pady = 3, padx = 3)
btn3.grid(row=0, column=2, pady = 3, padx = 50, sticky='E')

bouton_quitter = tk.Button(btnFrame,text = "Quitter", width = 20, command=fenetre.destroy)
bouton_quitter.grid(row=1, column=1, pady = 3)

fenetre.mainloop()
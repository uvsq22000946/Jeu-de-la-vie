#################################
# Auteur : Maxime Ebran
# MIASHS TD 2
#################################

#################################
# Import de librairie :

import tkinter as tk

#################################
# Variables globales

COULEUR_FONT = "black"
WIDTH = 500
HEIGHT = 500

#################################
# Fonctions

def quadrillage():
    """Affiche un quadrillage sur le canvas"""
    for x in range(20):
        canvas.create_line((x * 25, 0), (x * 25, 500), fill="white")
    for y in range(20):
        canvas.create_line((0, y * 25), (500, y * 25), fill="white")

#################################
# Programme principal

racine = tk.Tk()
racine.title("Jeu de la vie")

#Creation des widgets
canvas = tk.Canvas(racine, width=WIDTH, height=HEIGHT, bg=COULEUR_FONT)
quadrillage()

# Positionnent des widgets
canvas.grid()
racine.mainloop()
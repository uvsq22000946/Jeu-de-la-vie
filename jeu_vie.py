#################################
# Auteur : Maxime Ebran
# MIASHS TD X
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
        canevas.create_line((x * 25, 0), (x * 25, 500), fill="white")
    for y in range(20):
        canevas.create_line((0, y * 25), (500, y * 25), fill="white")

#################################
# Programme principal

racine = tk.Tk()
racine.title("Jeu de la vie")

#Creation des widgets
canevas = tk.Canvas(racine, width=WIDTH, height=HEIGHT, bg=COULEUR_FONT)
quadrillage()

# Positionnent des widgets
canevas.grid()
racine.mainloop()
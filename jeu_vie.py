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
tableau = None
NB_COL = 20
NB_LINE =20
COTE = 25

#################################
# Fonctions

def quadrillage():
    """Affiche un quadrillage sur le canvas"""
    for x in range(NB_COL):
        canvas.create_line((x * COTE, 0), (x * COTE, HEIGHT), fill="white")
    for y in range(NB_LINE):
        canvas.create_line((0, y * COTE), (WIDTH, y * COTE), fill="white")

def conversion(x, y):
    """Fonction qui retourne la colone et la ligne du quadrillage en fonction des coordonnés"""
    return x // COTE, y // COTE

def change_carre(event):
    """Au clic, change l'état du carre"""
    i, j = conversion(event.x, event.y)
    if tableau[i][j] == -1:
        x, y = i * COTE, j * COTE
        canvas.create_rectangle(x, y, x + COTE, y + COTE, fill="green", outline="white")

def creer_tableau():
    """Initialise un tableau qui vaut -1 pour une case morte et l'identifiant du carre si une case est vivante"""
    global tableau
    tableau_col = [-1] * NB_LINE
    tableau = [tableau_col for i in range(NB_COL)]


#################################
# Programme principal

racine = tk.Tk()
racine.title("Jeu de la vie")

#Creation des widgets
canvas = tk.Canvas(racine, width=WIDTH, height=HEIGHT, bg=COULEUR_FONT)
quadrillage()
creer_tableau()

# Positionnent des widgets
canvas.grid()

# Traitement des events

canvas.bind('<Button-1>', change_carre)


racine.mainloop()
##################################
# Auteur : Maxime Ebran
##################################

##################################
# Import

import tkinter as tk

##################################
# Variables

player = []

##################################
# Fonctions

def quadrillage():
    """Trace le quadrillage sur le canvas"""
    for x in range(20):
        canvas.create_line((x * 25, 0), (x * 25, 500), fill="white")
    for y in range(20):
        canvas.create_line((0, y * 25), (500, y * 25), fill="white")

def menu_combattre():
    """Menu du combat"""
    global combattre
    combattre = tk.Toplevel(racine, bg="black")
    Intitule = tk.Label(combattre, text="Choisissez votre adversaire", font=("Helvatica", "25"), bg="black", fg="white")
    boutton_garuda = tk.Button(combattre, text="Garuda", font=("Helvatica", "25"), bg="black", fg="white", command=garuda)

    Intitule.grid(row=0)
    boutton_garuda.grid(row=1)

def garuda():
    """Combat contre Garuda"""
    global position_player
    combattre.destroy()
    position_player = [10, 15]
    player.append(canvas.create_rectangle((position_player[0] * 25, position_player[1] * 25), (position_player[0] * 25 + 25, position_player[1] * 25 + 25), fill="green"))
    boutton_nord.config(command=nord)
    boutton_sud.config(command=sud)
    boutton_est.config(command=est)
    boutton_ouest.config(command=ouest)
    

def nord():
    """Avance le player vers le haut"""
    global canvas, position_player, player
    canvas.delete(player[-1])
    position_player[1] -= 1
    player.append(canvas.create_rectangle((position_player[0] * 25, position_player[1] * 25), (position_player[0] * 25 + 25, position_player[1] * 25 + 25), fill="green"))

def sud():
    """Avance le player vers le bas"""
    global canvas, position_player, player
    canvas.delete(player[-1])
    position_player[1] += 1
    player.append(canvas.create_rectangle((position_player[0] * 25, position_player[1] * 25), (position_player[0] * 25 + 25, position_player[1] * 25 + 25), fill="green"))

def est():
    """Avance le player vers la droite"""
    global canvas, position_player, player
    canvas.delete(player[-1])
    position_player[0] += 1
    player.append(canvas.create_rectangle((position_player[0] * 25, position_player[1] * 25), (position_player[0] * 25 + 25, position_player[1] * 25 + 25), fill="green"))

def ouest():
    """Avance le player vers la gauche"""
    global canvas, position_player, player
    canvas.delete(player[-1])
    position_player[0] -= 1
    player.append(canvas.create_rectangle((position_player[0] * 25, position_player[1] * 25), (position_player[0] * 25 + 25, position_player[1] * 25 + 25), fill="green"))


##################################
# Programme principal

racine = tk.Tk()
racine.title("Final Boss")
racine.config(bg="black")

canvas = tk.Canvas(racine, height=500, width=500, bg="black")
quadrillage()
boutton_nord = tk.Button(racine, text="N", font=("Helvatica", "30"), fg="white", bg="black")
boutton_sud = tk.Button(racine, text="S", font=("Helvatica", "30"), fg="white", bg="black")
boutton_est = tk.Button(racine, text="E", font=("Helvatica", "30"), fg="white", bg="black")
boutton_ouest = tk.Button(racine, text="W", font=("Helvatica", "30"), fg="white", bg="black")
boutton_inventaire = tk.Button(racine, text="Inventaire", font=("Helvatica", "30"), fg="white", bg="black")
boutton_combat = tk.Button(racine, text="Combattre", font=("Helvatica", "30"), fg="white", bg="black", command=menu_combattre)


canvas.grid(column=0, row=0, rowspan=7, columnspan=6)
boutton_nord.grid(column=7, row=1)
boutton_sud.grid(column=7, row=3)
boutton_est.grid(column=8, row=2)
boutton_ouest.grid(column=6, row=2)
boutton_inventaire.grid(column=6, row=4, columnspan=3)
boutton_combat.grid(column=6, row=5, columnspan=3)
racine.mainloop()
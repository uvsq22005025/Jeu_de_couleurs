#########################################
# Groupe MIASHS 4
# RASOLONJATOVO RINA ANDRIANINA
# ZAGMO BONNI RAMEZ
# VILHES LEA
# MAGHLAOUA ILYES
# AHMED KAISS BOURHA
# FALLIES CHARLOTTE
#########################################


# import de la librairie

from tkinter import *
import tkinter.font as font
import random
#########################################


# definition des fonctions
couleurs = ["RED", "BLUE", "GREEN", "PINK", "ORANGE", "YELLOW", "WHITE"]
temps = 30
score = 0
couleur_random = ''


def debut_du_jeu():
    """fonction qui initialise le debut du jeu"""
    global couleur_random
    if(temps == 30):
        Compte_a_rebours()
        couleur_random = random.choice(couleurs)
        affichage_mots.config(text=random.choice(couleurs), fg=couleur_random)


def Compte_a_rebours():
    """fonction qui initialise le compte à rebours"""
    global temps
    if(temps >= 0):
        temps_restant.config(text="Temps restant : " + str(temps))
        temps -= 1
        temps_restant.after(1000, Compte_a_rebours)
        if (temps == -1):
            temps_restant.config(text="Temps restant : 0")


def prochainmots(idx):
    global couleur_random
    global score
    global couleurs
    if(temps > 0):
        if(couleurs[idx] == couleur_random):
            score += 1
            score_jeu.config(text=" Score : " + str(score))
        couleur_random = random.choice(couleurs)
        affichage_mots.config(text=random.choice(couleurs), fg=couleur_random)


def rejouer():
    global score, temps
    score = 0
    score_jeu.config(text="Score :" + str(score))
    temps = 30
    temps_restant.config(text="Temps restant : " + str(temps))


#########################################

# Programme principal
ma_fenetre = Tk()
ma_fenetre.title("Jeu de couleurs")
ma_fenetre.geometry("600x500")
# creation des widgets
parametre_font = font.Font(family='Arial', size=13)
description_jeu = Label(ma_fenetre, text="Tapez la couleur des mots, et pas le texte des mots !!!",
                        font=parametre_font, fg="black")
score_jeu = Label(ma_fenetre, text="Score : " + str(score), font=parametre_font, fg="black")
temps_restant = Label(ma_fenetre, text="Temps restant : 30", font=parametre_font, fg="black")
affichage_mots = Label(ma_fenetre, font=(font.Font(size=26)), pady=10)
btn_frame2 = Frame(ma_fenetre, width=80, height=60)
# placements des widgets
description_jeu.pack()
score_jeu.pack()
temps_restant.pack()
affichage_mots.pack()
btn_frame2.pack(side=TOP)


#########################################
# Creation de boutons et placements

"""Boutons de couleurs"""
# Bouton rouge
boutton_rouge = Button(btn_frame2, text="Rouge ", width=5, font=(font.Font(weight="bold", size=10)),
                       fg="black", bg="red", bd=0, padx=10, pady=10, command=lambda: prochainmots(0))
boutton_rouge.grid(row=0, column=0, padx=10, pady=10)
# Bouton bleu
boutton_bleu = Button(btn_frame2, text="Bleu ", width=5, font=(font.Font(weight="bold", size=10)),
                      fg="black", bg="blue", bd=0, padx=10, pady=10, command=lambda: prochainmots(1))
boutton_bleu.grid(row=0, column=1, padx=10, pady=10)
# Bouton vert
boutton_vert = Button(btn_frame2, text="Vert ", width=5, font=(font.Font(weight="bold", size=10)),
                      fg="black", bg="green", bd=0, padx=10, pady=10, command=lambda: prochainmots(2))
boutton_vert.grid(row=0, column=2, padx=10, pady=10)
# Bouton rose
boutton_rose = Button(btn_frame2, text="Rose  ", width=5, font=(font.Font(weight="bold", size=10)),
                      fg="black", bg="pink", bd=0, padx=10, pady=10, command=lambda: prochainmots(3))
boutton_rose.grid(row=0, column=3, padx=10, pady=10)
# Bouton orange
boutton_orange = Button(btn_frame2, text="Orange  ", width=5, font=(font.Font(weight="bold", size=10)),
                        fg="black", bg="orange", bd=0, padx=10, pady=10,
                        command=lambda: prochainmots(4))
boutton_orange.grid(row=0, column=4, padx=10, pady=10)
# Bouton jaune
boutton_jaune = Button(btn_frame2, text="Jaune ", width=5, font=(font.Font(weight="bold", size=10)),
                       fg="black", bg="yellow", bd=0, padx=10, pady=10, command=lambda: prochainmots(5))
boutton_jaune.grid(row=1, column=2, pady=10)
# Bouton blanc
boutton_blanc = Button(btn_frame2, text="Blanc ", width=5, font=(font.Font(weight="bold", size=10)),
                       fg="black", bg="white", bd=0, padx=10, pady=10, command=lambda: prochainmots(6))
boutton_blanc.grid(row=1, column=3, pady=10)


"""Boutons de fonctionnement"""
# Le Frame sert à positionner les boutons de couleurs par rapport aux boutons de fonctionnement
btn_frame = Frame(ma_fenetre, width=60, height=20)
btn_frame.pack(side=BOTTOM)
# Bouton demarrer
bouton_demarrer = Button(btn_frame, text="Démarrer", width=20, fg="black", bg="grey",
                         pady=10, relief="flat", command=debut_du_jeu)
bouton_demarrer.grid(row=0, column=0, padx=10, pady=10)
# Bouton reinitialiser
bouton_reinitialiser = Button(btn_frame, text="Réinitialiser", width=20, fg="black",
                              bg="grey", pady=10, relief="flat", command=rejouer)
bouton_reinitialiser.grid(row=0, column=1, padx=270, pady=10)


#########################################
# boucle pricipale
ma_fenetre.mainloop()

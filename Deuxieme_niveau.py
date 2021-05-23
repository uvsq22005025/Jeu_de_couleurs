
#######################
# Groupe MIASHS 4
# RASOLONJATOVO RINA ANDRIANINA
# ZAGMO BONNI RAMEZ
# VHILES LEA
# MAGHLAOUA ILYES
# AHMED KAISS BOURHA
# FALLIES CHARLOTTE
#######################


#######################
# import de la librairie


from tkinter import *
import tkinter.font as font
import random


#######################
# définition des variables globales


couleurs = ["RED", "BLUE", "GREEN", "PINK", "ORANGE", "YELLOW", "WHITE"]
mots = ["RED", "BLUE", "GREEN", "PINK", "ORANGE", "YELLOW", "WHITE"]
labels = []
nombre = 0
couleur_random = ''
temps = 30
score = 0
couleur_a_afficher = []
text_a_afficher = []
WIDTH = 600
HEIGHT = 380
nbclick = 0
reponse = []
comment_jouer = "Tapez la couleur des mots, et pas le texte des mots !!!"


#######################
# définition des fonctions


def debut_du_jeu():
    """fonction qui initialise le debut du jeu"""
    global couleur_random, nombre, labels
    global couleur_a_afficher, text_a_afficher
    couleur_a_afficher.clear
    text_a_afficher.clear
    nombre = random.randint(2, 6)
    generermot(nombre)
    create_labels(nombre)
    if(temps == 30):
        Compte_a_rebours()
        for i in range(nombre):
            labels[i].config(text=text_a_afficher[i], fg=couleur_a_afficher[i])


def Compte_a_rebours():
    """fonction qui initialise le compte à rebours"""
    global temps
    if(temps >= 0):
        temps_restant.config(text="Temps restant : " + str(temps))
        temps -= 1
        temps_restant.after(1000, Compte_a_rebours)
        if (temps == -1):
            temps_restant.config(text="Temps restant : 0")


def generermot(nombre):
    """ fonction qui génère le mot composé dans une liste"""
    global couleur_random
    for i in range(nombre):
        text_a_afficher.append(mots[random.randint(0, len(mots)-1)])
        couleur_a_afficher.append(couleurs[random.randint(0, len(couleurs)-1)])


def create_labels(nombre):
    """fonction qui place le mots composé dans un label de texte et insère le
     tout dans un frame( fenetre fille )pour tout centralisé sur le canevas"""
    global labels
    labels.clear
    y = 0
    lblframe = Frame(canevas, width=WIDTH, height=HEIGHT)
    lblframe.grid(row=3, column=0, padx=25, pady=25, sticky="w")
    for i in range(nombre):
        lbl = Label(lblframe, font=(font.Font(size=16)), bg='grey74')
        lbl.grid(row=3, column=y)
        labels.append(lbl)
        y += 1


def prochainmots(idx):
    """fonction qui controle les couleurs saisies et les couleurs affichées;
    Si elles correspondent alors on génère un nouveau mot composé"""
    global nombre, score, couleurs, labels
    global nbclick, reponse, couleur_a_afficher, text_a_afficher
    if(temps > 0):
        reponse.append(couleurs[idx])
        nbclick += 1
        if nbclick == nombre:
            if reponse == couleur_a_afficher:
                score += 1
                score_jeu.config(text=" Score : " + str(score))
            for i in range(len(labels)):
                labels[i].destroy()
            labels.clear()
            nombre = random.randint(2, 6)
            nbclick = 0
            create_labels(nombre)
            reponse = []
            text_a_afficher = []
            couleur_a_afficher = []
            generermot(nombre)
            for i in range(nombre):
                labels[i].config(text=text_a_afficher[i], fg=couleur_a_afficher[i])


def rejouer():
    """fonction qui permet de reinitliser le score et
    le temps pour jouer à nouveau"""
    global score, temps
    score = 0
    score_jeu.config(text="Score :" + str(score))
    temps = 30
    temps_restant.config(text="Temps restant : " + str(temps))


#######################
# programme principal
ma_fenetre = Tk()
ma_fenetre.title("Jeu de couleurs")
ma_fenetre.geometry('600x380')
ma_fenetre.resizable(width=False, height=False)
# creation des widgets
canevas = Canvas(ma_fenetre, width=WIDTH, height=HEIGHT, bg='grey74')
parametre_font = font.Font(family='Ubuntu', size=14)
description_jeu = Label(canevas, text=comment_jouer, font=parametre_font, fg="black")
score_jeu = Label(canevas, text="Score : " + str(score), font=parametre_font, fg="black")
temps_restant = Label(canevas, text="Temps restant : 30", font=parametre_font, fg="black")
# placements des widgets
canevas.grid()
description_jeu.grid(row=0, column=0, columnspan=1, padx=50, sticky='w')
score_jeu.grid(row=1, column=0, padx=250, sticky='w')
temps_restant.grid(row=2, column=0, padx=210, sticky='w')


#######################
# Creation de boutons et placements

"""boutons de couleurs"""
# Bouton rouge
boutton_rouge = Button(canevas, text="Rouge ", width=5, font=(font.Font(weight="bold", size=10)),
                       fg="black", bg="red", bd=0, padx=10, pady=10, command=lambda: prochainmots(0))
boutton_rouge.grid(row=4, column=0, padx=50, pady=0, sticky='w')
# Bouton bleu
boutton_bleu = Button(canevas, text="Bleu ", width=5, font=(font.Font(weight="bold", size=10)),
                      fg="black", bg="blue", bd=0, padx=10, pady=10, command=lambda: prochainmots(1))
boutton_bleu.grid(row=4, column=0, padx=150, pady=0, sticky='w')
# Bouton vert
boutton_vert = Button(canevas, text="Vert ", width=5, font=(font.Font(weight="bold", size=10)),
                      fg="black", bg="green", bd=0, padx=10, pady=10, command=lambda: prochainmots(2))
boutton_vert.grid(row=4, column=0, padx=250, pady=0, sticky='w')
# Bouton rose
boutton_rose = Button(canevas, text="Rose", width=5, font=(font.Font(weight="bold", size=10)),
                      fg="black", bg="pink", bd=0, padx=10, pady=10, command=lambda: prochainmots(3))
boutton_rose.grid(row=4, column=0, padx=350, pady=0, sticky='w')
# Bouton orange
boutton_orange = Button(canevas, text="Orange  ", width=5, font=(font.Font(weight="bold", size=10)),
                        fg="black", bg="orange", bd=0, padx=10, pady=10,
                        command=lambda: prochainmots(4))
boutton_orange.grid(row=4, column=0, padx=450, pady=0, sticky='w')
# Bouton jaune
boutton_jaune = Button(canevas, text="Jaune ", width=5, font=(font.Font(weight="bold", size=10)),
                       fg="black", bg="yellow", bd=0, padx=10, pady=10, command=lambda: prochainmots(5))
boutton_jaune.grid(row=5, column=0, padx=200, pady=25, sticky='w')
# Bouton blanc
boutton_blanc = Button(canevas, text="Blanc", width=5, font=(font.Font(weight="bold", size=10)),
                       fg="black", bg="white", bd=0, padx=10, pady=10, command=lambda: prochainmots(6))
boutton_blanc.grid(row=5, column=0, padx=300, pady=25, sticky='w')

"""boutons de fonctionnement"""
# Bouton de demarrage
bouton_demarrer = Button(canevas, text="Démarrer", width=20, fg="black", bg="gainsboro", pady=10,
                         relief="flat", command=debut_du_jeu)
bouton_demarrer.grid(row=6, column=0, padx=10, pady=20, sticky='w')
# Bouton de reinitialisation
bouton_reinitialiser = Button(canevas, text="Réinitialiser", width=20, fg="black", bg="gainsboro",
                              pady=10, relief="flat", command=rejouer)
bouton_reinitialiser.grid(row=6, column=0, padx=440, pady=20, sticky='w')


#######################
# boucle pricipale
"""raffraichis la fenetre"""
ma_fenetre.mainloop()

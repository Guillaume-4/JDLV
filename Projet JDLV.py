from tkinter import *
from tkinter.messagebox import showinfo
from datetime import datetime
from time import strftime
import os

def dessin_grille() :
# dessin des lignes verticales
    x=100
    for i in range(21):
        y1=0
        y2=600
        Zone.create_line (x , y1 , x , y2 ,width=4,fill="blue")
        x=x+30
# dessin des lignes horizontales
    y = 0
    for i in range(21):
        x1=100
        x2=700
        Zone.create_line (x1 , y , x2 , y ,width=4,fill="blue")
        y= y + 30
    fen.after(500,dessin_grille)

#fonction appelée à chaque clic
def coordonnees(event):
    if valide == False:
        x,y = event.x, event.y
        coord_x = (x-100)//30
        coord_y = y//30
        if coord_x < 0 or coord_y < 0:
            return
        elif tab_grille[coord_y][coord_x]== 1:
            return
        else:
            tab_grille[coord_y][coord_x] = 1
            dessiner_creature(coord_y,coord_x)
    elif valide == True:
        return



def validation_du_jeu():
    global valide
    if valide == False:
        valide = True
        message = showinfo("Information","Vous venez de validé le placement des créatures")
    elif valide == True:
        message = showinfo("Erreur !","Vous avez déjà validé le placement des créatures")




def jour_suivant():
    for x in range(20):
            for y in range(20):
                futur[x][y] = 0
    c = 0
    if valide == False:
        message = showinfo("Veuillez validé","Le choix des créature doit être fait avant de passé au jour suivant")
    elif valide == True :
        for x in range(20):
            for y in range(20):
                if tab_grille[x][y] == 1:
                    futur[x][y] = 1
        for x in range(20):
            for y in range(20):
                c = 0
                if futur[x][y] == 1:
                    if x == 0 and y == 0: #coin en haut a gauche
                        c = c + futur[x+1][y]
                        c = c + futur[x][y+1]
                        c = c + futur[x+1][y+1]
                        if c <= 1 or c > 3:
                            tab_grille[x][y] = 0
                            Zone.create_oval(y*30+100 , x*30 , y*30+100 +25 , x*30+25 ,width=2 ,outline="gray",fill="gray")

                    elif x == 19 and y == 0: #coin en haut à droite
                        c = c + futur[x-1][y]
                        c = c + futur[x][y+1]
                        c = c + futur[x-1][y-1]
                        if c <= 1 or c > 3:
                            tab_grille[x][y] = 0
                            Zone.create_oval(y*30+100 , x*30 , y*30+100 +25 , x*30+25 ,width=2 ,outline="gray",fill="gray")

                    elif x == 0 and y == 19: #coin en bas a gauche
                        c = c + futur[x][y-1]
                        c = c + futur[x+1][y-1]
                        c = c + futur[x+1][y]
                        if c <= 1 or c > 3:
                            tab_grille[x][y] = 0
                            Zone.create_oval(y*30+100 , x*30 , y*30+100 +25 , x*30+25 ,width=2 ,outline="gray",fill="gray")

                    elif x == 19 and y == 19: #coin en bas a droite
                        c = c + futur[x-1][y]
                        c = c + futur[x][y-1]
                        c = c + futur[x-1][y-1]
                        if c <= 1 or c > 3:
                            tab_grille[x][y] = 0
                            Zone.create_oval(y*30+100 , x*30 , y*30+100 +25 , x*30+25 ,width=2 ,outline="gray",fill="gray")

                    elif y == 0 and 0<x<19:#première ligne mais on enlève les coins
                        c = c + futur[x-1][y]
                        c = c + futur[x+1][y]
                        c = c + futur[x-1][y+1]
                        c = c + futur[x][y+1]
                        c = c + futur[x+1][y+1]
                        if c <= 1 or c > 3:
                            tab_grille[x][y] = 0
                            Zone.create_oval(y*30+100 , x*30 , y*30+100 +25 , x*30+25 ,width=2 ,outline="gray",fill="gray")

                    elif y == 19 and 0<x<19:#dernière ligne mais on enlève les coins
                        c = c + futur[x-1][y-1]
                        c = c + futur[x][y-1]
                        c = c + futur[x+1][y-1]
                        c = c + futur[x-1][y]
                        c = c + futur[x+1][y]
                        if c <= 1 or c > 3:
                            tab_grille[y][y] = 0
                            Zone.create_oval(y*30+100 , x*30 , y*30+100 +25 , x*30+25 ,width=2 ,outline="gray",fill="gray")

                    elif x == 0 and 0<y<19:#première colone mais on enlève les coins
                        c = c + futur[x][y-1]
                        c = c + futur[x+1][y-1]
                        c = c + futur[x+1][y]
                        c = c + futur[x][y+1]
                        c = c + futur[x+1][y+1]
                        if c <= 1 or c > 3:
                            tab_grille[x][y] = 0
                            Zone.create_oval(y*30+100 , x*30 , y*30+100 +25 , x*30+25 ,width=2 ,outline="gray",fill="gray")

                    elif x == 19 and 0<y<19:#dernière colone mais on enlève les coins
                        c = c + futur[x][y-1]
                        c = c + futur[x-1][y-1]
                        c = c + futur[x-1][y]
                        c = c + futur[x][y+1]
                        c = c + futur[x-1][y+1]
                        if c <= 1 or c > 3:
                            tab_grille[x][y] = 0
                            Zone.create_oval(y*30+100 , x*30 , y*30+100 +25 , x*30+25 ,width=2 ,outline="gray",fill="gray")


                    else:
                        c = c + futur[x-1][y-1]
                        c = c + futur[x][y-1]
                        c = c + futur[x+1][y-1]
                        c = c + futur[x-1][y]
                        c = c + futur[x+1][y]
                        c = c + futur[x-1][y+1]
                        c = c + futur[x][y+1]
                        c = c + futur[x+1][y+1]
                        if c <= 1 or c > 3:
                            tab_grille[x][y] = 0
                            Zone.create_oval(y*30+100 , x*30 , y*30+100 +25 , x*30+25 ,width=2 ,outline="gray",fill="gray")

                elif futur[x][y] == 0:
                    if x == 0 and y == 0: #coin en haut a gauche
                        c = c + futur[x+1][y]
                        c = c + futur[x][y+1]
                        c = c + futur[x+1][y+1]
                        if c ==3:
                                tab_grille[x][y] = 1
                                Zone.create_oval(y*30+100 , x*30 , y*30+100 +25 , x*30+25 ,width=2 ,outline="yellow",fill="yellow")

                    elif x == 19 and y == 0: #coin en haut à droite
                        c = c + futur[x-1][y]
                        c = c + futur[x][y+1]
                        c = c + futur[x-1][y-1]
                        if c ==3:
                                tab_grille[x][y] = 1
                                Zone.create_oval(y*30+100 , x*30 , y*30+100 +25 , x*30+25 ,width=2 ,outline="yellow",fill="yellow")

                    elif x == 0 and y == 19: #coin en bas a gauche
                        c = c + futur[x][y-1]
                        c = c + futur[x+1][y-1]
                        c = c + futur[x+1][y]
                        if c ==3:
                                tab_grille[x][y] = 1
                                Zone.create_oval(y*30+100 , x*30 , y*30+100 +25 , x*30+25 ,width=2 ,outline="yellow",fill="yellow")

                    elif x == 19 and y == 19: #coin en bas a droite
                        c = c + futur[x-1][y]
                        c = c + futur[x][y-1]
                        c = c + futur[x-1][y-1]
                        if c ==3:
                                tab_grille[x][y] = 1
                                Zone.create_oval(y*30+100 , x*30 , y*30+100 +25 , x*30+25 ,width=2 ,outline="yellow",fill="yellow")

                    elif y == 0 and 0<x<19:#première ligne mais on enlève les coins
                        c = c + futur[x-1][y]
                        c = c + futur[x+1][y]
                        c = c + futur[x-1][y+1]
                        c = c + futur[x][y+1]
                        c = c + futur[x+1][y+1]
                        if c ==3:
                                tab_grille[x][y] = 1
                                Zone.create_oval(y*30+100 , x*30 , y*30+100 +25 , x*30+25 ,width=2 ,outline="yellow",fill="yellow")

                    elif y == 19 and 0<x<19:#dernière ligne mais on enlève les coins
                        c = c + futur[x-1][y-1]
                        c = c + futur[x][y-1]
                        c = c + futur[x+1][y-1]
                        c = c + futur[x-1][y]
                        c = c + futur[x+1][y]
                        if c ==3:
                                tab_grille[x][y] = 1
                                Zone.create_oval(y*30+100 , x*30 , y*30+100 +25 , x*30+25 ,width=2 ,outline="yellow",fill="yellow")

                    elif x == 0 and 0<y<19:#première colone mais on enlève les coins
                        c = c + futur[x][y-1]
                        c = c + futur[x+1][y-1]
                        c = c + futur[x+1][y]
                        c = c + futur[x+1][y]
                        c = c + futur[x+1][y+1]
                        if c ==3:
                                tab_grille[x][y] = 1
                                Zone.create_oval(y*30+100 , x*30 , y*30+100 +25 , x*30+25 ,width=2 ,outline="yellow",fill="yellow")

                    elif x == 19 and 0<y<19:#dernière colone mais on enlève les coins
                        c = c + futur[x][y-1]
                        c = c + futur[x-1][y-1]
                        c = c + futur[x-1][y]
                        c = c + futur[x][y+1]
                        c = c + futur[x-1][y+1]
                        if c ==3:
                                tab_grille[x][y] = 1
                                Zone.create_oval(y*30+100 , x*30 , y*30+100 +25 , x*30+25 ,width=2 ,outline="yellow",fill="yellow")

                    else:
                        c = c + futur[x-1][y-1]
                        c = c + futur[x][y-1]
                        c = c + futur[x+1][y-1]
                        c = c + futur[x-1][y]
                        c = c + futur[x+1][y]
                        c = c + futur[x-1][y+1]
                        c = c + futur[x][y+1]
                        c = c + futur[x+1][y+1]
                        if c ==3:
                                tab_grille[x][y] = 1
                                Zone.create_oval(y*30+100 , x*30 , y*30+100 +25 , x*30+25 ,width=2 ,outline="yellow",fill="yellow")





        cmpt_creature()


        if futur == tab_grille:
            dico = fin_partie()
            enregistrer(dico)
            message= showinfo("Jeu terminé", f"Fin du jeu, vous avez survécu {jour.get()} jours.\nVotre partie à été enregistré")
            fen.destroy()





def cmpt_creature():
    for x in range(20):
            for y in range(20):
                if tab_grille[x][y] == 1:
                    nb_creature.set(nb_creature.get()+1)

def dessiner_creature(li,col):
    Zone.create_oval(col*30+100 , li*30 , col*30+100 +25 , li*30+25 ,width=2 ,outline="yellow",fill="yellow")

def fin_partie():
    dico = []
    dico.append(jour.get())
    dico.append(nb_creature.get())
    dico.append(strftime('%Y-%m-%d %H:%M:%S'))

    return dico

def enregistrer(dico):
    if os.path.exists("jeu-de-la-vie.csv") == False:
        with open("jeu-de-la-vie.csv", "a") as f:
            f.write(f"Jour-survécu;nb-créature;date-heure\n")
            f.write(f"{dico[0]};{dico[1]};{dico[2]}\n")
    else:
        with open("jeu-de-la-vie.csv", "a") as f:
            f.write(f"{dico[0]};{dico[1]};{dico[2]}\n")
     


'''CONSTANTES'''
valide = False
jour = 0
futur = []
tab_grille = []
for i in range(20):
    tab_grille.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    futur.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])


"""PROGRAMME PRINCIPAL"""
# création de la fenêtre graphique
fen=Tk()
fen.geometry ("700x600") # dimensionnement de la fenêtre
fen.title ("Jeu de la vie")
# création d'un canvas
Zone=Canvas(fen,width=700,height=600,bg="grey")
Zone.place(x=0,y=0)

#appel de la fonction dessin grille
dessin_grille()
valider=Button(fen, text="valider",command=validation_du_jeu)
valider.place(x=0, y=60)

def affichage_jour():
    if valide == False:
        return
    else:
        jour.set(jour.get()+1)

jour= IntVar()
nb_creature= IntVar()
cmpt_jour = Label(fen, textvariable=jour )
cmpt_jour.grid(row=0, column=2)

aff_jour = Label(fen,text="Jour survécu :")
aff_jour.grid(row=0, column = 1)

suivant=Button(fen, text="jour suivant",command=lambda:[jour_suivant(),affichage_jour()])
suivant.place(x=0, y=200)




def quitter():
    showinfo(title="Vous avez quitté le jeu",message="Votre partie n'a pas été sauvegardé")
    fen.destroy()
Exit=Button(fen, text="Quitter",command=quitter)
Exit.place(x=0,y=500)





fen.bind('<Button-1>',coordonnees)



fen.mainloop()

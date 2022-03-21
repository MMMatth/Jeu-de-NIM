import pygame
from pygame.locals import *
import classGraphOriente as go
import classJoueur as joueur
import random

# lancement des modules inclus dans pygame
pygame.init() 
# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("comicsansms", 30)
# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Jeu de Nim") 
# chargement de l'image de fond
fond = pygame.image.load('../img/background.png')

# creation des joueurs
player1 = joueur.Joueur()
player2 = joueur.Joueur()

# creation du graphe de jeu pour l'intelligence artificielle
G = go.GraphOriente()
###à compléter Partie B : question 2)
##créer le graphe de tous les coups possibles sommets + arcs

#boutons cliquables joueur 1
zone1 = pygame.image.load("../img/b1.png") #image du bouton
zone1rect = pygame.Rect(10,10,30,30) #rectangle autour de l'image (10,10) coordonnées et (30,30) largeur et hauteur
zone2 = pygame.image.load("../img/b2.png")
zone2rect=pygame.Rect(10,50,30,30)
zone3 = pygame.image.load("../img/b3.png")
zone3rect = pygame.Rect(10,90,30,30)

#boutons cliquables joueur2
zone4rect = pygame.Rect(700,10,30,30)
zone5rect = pygame.Rect(700,50,30,30)
zone6rect = pygame.Rect(700,90,30,30)

#reponse question rejouer :
oui = pygame.image.load("../img/oui.png")
ouirect = pygame.Rect(10,450,50,50)

non = pygame.image.load("../img/non.png")
nonrect = pygame.Rect(70,450,50,50)


#allumettes
nbAllumettes = 12
allumette = pygame.image.load('../img/allumette.png')

running = True # variable de la boucle de jeu
#choix du joueur qui commence au hasard
n = random.randint(1,2)
if n == 1 :
    player1.joue = True
else :
    player2.joue = True
    
#variables de gestion de fin de partie
fin = False
augmente_score = False

###Boucle MENU : au choix : 2 joueurs humains ou 1 humain contre ordi en IA apprenante
menu = True
fondmenu = pygame.image.load("../img/menu.png")
humainVShumain = False
humainVSordi = True
while menu :
    screen.blit(fondmenu,(0,0))
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
            menu = False # menu est sur False
            running = False
              
       # gestion de la souris
        elif event.type == KEYDOWN: # quand j'appuie sur un bouton
            if event.key == pygame.K_1 or event.key == pygame.K_KP1: #choix touche 1 (même avec clavier numérique)
                humainVShumain = True
                menu = False
                player1.set_etat("humain")
                player2.set_etat("humain")
            if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                humainVSordi = True
                menu = False
                player1.set_etat("humain")
                player2.set_etat("ordi")
    pygame.display.update()
### BOUCLE DE JEU  ###
while running : # boucle infinie pour laisser la fenêtre ouverte
    if humainVShumain : 
        # dessin du fond
        screen.blit(fond,(0,0))
        if player1.joue == True:
            labelJ = myfont.render("joueur1 joue", 1, (255,0,0))
            screen.blit(labelJ, (320, 10))
        if player2.joue == True:
            labelJ2 = myfont.render("joueur2 joue", 1, (255,0,0))
            screen.blit(labelJ2, (320, 10))
        #affichage des allumettes :
        for i in range( nbAllumettes) :
            screen.blit(allumette,(300,i*35+100))

        ### Gestion des événements  ###
        for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
            if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
                running = False # running est sur False
                
           
           # gestion de la souris
            elif event.type == MOUSEBUTTONUP: # quand je relache le bouton
                if event.button == 1: # 1= clique gauche
                    if zone1rect.collidepoint(event.pos) and player1.joue == True:
                        print(1)
                        if nbAllumettes>=2 :nbAllumettes -=1
                        player1.joue = False
                        player2.joue = True
                    ###remettre ici votre Partie A : question 2)
                    if ouirect.collidepoint(event.pos) :
                        fin = False
                        n = random.randint(1,2)
                        if n == 1 :
                            player1.joue = True
                        else :
                            player2.joue = True
                        nbAllumettes = 12
                        player1.gagne = False
                        player2.gagne = False
                    if nonrect.collidepoint(event.pos) :
                        running = False
        screen.blit(zone1,(10,10))
        screen.blit(zone2,(10,50))
        screen.blit(zone3,(10,90))
        screen.blit(zone1,(700,10))
        screen.blit(zone2,(700,50))
        screen.blit(zone3,(700,90))

        if nbAllumettes == 1 and player1.joue == True :
            print('joueur2 gagne')
            fin = True
            player2.gagne = True
            # render text
            player2.joue = None
            player1.joue = None
            augmente_score = True
        if nbAllumettes == 1 and player2.joue == True :
            #remettre ici votre Partie A :question 3)
        if fin == True :
            if player1.gagne :
                label = myfont.render("Le gagnant est joueur1", 1, (255,255,0))
                if augmente_score == True :
                    player1.score+=1
                    augmente_score = False
                    
            else :
                #remettre ici votre Partie A :question 4)
                   
            question = myfont.render("Voulez-vous rejouer ?",1,(0,0,0))
            score = myfont.render("joueur 1 a "+str(player1.score)+" points et le joueur 2 a "+str(player2.score)+"points",1,(0,0,0))
            screen.blit(label, (200, 10))
            screen.blit(question,(10,400))
            screen.blit(oui,(10,450))
            screen.blit(non,(70,450))
            screen.blit(score,(10,500))
    if humainVSordi :
            # dessin du fond
            screen.blit(fond,(0,0))
            if player1.joue == True:
                labelJ = myfont.render("joueur1 joue", 1, (255,0,0))
                screen.blit(labelJ, (320, 10))
            if player2.joue == True:
                labelJ2 = myfont.render("joueur2 joue", 1, (255,0,0))
                screen.blit(labelJ2, (320, 10))
            #affichage des allumettes :
            for i in range( nbAllumettes) :
                screen.blit(allumette,(300,i*35+100))

            ### Gestion des événements  ###
            for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
                if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
                    running = False # running est sur False
                    
               
               # gestion de la souris
                elif event.type == MOUSEBUTTONUP: # quand je relache le bouton
                    if event.button == 1: # 1= clique gauche
                        if zone1rect.collidepoint(event.pos) and player1.joue == True:
                            print(1)
                            if nbAllumettes>=2 :nbAllumettes -=1
                            player1.joue = False
                            player2.joue = True
                        if zone2rect.collidepoint(event.pos) and player1.joue == True :
                            print(2)
                            if nbAllumettes>=3 :nbAllumettes -=2
                            player1.joue = False
                            player2.joue = True
                        if zone3rect.collidepoint(event.pos) and player1.joue == True :
                            print(3)
                            if nbAllumettes>=4 :nbAllumettes -=3
                            player1.joue = False
                            player2.joue = True
                        #il n'y a plus que les trois boutons du joueur humain
                        if ouirect.collidepoint(event.pos) :
                            fin = False
                            n = random.randint(1,2)
                            if n == 1 :
                                player1.joue = True
                            else :
                                player2.joue = True
                            nbAllumettes = 12
                            player1.gagne = False
                            player2.gagne = False
                        if nonrect.collidepoint(event.pos) :
                            running = False
            #on affiche que les trois boutons de l'humain
            screen.blit(zone1,(10,10))
            screen.blit(zone2,(10,50))
            screen.blit(zone3,(10,90))
            #l'ordi choisi son coup :
            if player2.joue == True and nbAllumettes >1 :
                #à compléter Partie B question 3) le player2 ordi doit choisir son coups grâce au graphe G des coups
                #il doit choisir au hasard parmi la liste des arcs issus du sommet correspondant au nb d'allumettes
                pass
                # à compléter partie C question 2) : gérer si la liste de coups issus du nbd'allumettes présente est vide (gobelet vide dans vidéo)

            if nbAllumettes == 1 and player1.joue == True :
                print('joueur2 gagne')
                fin = True
                player2.gagne = True
                player2.joue = None
                player1.joue = None
                augmente_score = True
            if nbAllumettes == 1 and player2.joue == True :
                print('joueur1 gagne')
                fin = True
                player1.gagne = True
                player2.joue = None
                player1.joue = None
                augmente_score = True
                #Partie C : question 1) Si le joueur humain gagne , l'ordi supprime son dernier coups pour ne plus le refaire
                
            if fin == True :
                if player1.gagne :
                    label = myfont.render("Le gagnant est joueur1", 1, (255,255,0))
                    if augmente_score == True :
                        player1.score+=1
                        augmente_score = False
                        
                else :
                    label = myfont.render("Le gagnant est joueur2", 1, (255,255,0))
                    if augmente_score == True :
                        player2.score+=1
                        augmente_score = False
                       
                question = myfont.render("Voulez-vous rejouer ?",1,(0,0,0))
                score = myfont.render("joueur 1 a "+str(player1.score)+" points et le joueur 2 a "+str(player2.score)+"points",1,(0,0,0))
                screen.blit(label, (200, 10))
                screen.blit(question,(10,400))
                screen.blit(oui,(10,450))
                screen.blit(non,(70,450))
                screen.blit(score,(10,500))
    pygame.display.update() # pour ajouter tout changement à l'écran
pygame.quit()

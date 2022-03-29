from re import I
import pygame
from pygame.locals import *
import classGraphOriente as graphe_oriente
import classJoueur as joueur
import random
import classpg as pg
import menu
import time 

def changer_tour(cond):
    global player1, player2
    if cond:
        
        player1.joue = False
        player2.joue = True
    else:
        player1.joue = True
        player2.joue = False
        
def main():
    global player1, player2
    pygame.init() 

    screen = pygame.display.set_mode((1168,826))

    pygame.display.set_caption("Jeu de Nim") 

    fond = pygame.image.load('../img/background.png')

    player1 , player2= joueur.Joueur(), joueur.Joueur()

    icon = pygame.image.load("../img/icon.png")
        
    pygame.display.set_icon(icon)

    clic = pg.son("../song/clic.mp3","song")

    # creation du graphe de jeu pour l'intelligence artificielle
    G = graphe_oriente.GraphOriente()
    ###à compléter Partie B : question 2)
    for i in range(1,13):
        G.ajouter_sommet(i)
        if i>3 :
            G.ajouter_arc(i,i-1)
            G.ajouter_arc(i,i-2)
            G.ajouter_arc(i,i-3)
    G.ajouter_arc(3,2)
    G.ajouter_arc(3,1)
    G.ajouter_arc(2,1)

    #ajouter les arcs

    ##créer le graphe de tous les coups possibles sommets + arcs

    boutons_gauches={
        "b1" : pg.bouton("../img/b1.png",107,260,147,147),
        "b2" : pg.bouton("../img/b2.png",107,445,147,147),
        "b3" : pg.bouton("../img/b3.png",107,630,147,147),
    }

    bouton = {
        "oui" : pg.bouton("../img/oui.png",435,560,147,147),
        "non" : pg.bouton("../img/non.png",735,560,147,147)
    }


    nbr_sticks = 12

    running = True # variable de la boucle de jeu
    #choix du joueur qui commence au hasard
    if random.randint(1,2) == 1 : 
        player1.joue = True
    else : 
        player2.joue = True
        
    #variables de gestion de fin de partie
    fin , augmente_score = False , False


    ###Boucle MENU : au choix : 2 joueurs humains ou 1 humain contre ordi en IA apprenante

    ### BOUCLE DE JEU  ###
    while running : # boucle infinie pour laisser la fenêtre ouverte
            # dessin du fond
            screen.blit(fond,(0,0))
            if player1.joue == True:
                pg.text("Joueur 1 ",590, 70,"center",size = 100, color= "white").iblit(screen)
                
            if player2.joue == True:
                pg.text("Joueur 2",590, 70,"center",size = 100, color= "white").iblit(screen)
                
            
            #affichage des allumettes :
            if not fin:
                for i in range(nbr_sticks) :
                    pg.img('../img/allumette.png',584,i*40+228 ,460,35).iblit(screen)
                    
                for i in boutons_gauches: # on blit les bouton de gauche
                    boutons_gauches[i].iblit(screen)
                    boutons_gauches[i].hover_big(pygame.mouse.get_pos(),10)
                
            ### Gestion des événements  ###
            for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
                if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
                    running = False # running est sur False
                    
            
            # gestion de la souris
                elif player1.joue == True:
                    for i in boutons_gauches:
                        if boutons_gauches[i].click(pygame.mouse.get_pos(),event):
                            clic.play()
                            cpt = int(i.replace("b",""))
                            if nbr_sticks>=cpt+1 :
                                nbr_sticks -= cpt
                                changer_tour(True)
                elif bouton["oui"].click(pygame.mouse.get_pos(),event):
                    clic.play()
                    fin = False
                    if random.randint(1,2) == 1 :
                            
                        player1.joue = True
                    else : 
                        player2.joue = True
                        
                    nbr_sticks = 12
                    
                    player1.gagne ,player2.gagne = False, False
                    
                    fond = pygame.image.load('../img/background.png')
                    
                elif bouton["non"].click(pygame.mouse.get_pos(),event):
                    clic.play()
                    menu.main()
                    
            #l'ordi choisi son coup :
            if player2.joue == True and nbr_sticks >1 :
                #à compléter Partie B question 3) le player2 ordi doit choisir son coups grâce au graphe G des coups
                #il doit choisir au hasard parmi la liste des arcs issus du sommet correspondant au nb d'allumettes
                liste_voisins = G.liste_sommets_issus(nbr_sticks)
                tmp1 = nbr_sticks
                nbr_sticks = random.choice(liste_voisins)
                tmp2 = nbr_sticks
                player2.joue=False
                player1.joue = True
                dernier_coup = None
                
                
                # à compléter partie C question 2) : gérer si la liste de coups issus du nbd'allumettes présente est vide (gobelet vide dans vidéo)
                
            if nbr_sticks == 1 and player1.joue == True :
                print('joueur2 gagne')
                fin = True
                player2.gagne = True
                player2.joue = None
                player1.joue = None
                augmente_score = True
            if nbr_sticks == 1 and player2.joue == True :
                print('joueur1 gagne')
                fin = True
                player1.gagne = True
                player2.joue = None
                player1.joue = None
                augmente_score = True
                
                #Partie C : question 1) Si le joueur humain gagne , l'ordi supprime son dernier coups pour ne plus le refaire
            if player1.gagne:
                G.supprimer_arc(tmp1,tmp2)
                print(G,tmp1,tmp2)
            #affichage du gagnant et du score
            if fin == True : #Si fin de partie
                fond = pygame.image.load('../img/background_end.png')
                if player1.gagne :
                    pg.img("../img/crown.png",130,160,93,77).iblit(screen)
                    print(G)
                    if augmente_score == True :
                        player1.score+=1
                        augmente_score = False #permet de n'augmenter le score qu'une seule fois
                else :
                    pg.img("../img/crown.png",1035,160,93,77).iblit(screen)
                    if augmente_score == True :
                        player2.score+=1
                        augmente_score = False #permet de n'augmenter le score qu'une seule fois
                #gérer la possibilité de rejouer       
                pg.text(str(player1.score),130, 440,"center", color = "white", size = 100).iblit(screen)
                pg.text(str(player2.score),1035, 440,"center", color = "white", size = 100).iblit(screen)
                bouton["oui"].iblit(screen)
                bouton["oui"].hover_big(pygame.mouse.get_pos(),10)
                
                bouton["non"].iblit(screen)
                bouton["non"].hover_big(pygame.mouse.get_pos(),10)
            pygame.display.update() # pour ajouter tout changement à l'écran
pygame.quit()
if __name__ == "__main__":
    main()
from re import I
import pygame
from pygame.locals import *
import classGraphOriente
import classJoueur as joueur
import random
import classpg as pg

        
def changer_tour(cond):
    global player1, player2
    if cond:
        player1.joue = False
        player2.joue = True
    else:
        player1.joue = True
        player2.joue = False
        
def restart():
    global player1, player2,fin,nbr_sticks       
    fin = False
    if random.randint(1,2) == 1 : player1.joue = True
    else : player2.joue = True
    nbr_sticks = 12
    player1.gagne = False
    player2.gagne = False

def humain():
    pygame.init() 

    screen = pygame.display.set_mode((1168,826))

    pygame.display.set_caption("Jeu de Nim") 

    fond = pygame.image.load('../img/background.png')

    player1 , player2= joueur.Joueur(), joueur.Joueur()

    icon = pygame.image.load("../img/icon.png")
        
    pygame.display.set_icon(icon)



    boutons_gauches={
        "b1" : pg.bouton("../img/b1.png",107,260,147,147),
        "b2" : pg.bouton("../img/b2.png",107,445,147,147),
        "b3" : pg.bouton("../img/b3.png",107,630,147,147),
    }

    boutons_droits={
        "b1" : pg.bouton("../img/b1.png",1061,260,147,147),
        "b2" : pg.bouton("../img/b2.png",1061,445,147,147),
        "b3" : pg.bouton("../img/b3.png",1061,630,147,147),
    }

    bouton = {
        "oui" : pg.bouton("../img/oui.png",10,450,50,50),
        "non" : pg.bouton("../img/non.png",70,450,50,50)
    }



    nbr_sticks = 12

    running = True # variable de la boucle de jeu

    if random.randint(1,2) == 1 : 
        
        player1.joue = True
        
    else : 
        
        player2.joue = True
        
        
    fin , augmente_score = False , False

    humainVShumain = True



    ### BOUCLE DE JEU  ###
    while running : # boucle infinie pour laisser la fenêtre ouverte
        if humainVShumain : 
            
            screen.blit(fond,(0,0))
            
            if player1.joue == True:
                pg.text("Joueur 1 ",586, 77,"center",size = 100, color= "white").iblit(screen)
                
            if player2.joue == True:
                pg.text("Joueur 2",586, 77,"center",size = 100, color= "white").iblit(screen)
                
            #affichage des allumettes :
            for i in range(nbr_sticks) :
                pg.img('../img/allumette.png',584,i*40+228 ,460,35).iblit(screen)
            for i in boutons_gauches: # on blit les bouton de gauche
                boutons_gauches[i].iblit(screen)
                boutons_gauches[i].hover_big(pygame.mouse.get_pos(),10)
            for i in boutons_droits:
                boutons_droits[i].iblit(screen)
                boutons_droits[i].hover_big(pygame.mouse.get_pos(),10)
                
            
                    
            for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
                
                if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
                    running = False # running est sur False
                    
                elif player1.joue == True:
                    for i in boutons_gauches:
                        if boutons_gauches[i].click(pygame.mouse.get_pos(),event):
                            cpt = int(i.replace("b",""))
                            if nbr_sticks>=cpt+1 :
                                nbr_sticks -= cpt
                                changer_tour(True)
                    
                elif player2.joue == True:
                    for i in boutons_droits:
                        if boutons_droits[i].click(pygame.mouse.get_pos(),event):
                            cpt = int(i.replace("b",""))
                            if nbr_sticks>=cpt+1 :
                                nbr_sticks -= cpt
                                changer_tour(False)
                
                elif bouton["oui"].click(pygame.mouse.get_pos(),event):
                    restart()
                    
                elif bouton["non"].click(pygame.mouse.get_pos(),event):
                    running = False

            
                    
            #gestion de la fin de partie quand il rest une seule allumette
            if nbr_sticks == 1 and player1.joue == True :
                #c'est au joueur 1 de jouer et il reste une seule allumette
                #donc il a perdu
                fin = True
                player2.gagne = True
                player2.joue = None
                player1.joue = None
                augmente_score = True # permet de dire qu'il faut augmenter le score
                
            if nbr_sticks == 1 and player2.joue == True :
                ####à compléter question 3)###
                fin = True
                player1.gagne = True
                player2.joue = None
                player1.joue = None
                augmente_score = True # permet de dire qu'il faut augmenter le score
            

            #affichage du gagnant et du score
            if fin == True : #Si fin de partie
                if player1.gagne :
                    pg.text("Le gagnant est le joueur n°1",400, 25,"center", color = "black").iblit(screen)
                    if augmente_score == True :
                        player1.score+=1
                        augmente_score = False #permet de n'augmenter le score qu'une seule fois
                else :
                    pg.text("Le gagnant est le joueur n°2",400, 25,"center", color = "black").iblit(screen)
                    if augmente_score == True :
                        player2.score+=1
                        augmente_score = False #permet de n'augmenter le score qu'une seule fois
                #gérer la possibilité de rejouer       
                pg.text("Voulez vous rejouer ?",400, 75,"center", color = "black").iblit(screen)
                pg.text("joueur 1 a "+str(player1.score)+" points et le joueur 2 a "+str(player2.score)+"points",400, 125,"center", color = "black").iblit(screen)
                bouton["oui"].iblit(screen)
                bouton["non"].iblit(screen)
                
        
        pygame.display.update() # mise à jour pour ajouter tout changement à l'écran
    pygame.quit()

def menu():
    pygame.init() 

    screen = pygame.display.set_mode((1168,826))

    pygame.display.set_caption("Jeu de Nim") 

    fond = pygame.image.load('../img/menu_bg.png')

    icon = pygame.image.load("../img/icon.png")
        
    pygame.display.set_icon(icon)
    
    boutons={
        "b1" : pg.bouton("../img/menu_b1.png",585,415,510,145),
        "b2" : pg.bouton("../img/menu_b2.png",585,600,510,145),
    }


    running = True # variable de la boucle de jeu

    ### BOUCLE DE JEU  ###
    while running : # boucle infinie pour laisser la fenêtre ouverte
            screen.blit(fond,(0,0))
            for i in boutons: # on blit les bouton de gauche
                boutons[i].iblit(screen)
                
            for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
                if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
                    running = False # running est sur False
                if boutons["b1"].click(pygame.mouse.get_pos(),event):
                    running = False
                    humain()
                if boutons["b2"].click(pygame.mouse.get_pos(),event):
                    print("1vIA")
                
        
            pygame.display.update() # mise à jour pour ajouter tout changement à l'écran
    pygame.quit()
    
    
if __name__ == "__main__":
    menu()
    
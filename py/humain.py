from re import I
import pygame
from pygame.locals import *
import classGraphOriente
import classJoueur as joueur
import random
import classpg as pg
import menu
import pygame_widgets
from pygame_widgets.button import Button
from functools import partial
        




def main():
    global clic, nbr_sticks,player1, player2
    
    def bouton(nbr,player):
        global clic, nbr_sticks,player1, player2
        if player1.joue == True and player == "p1":
            clic.play()
            if nbr_sticks>= nbr:
                nbr_sticks -= nbr
                player1.joue = False
                player2.joue = True
        elif player2.joue == True and player == "p2":
            clic.play()
            if nbr_sticks>= nbr:
                nbr_sticks -= nbr
                player1.joue = True
                player2.joue = False  
        print(nbr_sticks,nbr,player1.joue)
    pygame.init() 

    screen = pygame.display.set_mode((1168,826))

    pygame.display.set_caption("Jeu de Nim") 

    fond = pygame.image.load('../img/background.png')

    player1 , player2= joueur.Joueur(), joueur.Joueur()

    icon = pygame.image.load("../img/icon.png")
        
    pygame.display.set_icon(icon)

    clic = pg.son("../song/clic.mp3","song")
    
    buttons = {"bouton_gauche_1" : Button(screen,34,187,147,147, text='1', textVAlign = "bottom", margin = 10,textColour = (239,239,239), inactiveColour=(233,196,106), hoverColour=(226, 150, 90),  pressedColour=(0, 200, 20), radius=10, onClick = partial(bouton,1,"p1") ,  font = pygame.font.Font("../font/font.otf",110))
            ,"bouton_gauche_2" : Button(screen,34,372,147,147, text='2', textVAlign = "bottom", margin = 10,textColour = (239,239,239), inactiveColour=(233,196,106), hoverColour=(226, 150, 90),  pressedColour=(0, 200, 20), radius=10, onClick = partial(bouton,2,"p1") ,  font = pygame.font.Font("../font/font.otf",110))
            ,"bouton_gauche_3" : Button(screen,34,557,147,147, text='3', textVAlign = "bottom", margin = 10,textColour = (239,239,239), inactiveColour=(233,196,106), hoverColour=(226, 150, 90),  pressedColour=(0, 200, 20), radius=10, onClick = partial(bouton,3,"p1") ,  font = pygame.font.Font("../font/font.otf",110))
            
            ,"bouton_droite_1" : Button(screen,988,187,147,147, text='1', textVAlign = "bottom", margin = 10,textColour = (239,239,239), inactiveColour=(233,196,106), hoverColour=(226, 150, 90),  pressedColour=(0, 200, 20), radius=10, onClick = partial(bouton,1,"p2") ,  font = pygame.font.Font("../font/font.otf",110))
            ,"bouton_droite_2" : Button(screen,988,372,147,147, text='2', textVAlign = "bottom", margin = 10,textColour = (239,239,239), inactiveColour=(233,196,106), hoverColour=(226, 150, 90),  pressedColour=(0, 200, 20), radius=10, onClick = partial(bouton,2,"p2") ,  font = pygame.font.Font("../font/font.otf",110))
            ,"bouton_droite_3" : Button(screen,988,557,147,147, text='3', textVAlign = "bottom", margin = 10,textColour = (239,239,239), inactiveColour=(233,196,106), hoverColour=(226, 150, 90),  pressedColour=(0, 200, 20), radius=10, onClick = partial(bouton,3,"p2") ,  font = pygame.font.Font("../font/font.otf",110))
            
            # ,"oui" : Button(screen,107,630,147,147, text='3', textVAlign = "bottom", margin = 10,textColour = (239,239,239), inactiveColour=(233,196,106), hoverColour=(226, 150, 90),  pressedColour=(0, 200, 20), radius=10, onClick = partial(bouton,3,"p2") ,  font = pygame.font.Font("../font/font.otf",110))
            # ,"non" : Button(screen,107,445,147,147, text='2', textVAlign = "bottom", margin = 10,textColour = (239,239,239), inactiveColour=(233,196,106), hoverColour=(226, 150, 90),  pressedColour=(0, 200, 20), radius=10, onClick = partial(bouton,2,"p2") ,  font = pygame.font.Font("../font/font.otf",110))
            
 
               }

    bouton = {
        "oui" : pg.bouton("../img/oui.png",435,560,147,147),
        "non" : pg.bouton("../img/non.png",735,560,147,147)
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
            events = pygame.event.get()
            screen.blit(fond,(0,0))
            
            if player1.joue == True:
                pg.text("Joueur 1 ",590, 70,"center",size = 100, color= "white").iblit(screen)
                
            if player2.joue == True:
                pg.text("Joueur 2",590, 70,"center",size = 100, color= "white").iblit(screen)
                
            #affichage des allumettes :
            if not fin:
                for i in range(nbr_sticks) :
                    pg.img('../img/allumette.png',584,i*40+228 ,460,35).iblit(screen)
                pygame_widgets.update(events)
                
            
                    
            for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
                
                if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
                    running = False # running est sur False

                
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
                    humainVShumain = False
                    running = False
                    menu.main()
                    

            
                    
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
                fond = pygame.image.load('../img/background_end.png')
                if player1.gagne :
                    pg.img("../img/crown.png",130,160,93,77).iblit(screen)
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
            
        pygame.display.update() # mise à jour pour ajouter tout changement à l'écran
    pygame.quit()
    
    
if __name__ == "__main__":
    main()
    
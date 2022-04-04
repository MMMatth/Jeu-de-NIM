from re import I
import pygame
from pygame.locals import *
import classpg as pg
import game

def main():
    pygame.init() 

    screen = pygame.display.set_mode((1168,826))

    pygame.display.set_caption("Jeu de Nim") 

    fond = pygame.image.load('../img/menu_bg.png')

    icon = pygame.image.load("../img/icon.png")
        
    pygame.display.set_icon(icon)
    
    clic = pg.son("../song/clic.mp3","song")
    
    boutons={"b1" : pg.bouton("../img/menu_b1.png",585,415,510,145),"b2" : pg.bouton("../img/menu_b2.png",585,600,510,145),}
    
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
                    clic.play()
                    running = False
                    game.main("human","")
                if boutons["b2"].click(pygame.mouse.get_pos(),event):
                    clic.play()
                    running = False
                    choix()
                
        
            pygame.display.update() # mise à jour pour ajouter tout changement à l'écran
    pygame.quit()

def choix():
    pygame.init() 

    screen = pygame.display.set_mode((1168,826))

    pygame.display.set_caption("Jeu de Nim") 

    fond = pygame.image.load('../img/choice.png')

    icon = pygame.image.load("../img/icon.png")
        
    pygame.display.set_icon(icon)
    
    clic = pg.son("../song/clic.mp3","song")
    
    boutons={
        "1" : pg.bouton("../img/choice_b1.png",380,415,400,180),
        "2" : pg.bouton("../img/choice_b2.png",790,415,400,180),
        "3" : pg.bouton("../img/choice_b3.png",380,600,400,180),
        "4" : pg.bouton("../img/choice_b4.png",790,600,400,180)
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
                if boutons["1"].click(pygame.mouse.get_pos(),event):
                    clic.play()
                    running = False
                    game.main("bot","hard")
                if boutons["2"].click(pygame.mouse.get_pos(),event):
                    clic.play()
                    running = False
                    game.main("bot","meduim")
                if boutons["3"].click(pygame.mouse.get_pos(),event):
                    clic.play()
                    running = False
                    game.main("bot","easy")
                if boutons["4"].click(pygame.mouse.get_pos(),event):
                    clic.play()
                    running = False
                    game.main("bot","save")
                
        
            pygame.display.update() # mise à jour pour ajouter tout changement à l'écran
    pygame.quit()
if __name__ == "__main__": 
    main()
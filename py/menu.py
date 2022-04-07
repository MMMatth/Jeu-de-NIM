from re import I
import pygame
from pygame.locals import *
import classpg as pg
import game as g



class menu:
    def __init__(self,choice) -> None:
        pygame.init() 

        self.screen = pygame.display.set_mode((1168,826))

        pygame.display.set_caption("Jeu de Nim") 

        self.fond = pygame.image.load('../img/menu_bg.png')

        self.icon = pygame.image.load("../img/icon.png")
        
        self.choice = choice    
        
        pygame.display.set_icon(self.icon)
        
        self.clic = pg.son("../song/clic.mp3","song")
        if self.choice == "menu":
            self.button= {"1" : pg.bouton("../img/menu_b1.png",585,415,510,145),"2" : pg.bouton("../img/menu_b2.png",585,600,510,145),}
        else:
            self.button =  {
            "1" : pg.bouton("../img/choice_b1.png",380,415,400,180),
            "2" : pg.bouton("../img/choice_b2.png",790,415,400,180),
            "3" : pg.bouton("../img/choice_b3.png",380,600,400,180),
            "4" : pg.bouton("../img/choice_b4.png",790,600,400,180)
        }
        
        self.running = True
    
    def iblitall(self):
        self.screen.blit(self.fond,(0,0))
        for i in self.button:
            self.button[i].iblit(self.screen)
            self.grow(self.button[i])
            
    def grow(self,bouton):
        if bouton.rect.collidepoint(pygame.mouse.get_pos()) : 
            bouton.grow()
        if not bouton.rect.collidepoint(pygame.mouse.get_pos()) : 
            bouton.ungrow()
    
    def button_f(self,event):
        if self.choice == "menu":
            if self.button["1"].click(pygame.mouse.get_pos(),event):
                self.clic.play()
                self.running = False
                g.main("human","")
                
            if self.button["2"].click(pygame.mouse.get_pos(),event):
                self.clic.play()
                self.button =  {
                    "1" : pg.bouton("../img/choice_b1.png",380,415,400,180),
                    "2" : pg.bouton("../img/choice_b2.png",790,415,400,180),
                    "3" : pg.bouton("../img/choice_b3.png",380,600,400,180),
                    "4" : pg.bouton("../img/choice_b4.png",790,600,400,180)
                }
                self.choice = "choice"
                
                
        else: 
            if self.button["1"].click(pygame.mouse.get_pos(),event):
                self.clic.play()
                self.running = False
                g.main("bot","hard")
                
            if self.button["2"].click(pygame.mouse.get_pos(),event):
                self.clic.play()
                self.running = False
                g.main("bot","meduim")
                
            if self.button["3"].click(pygame.mouse.get_pos(),event):
                self.clic.play()
                self.running = False
                g.main("bot","easy")
                
            if self.button["4"].click(pygame.mouse.get_pos(),event):
                self.clic.play()
                self.running = False
                g.main("bot","save")

def main():
    pygame.init() 

    window = menu("menu")
    ### BOUCLE DE JEU  ###
    while window.running : # boucle infinie pour laisser la fenêtre ouverte
        window.iblitall()
        
        for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
            
            if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
                window.running = False # running est sur False
                
            window.button_f(event)

                
        
        
            pygame.display.update() # mise à jour pour ajouter tout changement à l'écran
    pygame.quit()

if __name__ == "__main__":
    main()
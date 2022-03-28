from re import I
import pygame
from pygame.locals import *
import classpg as pg
import humain
import pygame_widgets
from pygame_widgets.button import Button

def b1():
    global clic, run
    clic.play()
    run = False
    humain.main()
def b2():
    global clic, run
    clic.play()
    print("1vIA")

def main():
    global clic, run
    pygame.init() 

    screen = pygame.display.set_mode((1168,826))

    pygame.display.set_caption("Jeu de Nim") 

    fond = pygame.image.load('../img/menu_bg.png')

    icon = pygame.image.load("../img/icon.png")
        
    pygame.display.set_icon(icon)
    
    clic = pg.son("../song/clic.mp3","song")
    
    button = {"1": Button(
    # Mandatory Parameters
    screen,  # Surface to place button on
    329,  # X-coordinate of top left corner
    350,  # Y-coordinate of top left corner
    509,  # Width
    148,  # Height

    # Optional Parameters
    text='1v1',  # Text to display
    textVAlign = "bottom",
    margin = 10,
    textColour = (239,239,239),
    inactiveColour=(244, 162, 97),  # Colour of button when not being interacted with
    hoverColour=(226, 150, 90),  # Colour of button when being hovered over
    pressedColour=(0, 200, 20),  # Colour of button when being clicked
    radius=10,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: b1(),  # Function to call when clicked on
    font = pygame.font.Font("../font/font.otf",110)
    )
              
            ,"2" : Button(screen, 329, 545, 509, 148, text='1vIA', textVAlign = "bottom", margin = 10,textColour = (239,239,239), inactiveColour=(233,196,106), hoverColour=(226, 150, 90),  pressedColour=(0, 200, 20), radius=10, onClick=lambda: b2(),  font = pygame.font.Font("../font/font.otf",110))
    }


    run = True # variable de la boucle de jeu

    ### BOUCLE DE JEU  ###
    while run : # boucle infinie pour laisser la fenêtre ouverte
            screen.blit(fond,(0,0))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                    quit()
            if run:
                pygame_widgets.update(events)        
            pygame.display.update() # mise à jour pour ajouter tout changement à l'écran
    pygame.quit()
    
if __name__ == "__main__": 
    main()
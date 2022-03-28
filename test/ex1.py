import pygame

import pygame_widgets
from pygame_widgets.button import Button

# Set up Pygame
pygame.init()
win = pygame.display.set_mode((600, 600))

# Creates the button with optional parameters
button = {"1": Button(
    # Mandatory Parameters
    win,  # Surface to place button on
    50,  # X-coordinate of top left corner
    50,  # Y-coordinate of top left corner
    509,  # Width
    148,  # Height

    # Optional Parameters
    text='1v1',  # Text to display
    textColour = (239,239,239),
    margin=10,  # Minimum distance between text/image and edge of button
    inactiveColour=(244, 162, 97),  # Colour of button when not being interacted with
    hoverColour=(226, 150, 90),  # Colour of button when being hovered over
    pressedColour=(0, 200, 20),  # Colour of button when being clicked
    radius=10,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: print('Click'),  # Function to call when clicked on
    font = pygame.font.Font("../font/font.otf",100)
)
          ,"2" : Button(
    # Mandatory Parameters
    win,  # Surface to place button on
    50,  # X-coordinate of top left corner
    100,  # Y-coordinate of top left corner
    509,  # Width
    148,  # Height

    # Optional Parameters
    text='1v1',  # Text to display
    textColour = (239,239,239),
    margin=10,  # Minimum distance between text/image and edge of button
    inactiveColour=(244, 162, 97),  # Colour of button when not being interacted with
    hoverColour=(226, 150, 90),  # Colour of button when being hovered over
    pressedColour=(0, 200, 20),  # Colour of button when being clicked
    radius=10,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: print('Click'),  # Function to call when clicked on
    font = pygame.font.Font("../font/font.otf",100)
)
}

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    win.fill((255, 255, 255))

    pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
    pygame.display.update()
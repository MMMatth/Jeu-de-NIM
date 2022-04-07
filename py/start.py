import menu
import pygame

class music:
    def __init__(self):
        self.song = "../song/music.wav"
        self.song = pygame.mixer.music.load(self.song)
        self.song = pygame.mixer.music.set_volume(0.5)
        
    def play(self):
        self.music = pygame.mixer.music.play(-1)

    def stop(self):
        self.music = pygame.mixer.music.stop()
        
if __name__ == '__main__':
    pygame.init()
    music().play()
    menu.main()
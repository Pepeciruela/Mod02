import pygame, sys

class Game():
    runners = []
    __startLine = 20
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))
        self.__background = pygame.image.load("images/background.png")
        
    
    
    
if __name__ == "__main__":
    game = Game()
    
# NEXT STAGE -> establish structure chart for all functions in Game object to reoganize thoughts

import pygame
from game import Game

#Main game loop
if __name__ == '__main__':
    pygame.init
    Clock = pygame.time.Clock()
    GameActive = True
    ThisGame = Game()

    #Display
    pygame.display.set_caption("Overflow")
    ScreenWidth = 1300
    ScreenHeight = 900
    Screen = pygame.display.set_mode((ScreenWidth,ScreenHeight))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if GameActive:
            Screen.fill('White')
            ThisGame.run()

        pygame.display.update()
        Clock.tick(60)
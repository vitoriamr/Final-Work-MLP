import pygame
from pygame.locals import *
import localdefs
import os, sys

def main(screen,clock):

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    stillRunning = 1
    clock = pygame.time.Clock()
    
    while stillRunning:
        clock.tick(30)
        screen.blit(background,(0,0))

        # all inputs events
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            else:
                keyPressed = pygame.key.get_pressed()
                if keyPressed[K_ESCAPE]:
                    sys.exit()
               # TO DO: 
               # elif keyPressed

        pygame.display.flip()
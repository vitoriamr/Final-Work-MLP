import pygame
from pygame.locals import *
import localdefs
import os, sys

def main():
    pygame.init()
    print "Game initialized."
    pygame.display.set_caption("Tower Defence")
    pygame.mouse.set_visible(1)
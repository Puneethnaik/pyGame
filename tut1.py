import pygame
from pygame.locals import *
screen = pygame.display.set_mode([1024, 728], FULLSCREEN)
#car = pygame.image.load("/home/puneeth/Desktop/googledp.jpg")
#screen.blit(car, (50, 100))
pygame.display.flip()
running = True # this indicates the state of the program
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # this means the user has pressed the close button on the window and the window has to close!!!

import pygame,os
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((750,750))

background = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Flappy Bird Images\\bg(1).png")
background = pygame.transform.scale(background,(750,750))

bird = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Flappy Bird Images\\bird(1).png")
bird = pygame.transform.scale(bird,(750,750))


while 1:

    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
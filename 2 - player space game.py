import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((750,750))

up = False
down = False
left = False
right = False

#BG setup
background = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\space_bg.jpeg")
background = pygame.transform.scale(background,(750,750))

player_1 = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\spaceship.png")
player_1 = pygame.transform.scale(player_1,(75,75))
player_1 = pygame.transform.rotate(player_1,270)

player_1_X = 20
player_1_Y = 375

player_2 = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\spaceship.png")
player_2 = pygame.transform.scale(player_2,(75,75))
player_2 = pygame.transform.rotate(player_2,90)

player_2_X = 650
player_2_Y = 375

while 1:

    #drawing
    screen.blit(background,(0,0))

    screen.blit(player_1,(player_1_X,player_1_Y))
    screen.blit(player_2,(player_2_X,player_2_Y))

    pygame.draw.rect(screen, (255, 255, 255), (360,0,40,750))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == K_w:
                up = True
            if event.key == K_a:
                left = True
            if event.key == K_s:
                down = True
            if event.key == K_d:
                right = True
            
        elif event.type == pygame.KEYUP:
            if event.key == K_w:
                up = False
            if event.key == K_a:
                left = False
            if event.key == K_s:
                down = False
            if event.key == K_d:
                right = False

    if up:
        player_1_Y -= 1
    if down:
        player_1_Y += 1
    if left:
        player_1_X -= 1
    if right:
        player_1_X += 1

    if player_1_X >= 285:
        player_1_X = 285
        
    pygame.display.update()
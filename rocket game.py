import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((750,750))

#BG setup
background = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\space_bg.jpeg")
background = pygame.transform.scale(background,(750,750))

#rocket setup
rocket = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\rocket.png")
rocket = pygame.transform.scale(rocket,(125,175))
rocket_x = 325
rocket_y = 325

pressed_up = False
pressed_right = False
pressed_left = False

#Main Loop
while 1:

    #drawing
    screen.blit(background,(0,0))
    screen.blit(rocket,(rocket_x,rocket_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        #movement
        elif event.type == pygame.KEYDOWN:
            if event.key == K_w:
                pressed_up = True
            if event.key == K_d:
                pressed_right = True
            if event.key == K_a:
                pressed_left = True
        elif event.type == pygame.KEYUP:
                if event.key == K_w:
                    pressed_up = False
                if event.key == K_d:
                    pressed_right = False
                if event.key == K_a:
                    pressed_left = False

    if pressed_up:
        rocket_y -= 2
        pygame.display.update()
    if pressed_right:
        rocket_x += 1
        pygame.display.update()
    if pressed_left:
        rocket_x -= 1
        pygame.display.update()

    #gravity
    rocket_y += 1
    if rocket_y >= 750 or rocket_y <= -175 or rocket_x >= 750 or rocket_x <= -175:
        pygame.quit()
        print("Game Over")

    pygame.display.update()
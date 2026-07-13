import pygame

pygame.init()

screen = pygame.display.set_mode((750, 750))

image_1 = pygame.image.load("C:/Users/nkema/OneDrive/Desktop/Jetlearn/Pro Game Dev/Images/lights_off.png")
image_1 = pygame.transform.scale(image_1,(750,750))

image_2 = pygame.image.load("C:/Users/nkema/OneDrive/Desktop/Jetlearn/Pro Game Dev/Images/lights_on.jpeg")
image_2 = pygame.transform.scale(image_2,(750,750))

on = False
screen.blit(image_1, (0, 0))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if on == True:
                on = False
                screen.blit(image_1, (0, 0))
            else:
                on = True
                screen.blit(image_2, (0, 0))

    pygame.display.update()
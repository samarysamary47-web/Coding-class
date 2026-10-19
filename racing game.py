import pygame,os
from pygame.locals import *

width = 1000
height = 750

pygame.init()
pygame.display.set_caption("Racing Game")
screen = pygame.display.set_mode((width,height))

car = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\racecar.png")
car = pygame.transform.scale(car,(100,125))

car_rect = car.get_rect()

while 1:

    screen.fill((20,200,20))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_a:
                #car_rect = car.get_rect()#(((width // 2) - (car.get_width() // 2)),( height - 150)))
                car_rect.x -= 20
                print("works A")
                #screen.blit(car, car_rect)
            elif event.key == K_d:
                #car_rect = car.get_rect()#(((width // 2) - (car.get_width() // 2)),( height - 150)))
                car_rect.x += 20
                print("works D")
                #screen.blit(car, car_rect)

    screen.blit(car, car_rect)

    pygame.display.update()
import pygame, random
from pygame.locals import *

width = 1000
height = 750
game_over = False

pygame.init()
pygame.display.set_caption("Racing Game")
screen = pygame.display.set_mode((width, height))

car = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\racecar.png")
car = pygame.transform.scale(car, (100, 125))

tire = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\tire.png")
tire = pygame.transform.scale(tire, (60, 60))

car_rect = car.get_rect()
car_rect.topleft = (width // 2 - 50, height - 125)

tire_rect = tire.get_rect()
tire_rect.y = height

while True:
    screen.fill((20, 200, 20))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:
            if event.key == K_a:
                car_rect.x -= 20
            elif event.key == K_d:
                car_rect.x += 20

    if tire_rect.y >= height:
        tire_rect.x = random.randint(0, width - 60)
        tire_rect.y = -60

    tire_rect.y += 1

    if not game_over:
        screen.blit(tire, tire_rect)
        screen.blit(car, car_rect)
    else:
        font = pygame.font.SysFont("Times New Roman", 40,False,False)
        text = font.render("You lost!", True, (0,0,0),(20, 200, 20))
        screen.blit(text,(width // 2,height // 2))

    if car_rect.colliderect(tire_rect):
        game_over = True

    pygame.display.update()
import pygame,os,random
from pygame.locals import *

width = 1000
height = 750
score = 0

apple_x = random.randint(0,width-50)
apple_y = 100

pygame.init()
screen = pygame.display.set_mode((width,height))

background = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Flappy Bird Images\\bg(1).png")
background = pygame.transform.scale(background,(width,height))

basket = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\basket.png")
basket = pygame.transform.scale(basket,(200,200))

apple = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\apple.png")
apple = pygame.transform.scale(apple,(50,50))

apple_y = 100

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    basket_x = pygame.mouse.get_pos()[0]

    screen.blit(background,(0,0))
    screen.blit(basket,(basket_x - 100,550))
    screen.blit(apple,(apple_x,apple_y))

    font = pygame.font.SysFont("Times New Roman", 40,False,False)
    text = font.render(f"score: {score}", True, (0,0,0), "lightblue")
    screen.blit(text,(100,50))

    apple_y += 1

    apple_rect = apple.get_rect()
    apple_rect.x = apple_x
    apple_rect.y = apple_y

    basket_rect = basket.get_rect()
    basket_rect.x = basket_x - 100
    basket_rect.y = 550

    if apple_rect.colliderect(basket_rect):
        apple_y = 100
        apple_x = random.randint(0,width-50)
        score += 1
    elif apple_y > height:
        apple_y = 100
        score -= 1

    pygame.display.update()

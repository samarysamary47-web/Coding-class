import pygame,os
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((750,750))

mouse_down = False

font = pygame.font.SysFont("Times New Roman", 40,False,False)
text = font.render("Summer", True, (0,0,0), "White")
text2 = font.render("Winter", True, (0,0,0), "White")
text3 = font.render("Spring", True, (0,0,0), "White")
text4 = font.render("Autumn", True, (0,0,0), "White")


summer = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\summer.jpeg")
summer = pygame.transform.scale(summer,(90,90))

winter = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\winter.jpeg")
winter = pygame.transform.scale(winter,(90,90))

spring = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\spring.jpeg")
spring = pygame.transform.scale(spring,(90,90))

autumn = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\autumn.jpeg")
autumn = pygame.transform.scale(autumn,(90,90))

screen.fill((255,255,255))

screen.blit(text,(450,200))
screen.blit(text2,(450,300))
screen.blit(text3,(450,400))
screen.blit(text4,(450,500))

screen.blit(summer,(200,375))
screen.blit(winter,(200,175))
screen.blit(spring,(200,475))
screen.blit(autumn,(200,275))

pygame.display.update()

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen,(0,0,0),(pos),25)
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
            pos1 = pygame.mouse.get_pos()
            pygame.draw.line(screen,(0,0,0),pos,pos1,5)
            pygame.draw.circle(screen,(0,0,0),(pos1),25)

        pygame.display.update()
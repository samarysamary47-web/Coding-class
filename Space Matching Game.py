import pygame,os
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((750,750))

mouse_down = False
font = pygame.font.SysFont("Times New Roman", 40,False,False)
text = font.render("Closest to the Sun", True, (255,255,255), "Black")
font = pygame.font.SysFont("Times New Roman", 40,False,False)
text2 = font.render("Smallest", True, (255,255,255), "Black")
text3 = font.render("Habitable", True, (255,255,255), "Black")
text4 = font.render("Red", True, (255,255,255), "Black")
text5 = font.render("Ringed", True, (255,255,255), "Black")
text6 = font.render("Largest", True, (255,255,255), "Black")
font = pygame.font.SysFont("Times New Roman", 30,False,False)
text7 = font.render("Farthest from the Sun", True, (255,255,255), "Black")
font = pygame.font.SysFont("Times New Roman", 40,False,False)
text8 = font.render("blue", True, (255,255,255), "Black")


mercury = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\mercury.jpeg")
mercury = pygame.transform.scale(mercury,(90,90))

venus = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\venus.jpeg")
venus = pygame.transform.scale(venus,(90,90))

earth = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\earth.jpeg")
earth = pygame.transform.scale(earth,(90,90))

mars = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\mars.jpeg")
mars = pygame.transform.scale(mars,(90,90))

jupiter = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\jupiter.jpeg")
jupiter = pygame.transform.scale(jupiter,(90,90))

saturn = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\saturn.jpeg")
saturn = pygame.transform.scale(saturn,(90,90))

uranus = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\uranus.jpeg")
uranus = pygame.transform.scale(uranus,(90,90))

neptune = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\neptune.jpeg")
neptune = pygame.transform.scale(neptune,(90,90))

planets = [neptune,uranus,venus,mercury,earth,mars,saturn,jupiter]

texts = [text, text2, text3, text4, text5, text6, text7, text8]

screen.fill((0,0,0))

screen.blit(text,(450,0))
screen.blit(text2,(450,100))
screen.blit(text3,(450,200))
screen.blit(text4,(450,300))
screen.blit(text5,(450,400))
screen.blit(text6,(450,500))
screen.blit(text7,(450,600))
screen.blit(text8,(450,700))

screen.blit(mercury,(200,375))
screen.blit(venus,(200,175))
screen.blit(earth,(200,475))
screen.blit(mars,(200,275))
screen.blit(jupiter,(200,575))
screen.blit(saturn,(200,675))
screen.blit(uranus,(200,75))
screen.blit(neptune,(200,0))

pygame.display.update()

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen,(255,255,255),(pos),25)
            for i in range(len(planets)):
                r1 = planets[i].get_rect(topleft = (200,i * 100))
                if r1.collidepoint(pos):
                    n1 = True
                    print("1st click")
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
            pos1 = pygame.mouse.get_pos()
            pygame.draw.line(screen,(255,255,255),pos,pos1,5)
            pygame.draw.circle(screen,(255,255,255),(pos1),25)
            for i in range(len(texts)):
                r2 = texts[i].get_rect(topleft = (450, i * 100))
                if r2.collidepoint(pos1) and n1 == True:
                    print("Working")
                    n1 = False

        pygame.display.update()
import pygame
from pygame.locals import *
#Game setup
pygame.init()
screen = pygame.display.set_mode((750,750))

#BG setup
background = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\space_bg.jpeg")
background = pygame.transform.scale(background,(750,750))
#players
player_1i = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\spaceship.png")
player_1i = pygame.transform.scale(player_1i,(75,75))
player_1i = pygame.transform.rotate(player_1i,270)

player_2i = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\spaceship.png")
player_2i = pygame.transform.scale(player_2i,(75,75))
player_2i = pygame.transform.rotate(player_2i,90)

class player:
    def __init__(self,number,X,Y):
        self.number = number
        self.X = X
        self.Y = Y

    def shoot(self):
        pygame.draw.rect(screen, (255,255,255),(self.X,self.Y,20,10))


player_1 = player(1,100,375)
player_2 = player(2,100,375)

while 1:

    #drawing
    screen.blit(background,(0,0)) 
    screen.blit(player_1i,(player_1.X,player_1.Y)) 
    screen.blit(player_2i,(player_2.X,player_2.Y))

    #Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
#movement    
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                player_1.shoot()
            if event.key == K_w:
                player_1.Y -= 10
            if event.key == K_a:
                player_1.X -= 10
            if event.key == K_s:
                player_1.Y += 10
            if event.key == K_d:
                player_1.X += 10

            if player_1.X >= 285:
                player_1.X = 285
            elif player_1.X <= 0:
                player_1.X = 0
            if player_1.Y >= 675:
                player_1.Y = 675 
            elif player_1.Y <= 0:
                player_1.Y = 0

    pygame.draw.rect(screen, (255, 255, 255), (360,0,40,750))

    pygame.display.update()
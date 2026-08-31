import pygame
from pygame.locals import *
#Game setup
pygame.init()
screen = pygame.display.set_mode((750,750))

shot_1 = False
x = 0
shot_2 = False
x2 = 0
score1 = 0
score2 = 0

#BG setup
background = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\space_bg.jpeg")
background = pygame.transform.scale(background,(750,750))
#players
player_1i = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\spaceship.png")
player_1i = pygame.transform.scale(player_1i,(75,75))
player_1i = pygame.transform.rotate(player_1i,270)

player_1i_rect = player_1i.get_rect()

player_2i = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\spaceship.png")
player_2i = pygame.transform.scale(player_2i,(75,75))
player_2i = pygame.transform.rotate(player_2i,90)

player_2i_rect = player_2i.get_rect()

bullet1 = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\bullet.png")
bullet1 = pygame.transform.scale(bullet1,(100,50))
bullet1 = pygame.transform.rotate(bullet1,90)

bullet2 = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Images\\bullet.png")
bullet2 = pygame.transform.scale(bullet2,(100,50))
bullet2 = pygame.transform.rotate(bullet2,90)

class player:
    def __init__(self,number,X,Y):
        self.number = number
        self.X = X
        self.Y = Y

    def shoot(self):
        global shot_1,shot_2

        if self.number == 1:
            shot_1 = True

        if self.number == 2:
            shot_2 = True


player_1 = player(1,100,375)
player_2 = player(2,600,375)

while 1:

    bullet1_rect = bullet1.get_rect()
    bullet2_rect = bullet2.get_rect()

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

            if event.key == K_KP_0:
                player_2.shoot()

            if event.key == K_w:
                player_1.Y -= 10
            if event.key == K_a:
                player_1.X -= 10
            if event.key == K_s:
                player_1.Y += 10
            if event.key == K_d:
                player_1.X += 10

            if event.key == K_UP:
                player_2.Y -= 10
            if event.key == K_LEFT:
                player_2.X -= 10
            if event.key == K_DOWN:
                player_2.Y += 10
            if event.key == K_RIGHT:
                player_2.X += 10

            if player_1.X >= 285:
                player_1.X = 285
            elif player_1.X <= 0:
                player_1.X = 0
            if player_1.Y >= 675:
                player_1.Y = 675 
            elif player_1.Y <= 0:
                player_1.Y = 0

            if player_2.X <= 400:
                player_2.X = 400
            elif player_2.X >= 700:
                player_2.X = 700
            if player_2.Y >= 675:
                player_2.Y = 675 
            elif player_2.Y <= 0:
                player_2.Y = 0

    pygame.draw.rect(screen, (255, 255, 255), (360,0,40,750))

    player_1i_rect.topleft = (player_1.X, player_1.Y)
    player_2i_rect.topleft = (player_2.X, player_2.Y)

    font = pygame.font.SysFont("Times New Roman", 40,False,False)
    text = font.render("Player 1:{}     player 2:{}".format(score1,score2), True, (0,0,0), "White")
    screen.blit(text,(190,700))

    if not shot_1:
        px = player_1.X
        py = player_1.Y

    if shot_1:
        screen.blit(bullet1,(px + x,py))
        bullet1_rect.topleft = (px + x,py)
        x += 1
        if x > 750:
            shot_1 = False
            x = 0

        if bullet1_rect.colliderect(player_2i_rect):
            score1 += 10
            shot_1 = False
            x = 0

    if not shot_2:
        p2x = player_2.X - 30
        p2y = player_2.Y

    if shot_2:
        screen.blit(bullet2,(p2x - x2,player_2.Y))
        bullet2_rect.topleft = (p2x - x2,player_2.Y)
        x2 += 1
        if x2 > 750:
            shot_2 = False
            x2 = 0

        if bullet2_rect.colliderect(player_1i_rect):
            score2 += 10
            shot_2 = False
            x2 = 0

    pygame.display.update()
import pygame,os
from pygame.locals import *

width = 1000
height = 750

ground_movement = 0
scroll_speed = 1

pygame.init()
screen = pygame.display.set_mode((width,height))

background = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Flappy Bird Images\\bg(1).png")
background = pygame.transform.scale(background,(width,height))

#bird = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Flappy Bird Images\\bird1(1).png")
#bird = pygame.transform.scale(bird,(100,75))

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.bird_animation = []
        self.index = 0
        self.counter = 0
        for i in range(1,4):
            img = pygame.image.load(f"C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Flappy Bird Images\\bird{i}.png")
            self.bird_animation.append(img)
        self.image = self.bird_animation[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.vel = 0
        self.click = False
        self.flying = False
        self.game_over = False

    def update(self):
        if self.flying:
            self.vel += 0.2
        if not self.game_over:
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True
                self.vel = -2
                print("working")
            elif pygame.mouse.get_pressed()[0] == 0:
                self.click = False

        self.flap_cooldown = 2
        self.counter += 1

        if self.counter > self.flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.bird_animation):
                self.index = 0
            self.image = self.bird_animation[self.index]


bird_group = pygame.sprite.Group()
flappy_bird = Bird(100,height//2)
bird_group.add(flappy_bird)

ground = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Flappy Bird Images\\ground.png")
ground = pygame.transform.scale(ground,(width + 75,100))

pipe = pygame.image.load("C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Pro Game Dev\\Flappy Bird Images\\pipe(1).png")
pipe = pygame.transform.scale(ground,(width,100))

while 1:

    screen.blit(background,(0,0))
    bird_group.draw(screen)
    bird_group.update()

    screen.blit(ground,(ground_movement,height - 20))
    ground_movement -= scroll_speed
    if ground_movement < -75:
        ground_movement = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
import pygame, random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1000,750))

width = 1000
height = 750

level = 1
instructions = "WASD to move, go on the correct colours"
colour = "go on red to start game"

game_started = False
game_over = False
timer = 0

yellow_rect = pygame.Rect(100, 600, 200, 100)
red_rect = pygame.Rect(400, 600, 200, 100)
blue_rect = pygame.Rect(700, 600, 200, 100)

class player():
    def __init__(self):
        self.x = width // 2
        self.y = height // 2
        self.rect = pygame.Rect(self.x, self.y, 50, 50)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[K_w]:
            self.y -= 3
        if keys[K_s]:
            self.y += 3
        if keys[K_a]:
            self.x -= 3
        if keys[K_d]:
            self.x += 3

        self.rect.center = (self.x, self.y)

Player = player()

clock = pygame.time.Clock()

while True:

    screen.fill("lightgrey")

    pygame.draw.rect(screen, "yellow", yellow_rect)
    pygame.draw.rect(screen, "red", red_rect)
    pygame.draw.rect(screen, "blue", blue_rect)

    pygame.draw.circle(screen, (0,0,0), (int(Player.x),int(Player.y)), 25)

    font = pygame.font.SysFont("Times New Roman", 50, False, False)

    if not game_started and not game_over:
        instruction_text = font.render(instructions,True,(0,0,0))
        screen.blit(instruction_text, (75,120))
        if Player.rect.colliderect(red_rect):
            game_started = True
            colour = random.choice(["yellow", "blue"])
            timer = pygame.time.get_ticks()
            Player.x = width // 2
            Player.y = height // 2
            Player.rect.center = (Player.x, Player.y)

        text = font.render(colour, True, (0,0,0))
        screen.blit(text, (75,50))

    elif game_started:
        remaining = 5 - (pygame.time.get_ticks() - timer) // 1000

        text = font.render("Go on " + colour, True, (0,0,0))
        screen.blit(text, (75,50))

        timer_text = font.render("Time: " + str(remaining), True, (0,0,0))
        screen.blit(timer_text, (75,120))

        level_text = font.render("Level: " + str(level), True, (0,0,0))
        screen.blit(level_text, (75,190))

        if pygame.time.get_ticks() - timer >= 5000:
            game_over = True

        if colour == "yellow":
            if Player.rect.colliderect(yellow_rect):
                Player.x = width // 2
                Player.y = height // 2
                Player.rect.center = (Player.x, Player.y)
                level += 1
                colour = random.choice(["red", "blue"])
                timer = pygame.time.get_ticks()
            elif Player.rect.colliderect(blue_rect) or Player.rect.colliderect(red_rect):
                game_over = True

        elif colour == "blue":
            if Player.rect.colliderect(blue_rect):
                Player.x = width // 2
                Player.y = height // 2
                Player.rect.center = (Player.x, Player.y)
                level += 1
                colour = random.choice(["red", "yellow"])
                timer = pygame.time.get_ticks()
            elif Player.rect.colliderect(yellow_rect) or Player.rect.colliderect(red_rect):
                game_over = True

        elif colour == "red":
            if Player.rect.colliderect(red_rect):
                Player.x = width // 2
                Player.y = height // 2
                Player.rect.center = (Player.x, Player.y)
                level += 1
                colour = random.choice(["yellow", "blue"])
                timer = pygame.time.get_ticks()
            elif Player.rect.colliderect(yellow_rect) or Player.rect.colliderect(blue_rect):
                game_over = True

    if game_over:
        text = font.render("YOU LOSE!", True, (255,0,0))
        screen.blit(text, (350,300))
    elif level >= 10:
        text = font.render("YOU WIN!", True, (0,255,0))
        screen.blit(text, (350,300))

    Player.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
    clock.tick(60)
import pygame

pygame.init()
screen = pygame.display.set_mode((750,750))

class Ball():
    def __init__(self,size,colour):
        self.size = size
        self.colour = colour
        self.surface = screen
    
    def grow(self):
        self.size += 5
    
    def shrink(self):
        self.size -= 5
    
    def draw(self):
        pygame.draw.circle(self.surface,
                           self.colour,
                           (375,375),
                           self.size)

ball = Ball(20,"white")

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball.grow()
                ball.draw()
                print("it works")
            elif event.key == pygame.K_BACKSPACE:
                screen.fill("pink")
                ball.shrink()
                ball.draw()
                print("it works")
                pygame.draw.circle(ball.surface,
                           ball.colour,
                           (375,375),
                           ball.size)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ball.draw()
    
    pygame.display.update()
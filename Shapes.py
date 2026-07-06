import pygame

pygame.init()
screen = pygame.display.set_mode((750, 750))

shape = "none"

while 1:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                shape = "rect"
            elif event.key == pygame.K_c:
                shape = "circle"
            elif event.key == pygame.K_l:
                shape = "line"

    if shape == "rect":
        pygame.draw.rect(screen, (255, 0, 0), (175, 275, 200, 100))
    elif shape == "circle":
        pygame.draw.circle(screen, (0, 0, 255), (375, 375), 80)
    elif shape == "line":
        pygame.draw.line(screen, (0, 255, 0), (100, 400), (400, 400), 5)

    pygame.display.update()
import pygame,time

pygame.init()
screen = pygame.display.set_mode((750, 750))

image_1 = pygame.image.load("C:/Users/nkema/OneDrive/Desktop/Jetlearn/Pro Game Dev/Images/birthday_card.jpeg")
image_1 = pygame.transform.scale(image_1,(750,750))

image_2 = pygame.image.load("C:/Users/nkema/OneDrive/Desktop/Jetlearn/Pro Game Dev/Images/birthday_message.png")
image_2 = pygame.transform.scale(image_2,(750,750))

Marquee_x = 850

while 1:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(image_1,(0,0))
    pygame.display.update()
    time.sleep(3)
    screen.fill((255,255,255))

    screen.blit(image_2,(0,0))
    pygame.display.update()
    time.sleep(3)
    screen.fill((255,255,255))

    font = pygame.font.SysFont("Times New Roman", 40,False,False)
    text = font.render("I wish you a HAPPY BIRTHDAY!", True, (0,0,0), "Red")
    Marquee_x = 850
    screen.blit(text,(Marquee_x,325))
    pygame.display.update()
    for i in range(900):
        screen.fill((255,255,255))
        Marquee_x -= 1
        screen.blit(text,(Marquee_x,325))
        pygame.display.update()
    screen.fill((255,255,255))
    
import pgzrun,random

WIDTH = 700
HEIGHT = 600
TITLE = "Bee Game"
score = 0
has_ended = False
message = "Your score was {}".format(score)

#Creating the actors
bee = Actor("bee")
bee.pos = WIDTH / 2,HEIGHT / 2
flower = Actor("flower")
flower.pos = random.randint(50,450),random.randint(50,450)
time = 25

def draw():
    global message,time
    message = "Your score was {}".format(score)
    if not has_ended:
        screen.fill("lightblue")
        bee.draw()
        flower.draw()
        screen.draw.text("Time left:{}".format(time),center = (WIDTH/2,HEIGHT/8))
    else:
        screen.fill("lightblue")
        screen.draw.text(message,center = (WIDTH/2,HEIGHT/2))

def update():
    global score
    if keyboard.left:
        if bee.x > 0:
            bee.x -= 5
    if keyboard.right:
        if bee.x < WIDTH:
            bee.x += 5
    if keyboard.up:
        if bee.y > 0:
            bee.y -= 5
    if keyboard.down:
        if bee.y < HEIGHT:
            bee.y += 5
    if bee.colliderect(flower):
        score += 1
        while bee.colliderect(flower):
            flower.pos = random.randint(50,450),random.randint(50,450)

def end():
    global has_ended
    has_ended = True

def countdown():
    global time
    time -= 1

def move():
    flower.pos = random.randint(50,450),random.randint(50,450)

clock.schedule(end,25)
clock.schedule_interval(countdown,1)
clock.schedule_interval(move,1)

pgzrun.go()
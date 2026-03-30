import pgzrun, random

WIDTH = 500
HEIGHT = 500

Alien = Actor("alien")

message = "Click the Alien"
score = 0
color = "lightblue"

def draw():
    screen.clear()
    screen.fill(color)
    Alien.draw()
    screen.draw.text(message,center = (400,20))
    screen.draw.text(str(score),center = (250,20))

def on_mouse_down(pos):
    global message, score, color
    if Alien.collidepoint(pos):
        message = "Good shot!"
        score += 1
        move()
        color = "lightgreen"
    else:
        message = "You missed!"
        color = "red"

def move():
    Alien.x = random.randint(0,WIDTH)
    Alien.y = random.randint(0,HEIGHT)

clock.schedule_interval(move,1)

pgzrun.go()
import pgzrun

WIDTH = 500
HEIGHT = 500
y = HEIGHT / 2
velocity = 0 
gravity = 0.5 

def draw():
    screen.clear()
    screen.fill("lightblue")
    screen.draw.text("Click to jump", center=(WIDTH / 2, 20), color="black")
    rect = Rect((0, 0), (50, 50))
    rect.center = WIDTH / 2, y
    screen.draw.filled_rect(rect, "green")

def on_mouse_down():
    global velocity
    velocity = -10 

def update():
    global y, velocity
    velocity += gravity 
    y += velocity 

    if y > 475:
        y = 475
        velocity = 0
    if y < 25:
        y = 25
        velocity = 0

pgzrun.go()
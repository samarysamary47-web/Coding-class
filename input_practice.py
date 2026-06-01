import pgzrun

WIDTH = 500
HEIGHT = 500
x = 50
j = 1

def draw():
    screen.clear()
    screen.fill("lightblue")
    screen.draw.text("Click to change direction", center=(WIDTH / 2, 20), color="black")
    rect = Rect((0, 0), (50, 50))
    rect.center = x, WIDTH / 2
    screen.draw.filled_rect(rect, "green")

def on_mouse_down():
    global j
    j *= -1

def move():
    global x, j
    x += (j * 5)
    
    if x >= WIDTH or x <= 0:
        j *= -1

clock.schedule_interval(move, 0.01)
pgzrun.go()

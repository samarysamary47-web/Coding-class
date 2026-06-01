import pgzrun
WIDTH = 500
HEIGHT = 500
x = WIDTH / 2
y = HEIGHT / 2
c = "black"
def on_mouse_move(pos):
    global x, y
    x = pos[0]
    y = pos[1]
def on_mouse_down(pos):
    global c
    c = "red"
def on_mouse_up(pos):
    global c
    c = "black"
def draw():
    screen.fill("white")
    screen.draw.filled_circle((x, y), 20, c)
    if c == "red":
        screen.draw.text("Good job!", center = (WIDTH / 2, 10), color="red")
    else:
        screen.draw.text("Click the circle!", center = (WIDTH / 2, 10), color="black")
pgzrun.go()
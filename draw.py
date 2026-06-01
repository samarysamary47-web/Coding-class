import pgzrun

WIDTH = 500
HEIGHT = 500
TITLE = "Drawing App"

points = {}
is_drawing = False

Delete = Actor("delete button")
light = Actor("light")
dark = Actor("dark")

def on_mouse_down(pos):
    global is_drawing
    if Delete.collidepoint(pos):
        points.clear()
    is_drawing = True

def on_mouse_up():
    global is_drawing
    is_drawing = False

def on_mouse_move(pos):
    if is_drawing:
        points[len(points)] = pos

def draw():
    screen.fill("white")
    Delete.draw()
    Delete.x = 425
    Delete.y = 75
    light.draw()
    light.x = 75
    light.y = 75
    dark.draw()
    dark.x = 150
    dark.y = 75
    for i in points:
        screen.draw.filled_circle(points[i], 5, "black")

pgzrun.go()

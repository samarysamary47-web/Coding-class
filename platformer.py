import pgzrun

WIDTH = 700
HEIGHT = 600
TITLE = "Platformer"

player = Actor("guy")
player.pos = WIDTH / 2, HEIGHT - 90

velocity_y = 0
gravity = 0.5
jump_strength = -12
in_the_air = False

def draw():
    screen.fill("lightblue")
    screen.draw.filled_rect(Rect((0, HEIGHT - 50), (WIDTH, 50)), "lightgreen")
    player.draw()

def update():
    global velocity_y, in_the_air
    if keyboard.d and player.x < WIDTH - 30:
        player.x += 5
    if keyboard.a and player.x > 30:
        player.x -= 5
    if keyboard.w and not in_the_air:
        velocity_y = jump_strength
        in_the_air = True

    player.y += velocity_y
    velocity_y += gravity

    if player.y >= HEIGHT - 90:
        player.y = HEIGHT - 90
        velocity_y = 0
        in_the_air = False

pgzrun.go()
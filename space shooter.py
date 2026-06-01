import pgzrun

WIDTH = 750
HEIGHT = 500
TITLE = "Space Shooter"

player = Actor("spaceship")
player.pos = WIDTH // 2, HEIGHT - 50

enemies = []
for row in range(5):
    for column in range(5):
        enemy = Actor("enemy_spaceship")
        enemy.pos = row * 50,column * 35
        enemies.append(enemy)

def draw():
    screen.fill("lightblue")

    player.draw()
    for i in enemies:
        i.draw()

def shoot():
    #empty for now
    print(" ")

def update():
    if keyboard.a:
        player.x -= 10
    if keyboard.d:
        player.x += 10
    if keyboard.SPACE:
        shoot()

pgzrun.go()
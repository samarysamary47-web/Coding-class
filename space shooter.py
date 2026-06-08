import pgzrun

WIDTH = 750
HEIGHT = 500
TITLE = "Space Shooter"

turn = "left"
cooldown = False
win = False

player = Actor("spaceship")
player.pos = WIDTH // 2, HEIGHT - 50

bullets = []

enemies = []
for row in range(1):
    for column in range(1):
        enemy = Actor("enemy_spaceship")
        enemy.pos = row * 50 + 250,column * 35 + 20
        enemies.append(enemy)

def draw():
    screen.fill("lightblue")

    if not win:
        player.draw()

        for i in enemies:
            i.draw()

        for i in bullets:
            i.draw()
            i.y -= 1
    else:
        screen.draw.text("Well done. You won!",0,0,fontsize = 40,
                         color = "black",
                         center = (WIDTH // 2,HEIGHT // 2))

def shoot():
    global cooldown,bullets

    if not cooldown:
        bullet = Actor("bullet")
        bullet.pos = player.pos
        bullets.append(bullet)

def update():
    global win

    if keyboard.a:
        player.x -= 10
    if keyboard.d:
        player.x += 10
    for i in enemies:
        for j in bullets:
            if i.collidepoint(j.pos):
                enemies.remove(i)
                bullets.remove(j)
            if j.y <= 0:
                bullets.remove(j)
    if not enemies:
        win = True

def on_key_up(key):
    global cooldown

    if key == keys.SPACE:
        shoot()
        cooldown = True

        cooldown = False

def move_down():
    global turn
    for i in enemies:
        i.y += 25

def move_sideways():
    global turn

    for i in enemies:
        if turn == "left":
            i.x -= 25
        else:
            i.x += 25

def switch():
    global turn

    if turn == "left":
        turn = "right"
    else:
        turn = "left"

clock.schedule_interval(move_down,3)
clock.schedule_interval(move_sideways,1)
clock.schedule_interval(switch,5)

pgzrun.go()
import pgzrun,time

WIDTH = 750
HEIGHT = 500
TITLE = "Space Shooter"

turn = "left"
win = False
game_over = False

player = Actor("spaceship")
player.pos = WIDTH // 2, HEIGHT - 50

bullets = []

enemies = []
for row in range(5):
    for column in range(5):
        enemy = Actor("enemy_spaceship")
        enemy.pos = row * 50 + 250, column * 35 + 20
        enemies.append(enemy)

last_shot = 0
SHOT_DELAY = 0.4

def draw():
    screen.fill("lightblue")

    if win:
        screen.draw.text(
            "Well done. You won!",
            center = (WIDTH // 2, HEIGHT // 2),
            fontsize = 40,
            color = "green"
        )
        return

    if game_over:
        screen.draw.text(
            "Game Over!",
            center = (WIDTH // 2, HEIGHT // 2),
            fontsize = 40,
            color = "red"
        )
        return

    player.draw()

    for i in enemies:
        i.draw()

    for i in bullets:
        i.draw()

def shoot():
    global last_shot

    now = time.time()

    if now - last_shot >= SHOT_DELAY:
        bullet = Actor("bullet")
        bullet.pos = player.pos
        bullets.append(bullet)
        last_shot = now

def update():
    global win, game_over

    if win or game_over:
        return

    if keyboard.a:
        player.x -= 10
    if keyboard.d:
        player.x += 10

    for i in bullets[:]:
        i.y -= 6

        if i.y <= 0:
            bullets.remove(i)

    for i in enemies[:]:
        for j in bullets[:]:
            if i.collidepoint(j.pos):
                enemies.remove(i)
                bullets.remove(j)
                break

    for i in enemies:
        if i.y >= HEIGHT - 80:
            game_over = True

    if not enemies:
        win = True

def on_key_down(key):
    if key == keys.SPACE:
        shoot()

def move_down():
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

clock.schedule_interval(move_down, 3)
clock.schedule_interval(move_sideways, 1)
clock.schedule_interval(switch, 5)

pgzrun.go()
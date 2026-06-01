import pgzrun, random

WIDTH = 1000
HEIGHT = 750
TITLE = "Recycling Game"

score = 0

bags = []
for i in range(30):
    bag = Actor("bag")
    bag.pos = random.randint(30, WIDTH - 30), random.randint(30, HEIGHT - 30)
    bags.append(bag)

plastic = []
for i in range(20):
    plastic_bag = Actor("plastic_bag")
    plastic_bag.pos = random.randint(30, WIDTH - 30), random.randint(30, HEIGHT - 30)
    plastic.append(plastic_bag)

bin = Actor("bin")
bin.pos = WIDTH // 2, HEIGHT // 2

def draw():
    screen.blit("plant_bg", (0, 0))

    for bag in bags:
        bag.draw()

    for plastic_bag in plastic:
        plastic_bag.draw()

    bin.draw()

    screen.draw.text("Score: {}".format(score), (20, 20), fontsize=40, color="white")

def update():
    global score

    if keyboard.d and bin.x < WIDTH - 40:
        bin.x += 5

    if keyboard.a and bin.x > 40:
        bin.x -= 5

    if keyboard.w and bin.y > 40:
        bin.y -= 5

    if keyboard.s and bin.y < HEIGHT - 40:
        bin.y += 5

    for bag in bags[:]:
        if bin.colliderect(bag):
            bags.remove(bag)
            score += 5

    for plastic_bag in plastic[:]:
        if bin.colliderect(plastic_bag):
            plastic.remove(plastic_bag)
            score -= 5

pgzrun.go()
import pgzrun

WIDTH = 400
HEIGHT = 400

def draw():
    w = 200
    h = 300
    r = 50
    g = 50
    b = 100
    for i in range(10):
        screen.draw.circle((WIDTH/2, HEIGHT/2), 50 * ((i + 1) / 5), (r, g, b))
        r += 10
        g += 10
        b += 10

pgzrun.go()
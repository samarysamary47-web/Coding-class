import pgzrun
WIDTH = 800
HEIGHT = 800

def draw():
    w = 200
    h = 310
    r = 102
    g = 101
    b = 100
    for i in range(10):
        rect = Rect((100,150),(w * (i*0.1),h * (i*0.1)))
        rect.center = WIDTH/2,HEIGHT/2
        screen.draw.rect(rect,(r,g,b))
        r += 10
        g += 10
        b += 10



pgzrun.go()
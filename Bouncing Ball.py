import pgzrun, random

WIDTH = 750
HEIGHT = 500
TITLE = "Bouncing Ball"

count = 0
bounce = True
direction = -1

class Ball():
    def __init__(self,x,y,radius):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.radius = radius

    def draw_ball(self):
        screen.draw.filled_circle((self.x,self.y),self.radius,"black")

ball = Ball(30,30,20)

def draw():
    global count

    screen.fill("lightblue")
    ball.draw_ball()

    screen.draw.text("Bounces: {}".format(count), (10, 10),
                      color="black", fontsize=30)

# displacement = (u + v) / (2 * t)
# u = initial velocity
# v = final velocity
# t = time
# v = u + at(a = acceleration)

def update(dt):
    global count, bounce, direction

    uy = ball.vy
    ball.vy += (dt * 2000)
    ball.y += (uy + ball.vy ) * 0.5 * dt

    if ball.y >= HEIGHT - ball.radius:
        ball.y = HEIGHT - ball.radius
        if bounce:
            ball.vy = -ball.vy * 0.8

        if count <= 11:
            count += 1
        else:
            bounce = False
        
    ball.x += ball.x * dt * direction

    if ball.x >= WIDTH - ball.radius or ball.x <= ball.radius:
        direction *= -1

pgzrun.go()
import pgzrun, random

WIDTH = 750
HEIGHT = 500
TITLE = "Bouncing Ball"

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
    screen.fill("lightblue")
    ball.draw_ball()

# displacement = (u + v) / (2 * t)
# u = initial velocity
# v = final velocity
# t = time
# v = u + at(a = acceleration)

def update(dt):
    uy = ball.vy
    ball.vy += (dt * 2000)
    ball.y += (uy + ball.vy ) * 0.5 * dt

pgzrun.go()
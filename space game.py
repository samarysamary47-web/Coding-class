import pgzrun,random

WIDTH = 750
HEIGHT = 500
TITLE = "Space Game"

satellites = []
j = 1
next_satellite = 0
total_satellites = 10
lines = []
elapsed_time = 0

for i in range(total_satellites):
    Satellite = Actor("satellite")
    Satellite.pos = (random.randint(50,WIDTH - 50),random.randint(50,HEIGHT - 50))

    satellites.append(Satellite)


def tick():
    global elapsed_time
    if next_satellite < total_satellites:
        elapsed_time += 1

clock.schedule_interval(tick, 1.0)


def draw():
    global j
    screen.blit("space background",(0,0))
    screen.draw.text("Time: {}".format(elapsed_time), topleft=(10, 10), fontsize=40, color="white")
    for i in satellites:
        i.draw()
        screen.draw.text(str(j),center = (i.pos[0],i.pos[1] + 30))
        j += 1
    j = 1
    for line in lines:
         screen.draw.line(line[0],line[1],"White")
    

def on_mouse_down(pos):
        global next_satellite,total_satellites,lines
        if next_satellite < total_satellites:
            if satellites[next_satellite].collidepoint(pos):
                if next_satellite:
                    lines.append((satellites[next_satellite - 1].pos,satellites[next_satellite].pos))
                next_satellite += 1
        else:
             lines = []
             next_satellite = 0

pgzrun.go()
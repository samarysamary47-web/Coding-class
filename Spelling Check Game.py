import pgzrun

WIDTH = 750
HEIGHT = 500
TITLE = "Spelling Check Game"

score = 0
timer = 5
spelling = ""
spelling_l = []
s_num = 0
number = 0
lose = False
win = False
file = "C:\\Users\\nkema\\OneDrive\\Desktop\\Jetlearn\\Game Development\\Spellings.txt"

def next_spelling():
    global spelling,s_num,win

    spelling_l = []

    qfile = open(file,"r")

    for line in qfile:
        spelling_l.append(line)

    qfile.close()

    try:
        spelling = spelling_l[s_num]
        spelling = spelling.split(",")
    except IndexError:
        win = True

next_spelling()

wrong_box = Rect(20,HEIGHT - 120,WIDTH // 2 - 50,HEIGHT // 6)
correct_box = Rect(375,HEIGHT - 120,WIDTH // 2 - 50,HEIGHT // 6)
spelling_box = Rect(WIDTH // 4 + 25,HEIGHT // 3 - 50,WIDTH // 4 + 100,WIDTH // 4)

def draw():
    if not lose:
        screen.fill("lightblue")

        screen.draw.filled_rect(correct_box,color = "green")
        screen.draw.filled_rect(wrong_box,color = "red")
        screen.draw.filled_rect(spelling_box,color = "orange")

        screen.draw.textbox("Correct",correct_box,color = "black")
        screen.draw.textbox("Wrong",wrong_box,color = "black")
        screen.draw.textbox(spelling[number],spelling_box,color = "black")
    else:
        screen.fill("lightblue")
        screen.draw.text("You lose! Your score was {}".format(score),(WIDTH // 2 - 300,HEIGHT // 2 - 25),color = "black",fontsize = 40)
    if win:
        screen.fill("lightblue")
        screen.draw.text("You Won! Your score was {}".format(score),(WIDTH // 2 - 300,HEIGHT // 2 - 25),color = "black",fontsize = 40)

def on_mouse_down(pos):
    global lose,number,s_num,score

    if correct_box.collidepoint(pos):
        if spelling[number] == spelling[int(spelling[4]) - 1]:
            if number == 3:
                s_num += 1
                number = 0
            else:
                number += 1
            next_spelling()
            score += 1
        else:
            lose = True
    
    if wrong_box.collidepoint(pos):
        if not spelling[number] == spelling[int(spelling[4]) - 1]:
            if number == 3:
                s_num += 1
                number = 0
            else:
                number += 1
            next_spelling()
            score += 1
        else:
            lose = True

pgzrun.go()
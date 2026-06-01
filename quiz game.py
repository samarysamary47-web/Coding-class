import pgzrun

WIDTH = 750
HEIGHT = 500
TITLE = "Quiz Game"

question_file_name = "questions.txt"
timer = 10
questions = []
current_question = 0
total_questions = 0
score = 0
game_over = False
win = False

def read_question_file():
    global total_questions
    qfile = open(question_file_name,"r")
    for line in qfile:
        questions.append(line)
        total_questions += 1
    qfile.close()

def read_next_question():
    global current_question,questions

    current_question += 1

    return questions.pop(0).split(",")


read_question_file()

question = read_next_question()

def correct():
    global win
    global score,question,timer

    score += 1
    if questions:
        question = read_next_question()
    else:
        win = True
    timer = 10

def game_is_over():
    global game_over
    game_over = True

# print(question[0])

marquee_box = Rect(0,0,WIDTH,HEIGHT // 10)
question_box = Rect(25,75,WIDTH - 50,HEIGHT // 7)
answer_box_1 = Rect(25,250,WIDTH // 3,HEIGHT // 5)
answer_box_2 = Rect(300,250,WIDTH // 3,HEIGHT // 5)
answer_box_3 = Rect(25,375,WIDTH // 3,HEIGHT // 5)
answer_box_4 = Rect(300,375,WIDTH // 3,HEIGHT // 5)
timer_box = Rect(575,250,WIDTH // 5,HEIGHT // 5)
skip_box = Rect(575,375,WIDTH // 5,HEIGHT // 5)

answer_boxes = [answer_box_1,answer_box_2,answer_box_3,answer_box_4]

def draw():
    global score

    screen.fill("black")

    if not game_over and not win:
        screen.draw.filled_rect(marquee_box,"black")
        screen.draw.filled_rect(question_box,"lightgreen")
        screen.draw.filled_rect(answer_box_1,"lightblue")
        screen.draw.filled_rect(answer_box_2,"lightblue")
        screen.draw.filled_rect(answer_box_3,"lightblue")
        screen.draw.filled_rect(answer_box_4,"lightblue")
        screen.draw.filled_rect(timer_box,"orange")
        screen.draw.filled_rect(skip_box,"red")
        
        screen.draw.textbox(question[0],question_box,color = "black")
        screen.draw.textbox("SKIP",skip_box,color = "black")
        screen.draw.textbox(str(timer),timer_box,color = "black")
        screen.draw.textbox(question[1],answer_box_1,color = "black")
        screen.draw.textbox(question[2],answer_box_2,color = "black")
        screen.draw.textbox(question[3],answer_box_3,color = "black")
        screen.draw.textbox(question[4],answer_box_4,color = "black")
    elif win:
        screen.draw.text("You won! Your score was {}".format(str(score)),(WIDTH // 2 - 200,HEIGHT // 2),color = "white",fontsize = 40)
    else:
        screen.draw.text("Game Over! Your score was {}".format(str(score)),(WIDTH // 2 - 200,HEIGHT // 2),color = "white",fontsize = 40)

def second():
    global timer
    timer -= 1

def on_mouse_down(pos):
    global timer,question
    
    index = 1

    for i in answer_boxes:
            if i.collidepoint(pos):
                if index is int(question[5]):
                    correct()
                else:
                    game_is_over()
            index += 1
    
    if skip_box.collidepoint(pos):
        question = read_next_question()
        timer = 10

def update():
    global timer

    if timer == 0:
        game_is_over()

clock.schedule_interval(second,1)

pgzrun.go()
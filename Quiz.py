question1 = ("What does 'print()' do in Python?", 
             "A. Takes input from user", 
             "B. Displays output", 
             "C. Creates a variable", 
             "D. Ends the program", 
             "B")

question2 = ("Which symbol is used for comments in Python?", 
             "A. //", 
             "B. /* */", 
             "C. #", 
             "D. --", 
             "C")

question3 = ("What data type is a tuple?", 
             "A. Mutable", 
             "B. Immutable", 
             "C. Changeable", 
             "D. Flexible", 
             "B")

question4 = ("Which keyword is used to create a function in Python?", 
             "A. func", 
             "B. define", 
             "C. def", 
             "D. function", 
             "C")

question5 = ("What will len('Hello') return?", 
             "A. 4", 
             "B. 5", 
             "C. 6", 
             "D. Error", 
             "B")

score = 0

questions = [question1, question2, question3, question4, question5]

print("Welcome to the Coding Quiz!")

try:
    for i in range(len(questions)):
        q = questions[i]
        
        print()
        print("Question {}: {}".format(i + 1, q[0]))
        
        for j in range(1, 5):
            print(q[j])
        
        answer = str(input("Enter your answer (A/B/C/D): ").upper())
        
        if answer == q[5]:
            print("Correct!")
            score += 1
        else:
            print("Wrong! The correct answer was {}".format(q[5]))

except TypeError:
    print("Please enter one of the options")

print()
print("Your final score is {}/{}".format(score, len(questions)))
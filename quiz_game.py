print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    
print("Okay! Let's play : ")

score = 0
actual_score = score-0.25

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!") 
    score = score + 1
else:
    print("Incorrect!")
    # score = score - 0.25
    actual_score = score-0.25
    
answer = input("What does GPU stand for? ")
if answer.lower() == "graphical processing unit".lower():
    print("Correct!")
    score = score + 1 
else:
    print("Incorrect!")
    # score = score - 0.25
    actual_score = score-0.25
    
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory".lower():
    print("Correct!")
    score = score + 2 
else:
    print("Incorrect!")
    # score = score - 0.25
    actual_score = score-0.75
    
answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory".lower():
    print("Correct!")
    score = score + 3
else:
    print("Incorrect!")
    # score = score - 0.25
    actual_score = score-1.25
    
print(f'you got a {score} marks')    
print("You got " + str(actual_score) + 'actual marks')  
print("You got " + str((actual_score/4)*100) + "%.")  
           
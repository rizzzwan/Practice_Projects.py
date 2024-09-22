print ("\033[1mWelcome to my 1st ever Computer Quiz!\033[0m")
playing = input ("Do you want to play? ")
if playing.lower() !="yes":
    quit ()

print ("OK! Let's start playing :) ")
score = 0
answer = input ("What does \033[1mCPU\033[0m stands for? ")

if answer.lower() == "central processing unit":
    print ("\033[92mCorrect :)\033[0m")
    score = score+1
else:
    print ("\033[91mIncorrect :/\033[0m")

answer = input ("What does \033[1mGPU\033[0m stands for? ")

if answer.lower() == "graphics processing unit":
    print ("\033[92mCorrect :)\033[0m")
    score = score+1         
else:
    print ("\033[91mIncorrect :/\033[0m")
answer = input ("What does \033[1mRAM\033[0m stands for? ")

if answer.lower() == "random access memory":
    print ("\033[92mCorrect :)\033[0m")
    score = score+1
else:
    print ("\033[91mIncorrect :/\033[0m")
answer = input ("What does \033[1mROM\033[0m stands for? ")

if answer.lower() == "read only memory":
    print ("\033[92mCorrect :)\033[0m")
    score = score+1
else:
    print ("\033[91mIncorrect :/\033[0m")

print ("You got " + str(score) + " questions correct !")

if score >= 3:
    print ("Your IQ is above \033[96m100 (Average)\033[0m ")
else: 
    print ("Your IQ is above \033[91m80 (Below average)\033[0m ")

print ("\033[4mThanks for Playing\033[0m :)")
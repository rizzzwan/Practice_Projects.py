import random

tie = 0
user_wins = 0
computer_wins = 0
options = ["r", "p", "s"]
names = {"r" : "Rock", "p" : "Paper", "s" : "Scissors"}

while True:
    user_input = input ("Enter 'R' for rock/ 'P' for paper/ 'S' for scissors or press Q to quit: ").lower()
    if user_input == "q":
        break
    elif user_input  not in options:
        print ("Invalid input, Please enter Rock, Paper or Scissors")
        continue

    random_num = random.randint(0,2)
    #  rock = 0   paper = 1   scissors = 2
    computer_pick = options[random_num]
    print ("Computer picked ",computer_pick + ".")

    if user_input == "r" and computer_pick == "s":
        print ("\033[92m You won!\033[0m")
        user_wins +=1
    elif user_input == "p" and computer_pick == "r":
        print ("\033[92m You won!\033[0m")
        user_wins +=1
    elif user_input == "s" and computer_pick == "p":
        print ("\033[92mYou won!\033[0m")
        user_wins +=1
    elif user_input == computer_pick:
        print("it's a TIE.")
        tie+= 1
    else:
        print ("\033[91mYou lost:/\033[0m")
        computer_wins +=1  

print ("\033[92mYou won\033[0m ",user_wins, "time(s).")
print ("\033[91mComputer won\033[0m",computer_wins,"time(s).")
print ("\033[95mYou TIED\033[0m", tie,"time(s)")
print ("Goodbyeee!")
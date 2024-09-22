name = input ("Enter your name: ")
print ("Here's Your Own adventure game" ,name,", you can play this game by making your own life decisions.")
start = input ("Enter Start to play: ").lower()

while start != "start":
    start = input ("Enter 'Start' to play next time: ").lower()

print ("Lets Start playing.")
answer = input ("You are going to be BORN in an Arab family in the early 200s. Be born a Girl or a Boy? ").lower()
while answer != "girl" and answer !="boy":
    answer = input ("Enter Girl/Boy to continue:").lower()
    

if answer == "girl":
    print ("You were buried alive,\033[91m GAME OVER\033[0m")
    quit()    
elif answer == "boy":
    print ("\033[4mYou survived\033[0m,lets move towards the next Question.")

answer = input ("You became an adult, you are given two career options whether to become a Camelman or a Scientist. what will you chose? ").lower()
while answer != "camel man" and answer !=  "scientist" :
    answer = input ("Enter Camel Man/Scientist: ").lower()

if answer == "camel man":
    print ("You became poorer and poorer and died a faliure. \033[91m GAME OVER\033[0m ")
    quit
elif answer == "scientist":
    print ("You became a good Scientist and built a Time-Machine.")

answer = input ("Go in the 2050 BC or 2050 AC ? enter AC or BC: ").lower()
while answer != "ac" and answer != "bc":
    answer = input ("Enter 'AC' or 'BC' this time: ").lower()

if answer == "bc":
    answer = input ("Welcome in the year 2050 BC, you saw a stranger walking towards you. Enter 'Meet him' to meet him and 'Run' to run: ").lower()
    while answer!= "meet him" and answer!= "run":
        answer = input ("Enter 'Meet him' or 'Run' this time: ").lower()

    if answer == "meet him":
        print ("The stranger thought you are a threat, he called the guards and they took you.")
        answer = input ("They asked you to help them build the pyramids. Enter 'Help' to help them and 'Run' to run: ").lower()
        while answer!= "help" and answer!= "run":
            answer = input ("Enter 'Help' or 'Run' this time: ").lower()
        if answer == "help":
            print ("\033[91mYou helped them and afterwards they killed you.GAME OVER\033[0m")
        elif answer == "run":
            print ("\033[91mYou tried to run and they killed you.GAME OVER\033[0m")
    elif answer == "run":
        print("\033[91mYou tried to run and they killed you.GAME OVER\033[0m")
    
elif answer == "ac":
    answer = input ("You came in the future. They knew you because you invented the Time-Machine. They asked if you want to go home or live here? Home/Live: ").lower()
    while answer!= "home" and answer!= "live":
        answer = input ("Enter 'Home' or 'Live' this time: ").lower()
    if answer == "live":
        print ("\033[92mYou lived happily ever after.Congrats! YOU WOONNNNN\033[0m")
    elif answer == "home":
        print ("\033[91mYou got back home and became ill and died.GAME OVER\033[0m")


    
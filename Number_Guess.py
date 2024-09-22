import random 

top_of_range = input ("\033[1mEnter a number: \033[0m")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print ("Enter a number larger than 0 next time")
        quit()
else:
    print ("Type a NUMBER next time")
    quit()
random_num = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses = guesses +1
    user_guess =  input ("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print ("Type a NUMBER next time")
        continue
    if user_guess > random_num:
        print ("\033[91mWrong! You guessed too HIGH\033[0m")
    elif user_guess < random_num:
        print ("\033[91mWrong! You guessed too LOW\033[0m")
    else:
        print ("\033[96mYou guessed Correct!\033[0m")
        break
print ("You Got it in "+ str(guesses) + " guesses")
import random
import time

hmq= input("How many \033[1mQUESTIONS\033[0m you want? ")
hmq = int(hmq)
print("\nYour TIME starts now!")

OPERAND = ["+", "-", "*"]
min_operand = 3
max_operand = 10

def gen_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(OPERAND)

    expr = str(left) +" "+operator +" "+str(right)
    answer = eval(expr)
    return expr, answer

start_time = time.time()


score = 0
for i in range(hmq):
    expr, answer = gen_problem()
    while True:
        guess = input("Problem #"+ str(i + 1) +":  " + expr + " = ")
        if guess == str(answer):
            score+=1
            print("\033[96mYou guessed CORRECT!!!\033[0m")
            break
        else:
            print("\033[91mYou guessed WRONG!!!\033[0m")
            break

end_time = time.time()
total_time = round(end_time - start_time,2)

print ("\033[96mYoy got \033[0m"+str(score)+" \033[96mQuestions CORRECRT!!!\033[0m OUT OF "+str(hmq)+ " in "+str(total_time)+" seconds!")
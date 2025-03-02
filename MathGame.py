import random
import time



operators = ["+", "-", "*", "/"]

min_operand = 3

max_operand = 12

total_problems = 10

score = 5



input('Press Enter to Begin ')
print('----------------------------------------')
start_time = time.time()

def generate_problem():
    global first_try
    first_try = 0
    global score
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)
    while True:
        expr = str(left) + ' ' +  operator + ' ' + str(right)
        if operator == '/' and left % right !=0:
            left = random.randint(min_operand, max_operand)
            right = random.randint(min_operand, max_operand)
            operator = '/'
        else:
            answer = eval(expr)
            return expr, answer

        



for i in range(total_problems):
    expr, answer = generate_problem()
    while True:
        guess = input(f'Problem #{i + 1}: {expr} = ')
        if int(guess) == int(answer):
            break
        elif first_try < 1:
            score -= 1
            first_try += 1

        
        

final_time = time.time()

total_time = round(final_time - start_time, 2)



    
print('----------------------------------------')
print(f'Congrats! Your total time was: {total_time} seconds')
print(f'You got a score of {score}/{total_problems}')

generate_problem()

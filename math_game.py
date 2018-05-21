import math
from random import randint

def getQuestion():
    a = randint(0, 9)
    b = randint(0, 9)
    return "What is {} + {}?: ".format(a, b), a, b

while True:
    question, a, b = getQuestion()
    answer = input(question)
    if answer == str(a + b):
        continue
    else:
        print("You are wrong. Because of it, you have been eaten. Good job.")
        break

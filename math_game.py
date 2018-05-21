import math

def getQuestion():
    return "What is 2 + 2?: "

while True:
    question = getQuestion()
    answer = input(question)
    if answer == str(4):
        continue
    else:
        print("You are wrong  .")
        break

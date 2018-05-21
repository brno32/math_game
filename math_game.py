import math
import time
from random import randint

class Question:
    def __init__(self):
        self.id = randint(0,3)
        self.idMap = ["+", "-", "*", "//"]
        self.a = randint(0, 9)
        self.b = randint(0, 9)

    def getQuestion(self):
        operator = self.idMap[self.id]
        return "What is {} {} {}?: ".format(self.a, operator, self.b)

    def checkInput(self, input):
        if self.id == 0:
            return str(self.a + self.b) == input
        if self.id == 1:
            return str(self.a - self.b) == input
        if self.id == 2:
            return str(self.a * self.b) == input
        if self.id == 3:
            return str(self.a // self.b) == input

count = 0
while True:
    count += 1

    q = Question()
    answer = input(q.getQuestion())
    if q.checkInput(answer):
        if count > 4:
            print("You win!")
            break
        continue
    else:
        print("You are wrong. Because of it, you have been eaten. Good job.")
        break

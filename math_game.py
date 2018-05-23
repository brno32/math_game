import math
import sys
import os
from threading import Thread, Event
from time import time, sleep
from random import randint

TIMEOUT_MESSAGE = "You are too slow and stupid. You are dead."
WRONG_MESSAGE = "You are wrong. Because of it, you have been eaten. Good job."
VICTORY_MESSAGE = "You win! You can do (very) basic math! Hooray!"


class Question:
    """
    Generates a random math question the user is asked to solve
    """
    def __init__(self):
        self.id = randint(0,3)
        self.idMap = ["+", "-", "*", "/"]
        self.a = randint(1, 9)
        self.b = randint(1, 9)

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

def questions(stopFlag):
    count = 0
    while True:
        if not timer_thread.is_alive():
            return
        q = Question()
        answer = input(q.getQuestion())
        if q.checkInput(answer):
            count += 1
            if count > 4:
                print(VICTORY_MESSAGE)
                break
            continue
        else:
            print(WRONG_MESSAGE)
            break
    if not timer_thread.is_alive():
        return
    return

def timer():
    for i in range(15):
        sleep(1)
        if not game.is_alive():
            return
    if game.is_alive():
        # TODO: kill game thread here
        pass
    print(TIMEOUT_MESSAGE)
    return

if __name__ == "__main__":
    stopFlag = Event()
    game = Thread(target=questions, args=(stopFlag,))
    timer_thread = Thread(target=timer)
    timer_thread.start()
    game.start()

    timer_thread.join()
    game.join()

    print('\nExecution ends')

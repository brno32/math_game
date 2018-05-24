import os
from threading import Thread
from time import sleep
from random import randint

DIFFICULTY_MAP = [20, 15, 10]

DIFFICULTY_MESSAGE = """
Please enter:\n
1. for Easy. Timer Set to {} seconds\n
2. for Medium. Timer Set to {} seconds\n
3. for Hard. Timer Set to {} seconds \n
""".format(DIFFICULTY_MAP[0], DIFFICULTY_MAP[1], DIFFICULTY_MAP[2])
TIMEOUT_MESSAGE = "You are too slow and stupid. You are dead."
WRONG_MESSAGE = "You are wrong. Because of it, you have been eaten. Good job."
VICTORY_MESSAGE = "You win! You can do (very) basic math! Hooray!"

LINE_BREAK = '\n'


class Question:
    """
    Generates a random math question the user is asked to solve
    """

    def __init__(self):
        self.id = randint(0, 3)
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


def getDifficulty():
    selection = input(DIFFICULTY_MESSAGE)
    timer_duration = DIFFICULTY_MAP[int(selection) - 1]
    return timer_duration


def questions():
    count = 0
    while timer_thread.is_alive():
        question_obj = Question()
        answer = input(question_obj.getQuestion())
        if question_obj.checkInput(answer):
            count += 1
            if count > 4:
                print(VICTORY_MESSAGE)
                break
            continue
        else:
            print(WRONG_MESSAGE)
            break
    return


def timer(duration):
    for i in range(duration):
        sleep(1)
        if not game.is_alive():
            return
    if game.is_alive():
        print(LINE_BREAK + TIMEOUT_MESSAGE)
        os._exit(0)
    return


if __name__ == "__main__":
    user_selected_diff = getDifficulty()

    game = Thread(target=questions)
    timer_thread = Thread(target=timer, args=(user_selected_diff,))

    timer_thread.start()
    game.start()

    timer_thread.join()
    game.join()

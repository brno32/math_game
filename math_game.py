from threading import Thread
from time import sleep
from random import randint

from constants import (
    DIFFICULTY_MAP, DIFFICULTY_MESSAGE, TIMEOUT_MESSAGE, WRONG_MESSAGE,
    VICTORY_MESSAGE, LINE_BREAK, PLAY_AGAIN_MESSAGE
)


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


def promptForDifficulty():
    while True:
        selection = input(DIFFICULTY_MESSAGE)
        try:
            selection = int(selection)
        except ValueError:
            continue
        # Subtraction makes selection to correspond to array index
        selection = int(selection) - 1
        if selection in range(0, 3):
            timer_duration = DIFFICULTY_MAP[selection]
            return timer_duration


def questions():
    count = 0
    while timer_thread.is_alive():
        question_obj = Question()
        answer = input(question_obj.getQuestion())
        if not timer_thread.is_alive():
            break  # If the timer is up, end the game
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
    while True:
        for i in range(duration):
            sleep(1)
            if not game.is_alive():
                return
        if game.is_alive():
            print(LINE_BREAK + TIMEOUT_MESSAGE)
        return


if __name__ == "__main__":
    while True:
        answer = promptForDifficulty()
        timer_thread = Thread(target=timer, args=(answer,))
        game = Thread(target=questions)

        timer_thread.start()
        game.start()

        timer_thread.join()
        game.join()

        while True:
            reply = input(PLAY_AGAIN_MESSAGE)
            if reply == 'y' or reply == 'n':
                break
            else:
                continue
        if reply == 'y':
            continue
        elif reply == 'n':
            break

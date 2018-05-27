from threading import Thread
from random import randint
from time import sleep

from constants import (
    DIFFICULTY_MAP, DIFFICULTY_MESSAGE, TIMEOUT_MESSAGE,
    WRONG_MESSAGE, VICTORY_MESSAGE, PLAY_AGAIN_MESSAGE,
    CONFIRM_MESSAGE, THANK_YOU_MESSAGE,
)


class Question:
    """
    Generates random math question on instantiation
    Provides instance method to check answer
    """

    def __init__(self):
        self.id = randint(0, 3)
        self.idMap = ["+", "-", "*", "/"]
        self.a = randint(1, 9)
        self.b = randint(1, 9)

    def get_question(self):
        operator = self.idMap[self.id]
        return "What is {} {} {} ?: ".format(self.a, operator, self.b)

    def check_input(self, input):
        if self.id == 0:
            return str(self.a + self.b) == input
        if self.id == 1:
            return str(self.a - self.b) == input
        if self.id == 2:
            return str(self.a * self.b) == input
        if self.id == 3:
            return str(self.a // self.b) == input


def prompt_for_difficulty():
    while True:
        selection = input(DIFFICULTY_MESSAGE)
        try:
            selection = int(selection)
        except ValueError:
            print('Please enter a real answer')
            sleep(1)
            continue
        # Subtraction makes selection correspond to array index
        selection = int(selection) - 1
        if selection in range(0, 3):
            timer_duration = DIFFICULTY_MAP[selection]
            return timer_duration


def questions():
    count = 0
    while True:
        question_obj = Question()
        answer = input(question_obj.get_question())
        if not timer_thread.is_alive():
            break  # If the timer is up, end the game
        if question_obj.check_input(answer):
            count += 1
            if count > 4:
                print_and_sleep(VICTORY_MESSAGE)
                # TODO: it'd be nice to run input(CONFIRM_MESSAGE)
                # here, but this will also have to trigger some signal
                # to turn off the timer; otherwise, TIMEOUT_MESSAGE
                # might get printed while waiting for user input
                break
            continue
        else:
            print_and_sleep(WRONG_MESSAGE)
            # TODO: dito. see above
            break
    return


def timer(duration):
    while duration > 0:
        sleep(1)
        duration -= 1
        if not game_thread.is_alive():
            return
    if game_thread.is_alive():
        print(TIMEOUT_MESSAGE)
        print(CONFIRM_MESSAGE)
    return

def print_and_sleep(message_to_print):
    print(message_to_print)
    sleep(1)

def ask_to_play_again():
    while True:
        reply = input(PLAY_AGAIN_MESSAGE)
        if reply == 'y' or reply == 'n':
            break
        else:
            continue
    return reply == 'y'


if __name__ == "__main__":
    while True:
        answer = prompt_for_difficulty()
        timer_thread = Thread(target=timer, args=(answer,))
        game_thread = Thread(target=questions)

        timer_thread.start()
        game_thread.start()

        timer_thread.join()
        game_thread.join()

        if ask_to_play_again():
            continue
        break
    print(THANK_YOU_MESSAGE)

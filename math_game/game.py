from threading import Thread
from random import randint
from time import sleep

from math_game.constants import (
    DIFFICULTY_MAP, DIFFICULTY_MESSAGE, TIMEOUT_MESSAGE,
    WRONG_MESSAGE, VICTORY_MESSAGE, PLAY_AGAIN_MESSAGE,
    CONFIRM_MESSAGE,
)


class MathGame:
    """
    Generates series of random math questions
    Provides instance method to check answers
    """

    def __init__(self, difficulty):
        self.id = None
        self.a = None
        self.b = None
        self.idMap = ["+", "-", "*", "/"]
        self.timer_thread = Thread(target=self.timer, args=(difficulty,))
        self.game_thread = Thread(target=self.questions)

    def start_game(self):
        self.timer_thread.start()
        self.game_thread.start()
        self.timer_thread.join()
        self.game_thread.join()

    def randomize(self):
        self.id = randint(0, 3)
        self.a = randint(1, 9)
        self.b = randint(1, 9)

    def get_question(self):
        operator = self.idMap[self.id]
        return "What is {} {} {}?: ".format(self.a, operator, self.b)

    def check_input(self, input):
        if self.id == 0:
            return str(self.a + self.b) == input
        if self.id == 1:
            return str(self.a - self.b) == input
        if self.id == 2:
            return str(self.a * self.b) == input
        if self.id == 3:
            return str(self.a // self.b) == input

    def questions(self):
        count = 0
        while True:
            self.randomize()
            answer = input(self.get_question())
            if not self.timer_thread.is_alive():
                break  # If the timer is up, end the game
            if self.check_input(answer):
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

    def timer(self, duration):
        duration = int(duration)
        while duration > 0:
            sleep(1)
            duration -= 1
            if not self.game_thread.is_alive():
                return
        if self.game_thread.is_alive():
            print(TIMEOUT_MESSAGE)
            print(CONFIRM_MESSAGE)
        return


def print_and_sleep(message_to_print):
    print(message_to_print)
    sleep(1)


def ask_to_play_again():
    while True:
        reply = input(PLAY_AGAIN_MESSAGE)
        reply = reply.lower()
        if reply == 'y' or reply == 'n':
            break
        else:
            continue
    return reply == 'y'


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

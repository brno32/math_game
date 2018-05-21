import math
import time
from random import randint

# Constants
# TIME = 30  # Global which stores the time the player has

class Question:
    """
    Generates a random math question the user is asked to solve
    """
    def __init__(self):
        self.id = randint(0,3)
        self.idMap = ["+", "-", "*", "/"]
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

def get_time_stamp():
    return int(time.time())

def main():
    TIME = 15
    count = 0
    while True:
        q = Question()
        then = get_time_stamp()
        answer = input(q.getQuestion())
        now = get_time_stamp()
        if q.checkInput(answer):
            elapsed = now - then
            TIME = TIME - elapsed
            if TIME > 0:
                count += 1
                TIME = TIME + 5
                if count > 4:
                    print("You win!")
                    break
                continue
            else:
                print("You are too slow and stupid. You are dead.")
                break
        else:
            print("You are wrong. Because of it, you have been eaten. Good job.")
            break

if __name__ == "__main__":
    main()

from math_game.constants import THANK_YOU_MESSAGE

from math_game.game import (
    MathGame, prompt_for_difficulty, ask_to_play_again
)

if __name__ == "__main__":
    while True:
        difficulty = prompt_for_difficulty()

        game_obj = MathGame(difficulty)
        game_obj.start_game()

        if ask_to_play_again():
            continue
        break
    print(THANK_YOU_MESSAGE)

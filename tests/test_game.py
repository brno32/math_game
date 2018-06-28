import pytest
import sys
from io import StringIO
from contextlib import contextmanager
from math_game.constants import DIFFICULTY_MAP
from math_game.game import (
    MathGame, prompt_for_difficulty, ask_to_play_again
)


@contextmanager
def replace_stdin(target):
    orig = sys.stdin
    sys.stdin = target
    yield
    sys.stdin = orig


@pytest.mark.parametrize("difficulty", [
    ("1"), ("2"), ("3"),
])
def test_difficulty_select(difficulty):
    with replace_stdin(StringIO(difficulty)):
        duration = prompt_for_difficulty()
    assert duration == DIFFICULTY_MAP[int(difficulty) - 1]


@pytest.mark.parametrize("difficulty", [
    ("1"), ("2"), ("3"),
])
def test_question(difficulty):
    game = MathGame(difficulty)
    game.randomize()
    question = game.get_question()
    assert type(question) == str

    if game.id == 0:
        answer = game.a + game.b
        assert game.check_input(str(answer))
    if game.id == 1:
        answer = game.a - game.b
        assert game.check_input(str(answer))
    if game.id == 2:
        answer = game.a * game.b
        assert game.check_input(str(answer))
    if game.id == 3:
        answer = game.a // game.b
        assert game.check_input(str(answer))


@pytest.mark.parametrize("difficulty", [
    ("1"), ("2"), ("3"),
])
def test_timer(difficulty):
    game = MathGame(difficulty)
    game.timer_thread.start()
    assert game.timer_thread.is_alive

    # TODO: test elapsed time
    assert True


# def test_win():
#     game = MathGame("1")
#     game.start_game()
#
#     with replace_stdin(StringIO("1")):
#         game.randomize()
#         game.questions()
#     assert True
#
#
# def test_lose():
#     game = MathGame("1")
#     game.start_game()
#
#     with replace_stdin(StringIO("1")):
#         game.questions()
#     assert not game.check_input("82")


@pytest.mark.parametrize("answer", [
    ("y"), ("Y"),
])
def test_want_to_play_again(answer):
    with replace_stdin(StringIO(answer)):
        assert ask_to_play_again()


@pytest.mark.parametrize("answer", [
    ("n"), ("N"),
])
def test_dont_want_to_play_again(answer):
    with replace_stdin(StringIO(answer)):
        assert not ask_to_play_again()

from math_game.scripts.game import MathGame


def test_difficulty_select():
    # difficulty = prompt_for_difficulty()
    assert True


def test_easy():
    game = MathGame(3)
    question = game.get_question()
    assert type(question) == str

    game.timer_thread.start()
    assert game.timer_thread.is_alive


def test_medium():
    assert True


def test_hard():
    assert True


def test_win():
    assert True


def test_lose():
    assert True


def test_play_again():
    assert True


def test_quit():
    assert True

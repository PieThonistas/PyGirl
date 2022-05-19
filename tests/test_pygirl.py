from genericpath import exists
import pytest
from api.pygirl import start_game, get_guesses_left, get_incorrect_guesses, get_word_in_progress, game_turn

def test_start_game_exists():
    assert start_game

def test_class_exists():
    assert game_turn


def test_starts_game():
    value = start_game()['id']
    value2 = start_game()['status']
    expected = 1
    status = "start"
    print(value)
    assert value == expected
    assert value2 == status

#TODO: edgecase testing

def test_starts():
    value = start_game()['guesses']
    expected = 0
    assert value != expected

# def test_no_more_word():
#     value = get_incorrect_guesses[id_,"q", used]
#     letter_guessed = "q"
#     letter_guessed = "w"
#     letter_guessed = "z"
#     letter_guessed = "x"
#     letter_guessed = "q"
#     letter_guessed = "x"
#     expected = 0
#     assert value != expected


# def test_game_data():
#     TODO:test game_data when all code is completed
#     id_ = game_data["id"]
#     unsolved_word = game_data["working_word"]
#     status = game_data["status"]
#     guesses = game_data["guesses"]
#     value = Game.welcome_message("y")
#     expected = "Let's play!"
#     assert value == expected

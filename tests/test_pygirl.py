from genericpath import exists
import pytest
from api.pygirl import start_game, get_guesses_left, get_incorrect_guesses, get_word_in_progress, game_turn, is_correct_letter

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

def test_starts_guesses_empty():
    value = start_game()['guesses']
    expected = ""
    assert value == expected

def test_guess_incorrect():
    value = is_correct_letter(1, "y")
    expected = False
    assert value == expected

def test_guess_correct():
    value = is_correct_letter(1, "c")
    expected = True
    assert value == expected

def test_guess_correct():
    # guesses of none, pass in 1, f, _ _ _ _
    value = is_correct_letter(1, "c")
    expected = True
    assert value == expected

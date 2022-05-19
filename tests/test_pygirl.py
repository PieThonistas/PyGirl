import pytest
from api.backend import Game


def test_class_exists():
    assert Game


def test_function_exists():
    assert Game.welcome_message


def test_input():
    value = Game.welcome_message("y")
    expected = "Let's play!"
    assert value == expected

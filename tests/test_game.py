import pytest
from main_game.game import Game
# from main_game.game import welcome_message

def test_class_exists():
  assert Game

def test_function_exists():
  assert Game.welcome_message

def test_input():
  value = Game.welcome_message("y")
  expected = "Let's play!"
  assert value == expected
import sys
from http.server import BaseHTTPRequestHandler
from urllib import parse

# import requests
from collections import Counter
import random


words = {
            1: "function",
            2: "lambda",
            3: "methods",
            4: "tuple",
            5: "bumbershoot",
            6: "tree",
            7: "recursion",
            8: "class",
            9: "object",
            10: "stack",
            11: "queue",
            12: "kaggle",
            13: "jupyter",
            14: "pandas",
            15: "enqueue",
            16: "dequeue",
            17: "serverless",
            18: "automation",
            19: "init",
            20: "exception",
        }

'''

Guess a letter or solve the word

_ _ _ _ _

Incorrect guesses: 
Guesses left: 6
'''

'''
Game 1

Correct!
Guess a letter or solve the word

f _ _ _ _ _ _ _

Incorrect guesses: 
Guesses left: 6
'''
# add underscore to ids
def game_turn(id, guessed_letter, used_letters):
  output = f"Game {id}"
  correct = is_correct_letter(id, guessed_letter)
  if correct:
    output += "\nYou're correct!"
  else:
    output += "\nloser"
  # word_in_progress = get_word_in_progress()
  # incorrect_guesses = get_incorrect_guesses()
  # guesses_left = get_guesses_left()
  return output


def get_word_in_progress():
  message = ""
  for character in word:
    if character in letters:
        message += f"{character} "

def get_incorrect_guesses():
  pass

def get_guesses_left():
  pass

def is_correct_letter(id, guessed_letter):
  word = words[id]
  if guessed_letter in word:
    return True
  else:
    return False

def start_game():

  id = 1
  word = words[id]
  unsolved_word = ""
  for character in word:
    unsolved_word += "_ "
  tries_left = 6
  return f''' Game {id}

Guess a letter or solve the word

{unsolved_word}

Incorrect guesses: 
Guesses left: {tries_left}
'''

'''
PyGirl.com/?id=1&letter=p&incorrect=lx
'''

if __name__ == "__main__":
   response = game_turn(1, "x", "")
   print(response)





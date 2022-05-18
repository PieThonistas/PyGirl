from mimetypes import guess_all_extensions
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
def game_turn(id_, guessed_letter, wrong_letters, guess_attempts=0):
  #TODO: figureout how to update game_id instead of idx for library
  #TODO: attempts left counter is not working
  #TODO: word spaces _ _ _
  #TODO: wrong letters not tracking 
  #TODO: word displays first letter all the time

  output = f"Game {id_}"
  correct = is_correct_letter(id_, guessed_letter)
  if correct:
    output += "\nYou're correct! \n"
  else:
    output += "\n You've guessed an incorrect letter, \n Try Again! \n"

  word_in_progress = get_word_in_progress(id_, wrong_letters)
  wrong_guesses = get_incorrect_guesses(id_, guessed_letter, wrong_letters)
  guesses_left = get_guesses_left(id_, wrong_letters)

  return output + word_in_progress + wrong_guesses + guesses_left


def is_correct_letter(id_, guessed_letter):
  #is the letter they guessed in the word to solve
  word = words[id_]
  if guessed_letter in word:
    return True
  else:
    return False


def get_word_in_progress(id_, guessed_letter):
  # show the correctly guessed letters in the word
  word = words[id_]
  message = ""
  for guessed_letter in word:
    if guessed_letter in word:
      message += f"{guessed_letter}"
    else:
      message += "_ "
    return f"{message}\n" 

def get_incorrect_guesses(id_, guessed_letter, wrong_letters):
  # tracks incorrect letters
  word = words[id_]
  wrong_letters = ""
  message = ""
  for character in guessed_letter:
    if character not in word:
      message += f"{character} "
      message += wrong_letters
  return message + wrong_letters

def get_guesses_left(id_, guessed_letter):
  # counter for # of attempts minus incorrect guesses
  max_attempts = 10
  word = words[id_]
  counter = 0
  guesses_left = 0
  for character in guessed_letter:
    if character not in word:
      counter += 1
  guesses_left = max_attempts - counter

  return f" Attempts left: {guesses_left}"
    

def start_game(id_, guessed_letter):
  #initiates first round
  id_ = 1
  word = words[id]
  unsolved_word = ""
  for guessed_letter in word:
    unsolved_word += "_ "
  tries_left = 6
  return f''' Game {id_}

Guess a letter or solve the word

{unsolved_word}

Incorrect guesses: ***

Guesses left: {tries_left}
'''


#possible link
'''
PyGirl.com/?id_=1&letter=p&incorrect=lx
'''

#runs game
if __name__ == "__main__":
   response = game_turn(id_=3, guessed_letter="y", wrong_letters="", guess_attempts="")
   print(response)



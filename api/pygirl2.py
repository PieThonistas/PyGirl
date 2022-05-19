from mimetypes import guess_all_extensions
import sys
from http.server import BaseHTTPRequestHandler
from turtle import position
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
def game_turn(id_, guessed_letter, used_letters):
  #TODO: figure out how to update game_id instead of idx for library
  #TODO: id_ needs to be setup to randomize number from 1-20 at game initiation

  output = f"\nGame {id_}\n"
  correct = is_correct_letter(id_, guessed_letter)
 
  if correct:
    output += "\nYou're correct! \n\n"
  else:
    output += "\n You've guessed an incorrect letter. \n Try Again! \n\n"

  word_in_progress = get_word_in_progress(id_, guessed_letter, used_letters)

  wrong_guesses = get_incorrect_guesses(id_, guessed_letter, used_letters)

  guesses_left = get_guesses_left(id_, guessed_letter)

  return output + word_in_progress + wrong_guesses + guesses_left


def is_correct_letter(id_, guessed_letter):
  #is the letter they guessed in the word to solve
  word = words[id_]
  if guessed_letter in word:
    return True
  else:
    return False


def get_word_in_progress(id_, guessed_letter, used_letters):
  # show the correctly guessed letters in the word
  word = words[id_]
  message=""

  for character in word:
    if character == guessed_letter or character in used_letters:
      message += f"{character} "
    else:
      message += "_ "

  return f"{message} \n" 



def get_incorrect_guesses(id_, guessed_letter, used_letters):
  # tracks incorrect letters
  word = words[id_]
  used_letters = ""
  message = ""
  for character in guessed_letter:
    if character not in word:
      message += f"\nGuessed Letters: {character} \n "
      message += used_letters
  return message + used_letters


def get_guesses_left(id_, guessed_letter):
  counter = 0
  word = words[id_]
  max_attempts = 10
  guesses_left = 0

  if guessed_letter not in word:
      counter += 1

  guesses_left = max_attempts - counter
  return f" \nAttempts left: {guesses_left} \n"
    

def start_game(id_, guessed_letter):
  #initiates first round
  id_ = 1
  word = words[id_]
  unsolved_word = ""
  for guessed_letter in word:
    unsolved_word += "_ "
  tries_left = 6
  return f''' 
Game {id_}

Guess a letter or solve the word

{unsolved_word}

Incorrect guesses: ***

Guesses left: {tries_left}
'''


#possible link
'''
PyGirl.com/?id_=1&letter=p&incorrect=lx
'''

#runs game methods
if __name__ == "__main__":
    turn0 = start_game(id_="", guessed_letter="")
    print(turn0)

    turn1 = game_turn(id_=3, guessed_letter="m", used_letters="")
    print(turn1)

    turn2 = game_turn(id_=3, guessed_letter="e", used_letters="m")
    print(turn2)


import sys
from http.server import BaseHTTPRequestHandler
import urllib import parse
import requests
from collections import Counter
import random

# sms text to user prompting a weclome messages and asking if they'd like to play a game of PyGirl
# y to play
# q to not play


class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    s = self.path
    url_components = parse.urlsplit(s)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)

    name = dic.get("id: 2")




# class Game:
#   print("hello")

#   def __init__(self):
#     pass

#   def welcome_message(self):
#     # the user_answer starts the game; at the beginning the user doesn't guess.
#     print("Welcome to PyGirl! Want to play a word game?")
#     response = input("(y)es to play or (n)o to decline")
#     response.toLowerCase 
#     if response == "n":
#       print("Maybe next time!")
#       sys.exit()
#     if response == "y":
#       print("Let's play!")
#     # some functionality to begin game
    
#   def yes_to_play(self):
#     # user_answer = "y"
#     # randomize
#     pass
    
# if __name__ == "__main__":
#     game = Game()
#     game.welcome_message()
#     game.yes_to_play() 



# # this is the answer we're looking for
# correct_answer = "PYTHON"
# # this is the number of tries left. Wrong letters.
# remaining_tries = 10
# # state of the game at the beginning
# game_state = "IN PROGRESS"
# while user_answer != correct_answer:
#     # ask the user for another letter
#     if guess not in correct_answer:
#         remaining_tries = remaining_tries -1
#     else:
#         # update user_answer so it includes the correct letter guess
# otherwise:
#     if user_answer == correct_answer:
#         game over
#         game_state = "YOU WIN"
#     if the snake is complete:
#         game over
#         game_state = "YOU LOSE"
# if game_state != "IN PROGRESS":
#     game over --> user or pygirl won or loss
#         # go back to main menu (start another game, quit)
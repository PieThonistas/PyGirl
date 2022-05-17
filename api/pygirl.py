import sys
from http.server import BaseHTTPRequestHandler
from urllib import parse

# import requests
from collections import Counter
import random

# sms text to user prompting a welcome messages and asking if they'd like to play a game of PyGirl
# y to play
# q to not play

questions = {
    "1": {"id": "1", "text": "_ _ _ _ _", "solution": "doozy"},
    "2": {"id": "2", "text": "_ _ _ _ _", "solution": "yitten"},
}


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        # get initial query by targeting http:../pygirl/user-response
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        id = dic["id"]
        message = str(questions[id])
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(message.encode())

        # name = dic.get("id: 2")
        # does dict.get id:2 exist if so, yes, otherwise no
        # serverless function cannot have a counter, but you can incorporate counter here
        # incorporate Vercel and Twillio
        # make a request
        # wait for a response
        # respond
        # can have a URL for each turn, response, and game status


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


class Game:
    def __init__(self):
        self.questions = {
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
        self.definition = {
            1: "function definition",
            2: "lambda definition",
            3: "methods definition",
            4: "tuple definition",
            5: "bumbershoot definition",
            6: "tree definition",
            7: "recursion definition",
            8: "class definition",
            9: "object definition",
            10: "stack definition",
            11: "queue definition",
            12: "kaggle definition",
            13: "jupyter definition",
            14: "pandas definition",
            15: "enqueue definition",
            16: "dequeue definition",
            17: "serverless definition",
            18: "automation definition",
            19: "init definition",
            20: "exception definition",
        }
        self.attempts_allowed = 6
        self.failed_attempts = 0

    def show_word_so_far(self, word, letters):
        # show the correctly guessed letters in the word
        message = ""
        for character in word:
            if character in letters:
                message += f"{character} "
            # this part addes the underscore for the blank letters
            else:
                message += "_ "
        return message

    # this checks if they have enough words to win the game
    def check_for_win(self, word, letters):
        # show the correctly guessed letters in the word
        correct_count = 0
        for character in word:
            if character in letters:
                correct_count += 1
        if correct_count == len(word):
            return True
        else:
            return False

    def play(self):
        # prompt to see if they want to play
        print("Do you want to play a game?")
        # I don't know how to do this for the serverless function. We can change this to make it work.
        response = input("> ")
        if response != "y":
            print("Have a nice day!")
            return
        # pick random word. Their guess must be 1 letter long.
        id = random.randint(1, len(self.questions))
        word = self.questions[id]
        # print(f"it's a secret: {word}")
        letters = set()
        # while game loop
        while True:
            response = input("What is your guess? >")
            # validate user input. Their guess must be 1 letter long.
            while len(response) != 1:
                response = input("Invalid input. What is your guess? >")
            letters.add(response)
            if response in word:
                # congratulate and show current progress
                print(
                    f"Yay! You got one. Your progress so far: { self.show_word_so_far(word, letters) }"
                )
                # if word is complete, end game
                if self.check_for_win(word, letters):
                    print(
                        "Way to go! You won! The definition of + {id} is {self.definition[id]}"
                    )
                    return
            else:
                # admonish and show attempts remaining
                self.failed_attempts += 1
                # I need to figure out how to keep this message from printing when they get down to zero guesses remaining; show show that they lost if they get down to zero.
                print(
                    f"Sorry but you cannot pass go at this time. {self.attempts_allowed - self.failed_attempts} guesses remaining. Your progress so far: { self.show_word_so_far(word, letters) }"
                )
                if self.failed_attempts >= self.attempts_allowed:
                    # This is a Transformers reference XD
                    print(
                        "You've failed me for the last time Starscream! The definition of + {id} is {self.definition[id]}"
                    )
                    return


g = Game()
g.play()

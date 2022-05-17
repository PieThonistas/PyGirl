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
        self.definitions = {
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

    def show_snake(self, wrong_guesses):
        snake_imgs = [
            '''
        "xxxx -=: xxxxx"''',
            """
                        ________
                xxxx -=:___________  xxxxx""",
            """
                        ________/   /
                xxxx -=:___________/ xxxxx""",
            """
                       \\
                        \    /
                ________/   /
        xxxx -=:___________/ xxxxx""",
            """
                         _____
                       /  0 0 \\
                       \\
                        \    /
                ________/   /
        xxxx -=:___________/ xxxxx""",
            """
                         _____
                       /  0 0 \\
                       \    --------<
                        \    /
                ________/   /
        xxxx -=:___________/ xxxxx
        """,
        ]
        print(snake_imgs[wrong_guesses])

    def show_pygirl(self, wrong_guesses):
        pygirl_img = [
            """
            "%%%"
           %(-_-)%
            /) )Z
             / \"
           """,
        ]

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
        print(self.show_word_so_far(word, set()))
        # print(f"it's a secret: {word}")
        letters = set()
        # while game loop
        while True:
            response = input("\n What is your guess? >")
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
                        f"Way to go! You won! The definition of {self.questions[id]} is {self.definitions[id]}"
                    )
                    return
            else:
                # admonish and show attempts remaining
                self.failed_attempts += 1
                # I need to figure out how to keep this message from printing when they get down to zero guesses remaining; show show that they lost if they get down to zero.

                if self.failed_attempts >= self.attempts_allowed:
                    # This is a Transformers reference XD
                    print(
                        f"You've failed me for the last time Starscream! The definition of {self.questions[id]} is {self.definitions[id]}"
                    )
                    return
                else:
                    self.show_snake(self.failed_attempts)
                    print(
                        f"Sorry but you cannot pass go this time. {self.attempts_allowed - self.failed_attempts} guesses remaining. Your progress so far: { self.show_word_so_far(word, letters) }"
                    )

    def game_state(incorrect_answers):
        if incorrect_answers == 1:
            print


g = Game()
g.play()

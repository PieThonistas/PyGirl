from http.server import BaseHTTPRequestHandler
from traceback import format_exc
from urllib import parse
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

"""

Guess a letter or solve the word

_ _ _ _ _

Incorrect guesses: 
Guesses left: 6
"""

"""
Game 1

Correct!
Guess a letter or solve the word

f _ _ _ _ _ _ _

Incorrect guesses: 
Guesses left: 6
"""


def game_turn(id_, guessed_letter, used_letters):
    game_data = {
        "id": id_,
    }

    correct = is_correct_letter(id_, guessed_letter)

    if correct:
        game_data["status"] = "correct"
    else:
        game_data["status"] = "incorrect"

    game_data["working_word"] = get_word_in_progress(id_, guessed_letter, used_letters)

    game_data["guesses"] = used_letters + guessed_letter

    return game_data


def is_correct_letter(id_, guessed_letter):
    # is the letter they guessed in the word to solve
    word = words[id_]
    if guessed_letter in word:
        return True
    else:
        return False


def get_word_in_progress(id_, guessed_letter, used_letters):
    # show the correctly guessed letters in the word
    word = words[id_]
    message = ""

    for character in word:
        if character == guessed_letter or character in used_letters:
            message += f"{character} "
        else:
            message += "_ "

    return f"{message} \n"

def get_snake_image(id_, used_letters):
        snakes = [
            "xxxx -=: xxxxx",
            """        ________
                xxxx -=:___________  xxxxx""",
            """         ________/   /
                xxxx -=:___________/ xxxxx""",
            """
                    \\
                        \    /
                ________/   /
        xxxx -=:___________/ xxxxx""",
            """        _____
                    /  0 0 \\
                    \\
                        \    /
                ________/   /
        xxxx -=:___________/ xxxxx
        """,
            """        _____
                     /  0 0 \\
                    \    --------<
                        \    /
                ________/   /
        xxxx -=:___________/ xxxxx
        """
        ]
        incorrect = get_incorrect_count(id_, used_letters)
        if incorrect > 0:
            return f"\n\n{snakes[incorrect - 1]}\n\n"
        else:
            return ""
       
def get_incorrect_count(id_, used_letters):
        word = words[id_]
        counter = 0
        for letter in used_letters:
            if not letter in word:
                counter += 1
        return counter


def get_incorrect_guesses(id_, guessed_letter, used_letters):
    # tracks incorrect letters
    word = words[id_]
    used_letters = ""
    message = ""
    for character in guessed_letter:
        if character not in word:
            message += f"\nGuessed Letters: {character} \n "
            message += used_letters
        else:
            if character in word:
                message += f"\nGuessed Letters: {used_letters} \n "
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


def is_game_won(game_data):
    word = words[game_data["id"]]
    for character in word:
        if not character in game_data["guesses"]:
            return False
    return True


def is_game_lost(game_data):
    word = words[game_data["id"]]
    max_attempts = 10
    incorrect_counter = 0
    guesses = game_data["guesses"]
    for character in guesses:
        if not character in word:
            incorrect_counter += 1
    if incorrect_counter >= max_attempts:
        return True
    else:
        return False


def start_game():
    id_ = random.randint(1, len(words))
    game_data = {}
    game_data["id"] = id_
    game_data["status"] = "start"
    game_data["guesses"] = ""
    word = words[id_]
    unsolved_word = ""
    for character in word:
        unsolved_word += "_ "
    game_data["working_word"] = unsolved_word

    return game_data


# Guess a letter or solve the word

# {unsolved_word}

# Incorrect guesses: ***

# Guesses left: {tries_left}

# if __name__ == "__main__":
#     start = get_incorrect_count(1, "m")
#     print(start)
    # turn0 = start_game(id_="", guessed_letter="")
    # print(turn0)

    # turn1 = game_turn(id_=3, guessed_letter="y", used_letters="")
    # print(turn1)

    # turn2 = game_turn(id_=3, guessed_letter="e", used_letters="m")
    # print(turn2)

# test_game_data = {"id": 1, "status": "start", "guesses": "function"}

# print(is_game_won(test_game_data))  # should return true

# test_game_data = {"id": 1, "status": "start", "guesses": "wrong"}

# print(is_game_won(test_game_data))  # should return false

# test_game_data = {"id": 1, "status": "start", "guesses": "abcde"}

# print(is_game_lost(test_game_data))  # should return false

# test_game_data = {"id": 1, "status": "start", "guesses": "abdeghklmp"}

# print(is_game_lost(test_game_data))  # should return true
print(get_snake_image(1, "abcdefg"))

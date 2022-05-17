from http.server import BaseHTTPRequestHandler
from urllib import parse

# from pygirl import pygirl


# class handler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         s = self.path
#         url_components = parse.urlsplit(s)
#         # get initial query by targeting http:../pygirl/user-response
#         query_string_list = parse.parse_qsl(url_components.query)
#         dic = dict(query_string_list)
#         id = dic["id"]
#         message = str(questions[id])
#         self.send_response(200)
#         self.send_header("Content-type", "application/json")
#         self.end_headers()
#         self.wfile.write(message.encode())


# user responds if they want to play
# user's response will stored
# logic to determine if they response is correct
# if response is correct prompt for another guess
# if respone is incorrect build snake and alk for another guess
# if user has 2 guesses left prompt to ask if they want a defintion
# a way to account for the user knows the word and has nearly all tries left

# g to guess the word
# d for definition
# q to quit

user_answer = "n"
# with open("assets/library.txt") as library:
#     words = library.read()

questions = {
        1: {"id": 1, "text": "_ _ _ _ _ _ _ _", "solution": "function"},
        2: {"id": 2, "text": "_ _ _ _ _ _", "solution": "lambda"},
        3: {"id": 3, "text": "_ _ _ _ _ _ _", "solution": "methods"},
        4: {"id": 4, "text": "_ _ _ _ _", "solution": "tuple"},
        5: {"id": 5, "text": "_ _ _ _ _ _ _ _ _ _ _", "solution": "bumbershoot"}
}
#
# word = questions[1]["solution"]
# split_word = enumerate(word)
# print(*split_word)
# for i in enumerate(word):
#     if i == user_answer:
#         print("you are right!!")
#     else:
#         print("Wrong!")


def user_response(user_answer_):
    remaining_tries = 8
    bad_guesses = ""
    correct_answer = questions[1]['solution']
    # if user_answer_ != correct_answer:
    if user_answer_ in split_word:
        bad_guesses += user_answer_
        print("you're wrong")
        remaining_tries -= 1
        print(f"You have {remaining_tries} remaining tries.")
    else:
        correct_guesses = ""
        correct_guesses += user_answer_
        print("you're right. You guessed a correct letter.")


user_response(user_answer)

# s = input('Enter a string to see if strings are repeated: ')
#     d = dict()
#     p = s.split()
#     word = ','
#     for word in p:
#         if word not in d:
#             d[word] = 1
#         else:
#             d[word] += 1
#     print (d)


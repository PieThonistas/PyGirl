from http.server import BaseHTTPRequestHandler
from urllib import parse

# from pygirl import pygirl


# questions = {
#     "1": {"id": "1", "text": "_ _ _ _ _", "solution": "doozy"},
#     "2": {"id": "2", "text": "_ _ _ _ _", "solution": "yitten"},
# }


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
user_answer = ""
correct_answer = "doozy"


def user_response(user_answer):
    remaining_tries = 8
    if user_answer != correct_answer:
        print("you're wrong")
        remaining_tries -= 1
        print(f"You have {remaining_tries} remaining tries.")


user_response(user_answer)

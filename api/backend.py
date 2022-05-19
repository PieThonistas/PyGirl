
# from http.server import BaseHTTPRequestHandler
from pyodide.http import pyFetch
import asyncio
import string

pyscript = pyscript

prompts = {
    "Start": "Guess a letter to solve the word",
    "Incorrect": "Wrong!! Guess again!",
    "Correct": "Good job! Keep it up",
    "Winner": "Smarty pants!! Good work!",
    "Defeat": "Better luck next time"
}

url = "https://py-girl-self.vercel.app/api/pygirl"
game_data = None

async def fetch_game_data(query_string=""):
    global game_data

    game_data = await pyfetch(url=url + query_string + method="GET").json()
    id_ = game_data["id"]
    status = game_data["status"]
    guesses = game_data["guesses"]
    word = game_data["word_id"]
    unsolved_word = game_data["unsolved_word"]
    working_word = game_data




# class handler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         s = self.path
#         url_components = parse.urlsplit(s)
#         query_string_list = parse.parse_qsl(url_components.query)
#         dic = dict(query_string_list)
#
#         if not dic.get("id_"):
#             message = start_game()
#         else:
#             id = int(dic["id_"])
#             guessed_letter = dic["guessed_letter"]
#             used_letters = dic["used_letters"]
#             message = game_turn(id, guessed_letter, used_letters)
#
#         self.send_response(200)
#         self.send_header("Content-type", "text/plain")
#         self.end_headers()
#         self.wfile.write(message.encode())

from http.server import BaseHTTPRequestHandler
from urllib import parse
from api.pygirl import start_game, game_turn
import json


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if not dic.get("id"):
            game_data = start_game()
        else:
            id = int(dic["id"])
            guessed_letter = dic["guessed_letter"]
            used_letters = dic["used_letters"]
            game_data = game_turn(id, guessed_letter, used_letters)
        message = json.dumps(game_data)
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(message.encode())
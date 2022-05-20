from http.server import BaseHTTPRequestHandler
from urllib import parse
from api.pygirl import start_game, game_turn
import json

# url = "http://localhost:3000/api/backend/"
# url_vercel = "https://py-girl-self.vercel.app/api/backend/"


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if not dic.get("id"):
            game_data = start_game()
        else:
            id_ = int(dic["id"])
            guessed_letter = dic["guess"]
            used_letters = dic["guesses"]
            game_data = game_turn(id_, guessed_letter, used_letters)
        message = json.dumps(game_data)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(message.encode())
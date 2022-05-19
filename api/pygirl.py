from http.server import BaseHTTPRequestHandler
from urllib import parse
from api.pygirl2 import game_turn, start_game


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        # get initial query by targeting http:../pygirl/user-response
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        
        if not dic.get("id_"):
            message=start_game()
        else: 
            id = int(dic["id_"])
            guessed_letter = dic["guessed_letter"]
            used_letters = dic["used_letters"]
            message = game_turn(id,guessed_letter, used_letters)

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())

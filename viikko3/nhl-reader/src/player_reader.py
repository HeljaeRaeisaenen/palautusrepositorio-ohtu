import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.players = []
        #self.url = url
        self.__get_players(url)
    
    def __get_players(self, url):
        response = requests.get(url).json()

        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['team'],
                player_dict['assists'],
                player_dict['goals']
            )

            self.players.append(player)

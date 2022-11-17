class PlayerStats:
    def __init__(self, player_reader):
        self.reader = player_reader

    def top_scorers_by_nationality(self, nationality:str):
        players = []

        for player in filter(lambda p : p.nationality == nationality, self.reader.players):
            players.append(player)

        players.sort(key= lambda x : x.assists+x.goals, reverse=True)

        return players
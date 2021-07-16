
class Tournament:
    description = " ceci est un tournoi d'échec"

    def __init__(self, name, date, place="local", turn_played=4, players_numbers=8, time_control="blitz"):
        """init values of this tournament"""
        self.players = []
        self.name = name
        self.date = date
        self.place = place
        self.turn_played = turn_played
        self.players_numbers = players_numbers
        self.time_control = time_control

    def add_player(self, player):
        """add an player in the players list of this tournament"""
        self.players.append(player)

    def del_player(self, player):
        """del an player in the players list of this tournament"""
        self.players.remove(player)


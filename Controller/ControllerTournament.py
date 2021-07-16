from View.ViewMenu import View
from Models.tournament import Tournament
from Controller.VerificatorInput import Field
from Controller.ControllerPlayer import ControllerPlayer


class ControllerTournament:
    def __init__(self):
        self.view = View()

    def newtournament(self):
        item = Field()
        name = item.stringcheck("name_tournament")
        date = item.datecheck("date_tournament")
        t1 = Tournament(name, date)
        return t1

    def addplayerstournament(self, t1):
        for p in range(2): #(t1.players_numbers):
            control_player = ControllerPlayer()
            player = control_player.newplayer()
            t1.players.append(player)
        print(t1.players)


tournament = ControllerTournament()
t = tournament.newtournament()
tournament.addplayerstournament(t)



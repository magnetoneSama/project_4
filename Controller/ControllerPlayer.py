from Controller.VerificatorInput import Field
from Models.player import Player


class ControllerPlayer:

    def __init__(self):
        self.control = False

    def newplayer(self):
        items = {}
        item = Field()
        items["firstname"] = item.stringcheck("firstname")
        items["lastname"] = item.stringcheck("lastname")
        items["birthday"] = item.datecheck("birthday")
        items["gender"] = item.gendercheck()
        player = Player(items["firstname"],
                        items["lastname"],
                        items["birthday"],
                        items["gender"])
        return player



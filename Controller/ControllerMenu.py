from View.ViewMenu import View


class ControllerMenu:
    """basic control of main menu,basically control main view and first user input"""

    def __init__(self):
        self.value = None
        self.exit = False
        self.view = View()

    def main_menu(self):

        self.view.mainmenu()
        while self.exit is False:
            value = input()

            if value == "1":
                print('choix 1')
            elif value == "2":
                print('choix 2')
            elif value == "3":
                print('choix 3')
            elif value == "4":
                self.exit = True
            else:
                print(self.view.informationmenu("invalide", value))




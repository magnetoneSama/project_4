from datetime import datetime

from View.ViewMenu import View


class Field:

    def __init__(self):
        """init an value with an none argument and an view for user information in method"""
        self.value = None
        self.view = View()

    def datecheck(self, name_view):
        """function for check an date input, check on function and return value input"""
        valid = False
        while valid is False:
            value = input(f"{self.view.informationmenu(name_view)}")
            try:
                datetime.strptime(value, '%d/%m/%Y')
                return value
            except ValueError:
                print(f"{self.view.informationmenu('invalide', value)}")

    def stringcheck(self, name_view, minlenght: int = 2):
        valid = False
        while valid is False:
            value = input(f"{self.view.informationmenu(name_view)}")
            if len(value) >= minlenght:
                print("ça passe")
                return value
            else:
                print(f"{self.view.informationmenu('invalide', value)}")

    def gendercheck(self):
        valid = False
        while valid is False:
            value = input(f"{self.view.informationmenu('gender')}")
            if value in ["h", "H", "f", "F"]:
                return value

            else:
                print(f"{self.view.informationmenu('invalide', value)}")

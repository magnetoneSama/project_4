class View:
    def __init__(self):
        self.active = None

    def mainmenu(self):
        print("[1]Créer un nouveau tournoi")
        print("[2]Ajouter un joueur")
        print("[3]Consulter les  Rapports  ")
        print("[0] quitter le programme")

    def informationmenu(self, name_view, value=None):
        name_views = {"firstname": "Veuillez renseigner votre Prénom:",
                      "lastname": "Veuillez renseigner votre Nom:",
                      "birthday": "Veuillez renseigner votre date de naissance (jj/mm/aaaa) :",
                      "gender": "Veuillez renseigner votre sexe [h]/[f]:",
                      "invalide": f"L'entrée {value} est invalide ",
                      "name_tournament": "Saisissez le nom du tournoi",
                      "date_tournament": "Saisissez la date du tournoi (jj/mm/aaaa)"
                      }

        print(name_views[name_view])

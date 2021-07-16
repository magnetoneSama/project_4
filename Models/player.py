class Player:

    def __init__(self, firstname, lastname, birthday, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.gender = gender
        self.rank = 0

    def add_rank(self, rank_point):
        self.rank += rank_point

    def del_rank(self, rank_point):
        self.rank -= rank_point

# 
import sys

from generala import get_random_dice

class Player():

    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def game_start(self, nplayers):
        pass

    def play(self, dice, players, scoresheets):
        pass

    def notify(self, not_type, message):
        pass

class Game():

    def __init__(self, nscoresheets):
        self.nscoresheets = nscoresheets
        self.players_plugins = []
        self.players = []
        self.scoresheets = []

    def add_player(self, player):
        self.players_plugins.append(player)
        self.players.append(player.name)

    def start(self):
        # plays are:
        # 4
        # 5
        # 6
        # ESCALERA
        # FULL
        # POKER
        # GENERALA
        rounds = self.nscoresheets * 7
        for i in range(rounds):
            for player in self.players:
                self.turn(player)



    def turn(self, player):
        r = get_random_dice(5)
        for i in range(3):
            try:
                roll, decision, scoresheet  = player.play(r, self.players, self.scoresheets)
            except:
                print("Error inesperado:", sys.exc_info()[0])
                # NOTIFY




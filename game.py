# 
import sys
import traceback

from helper import print_scoresheets

from generala import get_random_dice, valid_play, play_value

class Player():#last branching test

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
        self.nplayers = 0
        self.players_plugins = {}
        self.players = []
        self.scoresheets = []
        for i in range(nscoresheets):
            self.scoresheets.append({})

    def add_player(self, player):
        name = player.name()
        self.players_plugins[name] = player
        self.players.append(name)
        for i in range(self.nscoresheets):
            self.scoresheets[i][name] = {}
        self.nplayers = self.nplayers + 1

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

    def results(self):
        print_scoresheets(self.scoresheets)

    def turn(self, player):
        plugin = self.players_plugins[player]
        r = get_random_dice(5)
        nroll = 5
        for i in range(3):
            try:
                bonus = (nroll == 5)
                roll, decision, scoresheet  = plugin.play(i, r, bonus, self.players, self.scoresheets)
                decision = decision.upper() if decision else None
                nroll = len(roll)
                if nroll > 0:
                    r0 = get_random_dice(nroll)
                    i = 0
                    for new_r in roll:
                        r[new_r] = r0[i]
                        i = i+1
                else:
                    if not valid_play(decision):
                        raise Exception('Play [{0}] is invalid'.format(decision))
                    scoresheet = self.scoresheets[scoresheet][player]
                    if decision not in scoresheet:
                        scoresheet[decision] = play_value(decision, r, bonus)
                    else:
                        raise Exception('Decision [{0}] is already taken'.format(decision))
                    break


            except Exception as e:
                print(traceback.format_exc())
                print("Error inesperadamente inesperado: {0}".format(e))
                # NOTIFY




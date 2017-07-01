import traceback

from helper import print_scoresheets
from generala import get_random_dice, valid_play, play_value
"""Library necessary to copy the list "scoresheets" to pass by value to the plugin"""
from copy import deepcopy
"""Libraries necessary for timing the plugin's response"""
import signal
"""Library for displaying the winner"""
import operator
"""Libraries for sandboxing"""
from sandboxing import getPlay#for the sandboxing
TIME_AVAILABLE = 1#time available to compute the plugin's response

class Timeout():
    """Timeout class using ALARM signal."""

    class Timeout(Exception):
        pass

    def __init__(self, sec):
        self.sec = sec

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.raise_timeout)
        signal.alarm(self.sec)

    def __exit__(self, *args):
        signal.alarm(0)  # disable alarm

    def raise_timeout(self, *args):
        raise Timeout.Timeout()


class Player():#

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
        self.players_plugins = {} #the name of the file of the plugins
        self.players = [] #the name() of the plugins
        self.scoresheets = []
        for i in range(nscoresheets):
            self.scoresheets.append({})

    def add_player(self, namePlayer,plugin):
        self.players_plugins[namePlayer] = plugin
        self.players.append(namePlayer)
        for i in range(self.nscoresheets):
            self.scoresheets[i][namePlayer] = {}
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
        """calculating the winner"""
        total = {}
        for player in self.players:
            total[player] = 0
        for scoresheet in self.scoresheets:
            for player in scoresheet:
                for play, score in scoresheet[player].items():
                    total[player] += score
        print "The winner is!:",max(total.iteritems(),key=operator.itemgetter(1))[0]

    def turn(self, player):
        plugin = self.players_plugins[player]#name of the module
        print "turn", plugin
        r = get_random_dice(5)#obtain the dices as a list eg: [2,1,4,4,6]
        nroll = 5
        for i in range(3):#ith opportunity of the current player
            try:
                """It executes the corresponding turn for the plugin with TIME_AVAILABLE seconds to decide"""
                with Timeout(TIME_AVAILABLE):
                    bonus = (nroll == 5)
                    """
                    The return parameters of the play function of the plugin should be: 
                    roll: which dices should be re-rolled referencing the indexes of the r list
                    decision: the final decision of the turn as a string. The avalaible decisions are stated in helper.py
                    scorsheet: which scoresheet should the play be applied
                    """
                    copyScoresheets = deepcopy(self.scoresheets)#make a copy of the scoresheets because we want to send them by value not by reference for safety
                    """getPlay from the sandboxing.py with the parameters
                    plugin: name of the file's plugin eg: serial_dicer.py
                    i: ith opportunity to throw again the dice
                    r: the dices itself
                    bonus: if that throw contains a bonus
                    player: the current players playing the game
                    Scoresheets: the poins currently assigned
                    """
                    roll, decision, scoresheet = getPlay(plugin,i, r, bonus, self.players, copyScoresheets)
                    #roll, decision, scoresheet = plugin.play(i, r, bonus, self.players, copyScoresheets)<--reemplazado
                    decision = decision.upper() if decision else None
                    nroll = len(roll)#how many dices should be re-roll
                    if nroll > 0:#the player has decided re-roll again at least one dice
                        r0 = get_random_dice(nroll)#it obtains "nroll" new dices
                        i = 0
                        for new_r in roll:#it updates the new dices list
                            r[new_r] = r0[i]
                            i = i+1
                    else:#the player has decided that no dice shoul be re-rolled
                        if not valid_play(decision):#the player has not stated a valid play in the format stated in generala.py
                            raise Exception('Play [{0}] is invalid'.format(decision))
                        scoresheet = self.scoresheets[scoresheet][player]#retrieve the plays that player has already played in that scoresheet
                        if decision not in scoresheet:
                            #The player adds a new play in that scoresheet
                            scoresheet[decision] = play_value(decision, r, bonus)
                        else:
                            raise Exception('Decision [{0}] is already taken'.format(decision))
                        break
            except Timeout.Timeout:#Times up for the ith opportunity
                print "Plugin Timeout",plugin
                break
            except Exception as e:
                print(traceback.format_exc())
                print("Error inesperadamente inesperado: {0}".format(e))
                # NOTIFY

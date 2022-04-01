import math
import random


class Player:
    """
    Initiates a player class. Each player in the game will be represented with an X or an O.
    get_move function will allow all players to get their next move.
    """
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self, game):
        pass


class ComputerPlayer(Player):
    """
    Specific kind of player that is going to be managed by the program.
    """
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        pass


class HumanPlayer(Player):
    """
    Specific class for the human player.
    """
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        pass


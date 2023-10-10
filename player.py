import math
import random

class Player:
    def __init__(self, letter):
        #we define a letter x or o
        self.letter = letter

    #we want all players to get their next move given a game
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        #we get a random valid spot for our next move
        square = random.choice(game.availableMoves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        validSquare = False
        val = None
        while not validSquare:
            square = input(self.letter+ '\'s turn. Choose a move (0-8): ')
            #we will check if it s a correct value by casting to an integer
            #if it s not then we say it s invalid
            #or if it s not available on the board, we say it s invalid
            try:
                val = int(square)
                if val not in game.availableMoves():
                    raise ValueError
                validSquare = True
            except ValueError:
                print('Invalid square. Try again')
            return val
                
            
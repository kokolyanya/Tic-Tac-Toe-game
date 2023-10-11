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
            square = input(self.letter+ '\'s turn. Choose a move (1-9): ')
            #we will check if it s a correct value by casting to an integer
            #if it s not then we say it s invalid
            #or if it s not available on the board, we say it s invalid
            try:
                val = int(square)-1
                if val not in game.availableMoves():
                    raise ValueError
                validSquare = True
            except ValueError:
                print('Invalid square. Try again')
            return val

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.availableMoves()) == 9 :
            square = random.choice(game.availableMoves())
        else :
            #get the square based of the minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        maxPlayer = self.letter #you
        otherPlayer = 'X' if player == 'O' else 'O'

        #check if the previous move is the winner
        if state.currentWinner == otherPlayer:
            #we should return position and score because we need to track the score
            return {'position': None,
                'score': 1*(state.numEmptySquares() +1) if otherPlayer == maxPlayer else -1*(state.numEmptySquares() +1)
                }
        
        elif not state.numEmptySquares():
            return {'position': None, 'score': 0 }

        #initialize some dictionaries
        if player == maxPlayer:
            best = {'position': None, 'score': -math.inf}   #each score should maximise
        else:
            best = {'position': None, 'score': math.inf}   #each score should minimise
        
        for possibleMove in state.availableMoves():
            #step 1: make a move and try it
            state.makeMove(possibleMove, player)
            #step 2: recurse using minimax to simulate a game after making that move
            simScore = self.minimax(state, otherPlayer) #we alternate players
            #step 3: undo the move
            state.board[possibleMove] = ' '
            state.currentWinner = None
            simScore['position'] = possibleMove #otherwise this will get messed up from the recursion
            #step 4: update the dictionaries if necessary
            if player == maxPlayer: #we are trying to maximise the maxPlayer
                if simScore['score'] > best['score'] :
                    best = simScore     #replace best
            else:   #but minimise the other player
                if simScore['score'] < best['score'] :
                    best = simScore     #replace best
        
        return best




            
from player import HumanPlayer, RandomComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [ ' ' for _ in range(9)] #we will use a single list to rep 3x3 board
        self.currentWinner = None #to keep track of winner

    def printBoard(self):
        #this is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+' | '.join(row)+' |')

    @staticmethod   #function which doesn't use self
    def printBoardNums():
        #tells us what number corresponds to what box
        numberBoard = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in numberBoard:
            print('| '+' | '.join(row)+' |')

    def availableMoves(self):
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     if spot == ' ':
        #         moves.append(i)
        # return moves
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def emptySquares(self):
        return ' ' in self.board

    def numEmptySquares(self):
        return self.board.count(' ')

    def makeMove(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.currentWinner = letter
            return True
        return False

    def winner(self, square, letter):
        #check the row
        row_ind = square // 3
        row = self.board[ row_ind*3 : (row_ind+1)*3 ]
        if all([spot == letter for spot in row]):
            return True

        #check the column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #check the diagonal
        #but if only the square is an even number [0, 2, 4, 6, 8]
        if square % 2 == 0:
            #check the left to right diagonal
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            #check the right to left diagonal
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        
        #if all of these false
        return False



def play(game, x_player, o_player, printGame = True):
    if printGame:
        game.printBoardNums()

    letter = 'X'
    while game.emptySquares():
        #get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        if game.makeMove(square, letter):
            if printGame:
                print(letter+ f' makes a move to square {square}')
                game.printBoard()
                print('')   #just an empty line

            if game.currentWinner:
                if printGame:
                    print(letter + ' wins !')
                return letter
        
            #after we made move, we alternate letters
            letter = 'O' if letter == 'X' else 'X'

            #tiny break to make things a little easier to read
            time.sleep(0.8)

    if printGame:
        print('It\'s a tie !')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t= TicTacToe()
    play(t, x_player, o_player, printGame = True)



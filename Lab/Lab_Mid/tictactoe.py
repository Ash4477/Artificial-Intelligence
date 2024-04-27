from copy import deepcopy

# Tic Tac Toe Board
class Board():
    def __init__(self, board=None):
        self.player_x = 'x'
        self.player_o = 'o'
        self.empty_square = '.'

        self.position = {}

        self.init_board()

        if board is not None:
            self.__dict__ = deepcopy(board.__dict__)

    def init_board(self):
        for row in range(3):
            for col in range(3):
                self.position[row, col] = self.empty_square
    
    def __str__(self):
        for row in range(3):
            for col in range(3):
                print(' %S' % self.position[row, col])


# main driver
if __name__  == '__main__':
    board = Board()
    print(board.dict)
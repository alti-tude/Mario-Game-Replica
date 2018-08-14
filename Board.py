import config
import os
from colorama import *


class Board:
    #board contains the printout
    #collision_map contains the actual collision map

    def __init__(self):
        rep = [' ' for i in range(config.boardWidth)]
        self.board = [rep[:] for i in range(config.boardHeight)]

        rep = [0 for i in range(config.boardWidth)]
        self.collision_map = [rep[:] for i in range(config.boardHeight)]

    @staticmethod
    def border_board(matrix):
        for i in range(config.dispHeight):
            matrix[i][0] = 'X'
            matrix[i][-1] = 'X'

        for i in range(config.dispWidth):
            matrix[0][i] = 'X'
            matrix[-1][i] = 'X'

        return matrix

    def render(self, start_col):
        os.system("tput reset")
        matrix = []
        for i in range(config.dispHeight):
            ap = [self.board[i][j+start_col] for j in range(config.dispWidth)]
            matrix.append(ap)

        matrix = self.border_board(matrix)
        for i in range(config.dispHeight):
            print(''.join(matrix[i][:]))


if __name__=='__main__':
    board = Board()
    board.render(0)

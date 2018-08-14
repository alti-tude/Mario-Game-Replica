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
            matrix[i].insert(0, 'X')
            matrix[i].append('X')

        matrix.append(['X']*(config.dispWidth+2))
        matrix.insert(0, ['X']*(config.dispWidth+2))

        return matrix

    def render(self, start_col):
        os.system("tput reset")
        matrix = []
        for i in range(config.dispHeight):
            ap = [self.board[i][j+start_col] for j in range(config.dispWidth)]
            matrix.append(ap)

        matrix = self.border_board(matrix)
        for i in range(len(matrix)):
            print(''.join(matrix[i][:]))



if __name__=='__main__':
    board = Board()
    board.render(0)

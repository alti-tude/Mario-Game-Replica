import GLOBAL
import config


class Entity:

    def __init__(self, x, y, shape_mat, code):
        self.x = x
        self.y = y
        self.shape_mat = shape_mat
        self.code = code
        self.copy_sprite()

    def copy_sprite(self):
        for i in range(len(self.shape_mat)):
            for j in range(len(self.shape_mat[0])):
                GLOBAL.board.collision_map[self.y + i][self.x + j] = self.code
                GLOBAL.board.board[self.y + i][self.x + j] = self.shape_mat[i][j]

    def del_sprite(self):
        for i in range(len(self.shape_mat)):
            for j in range(len(self.shape_mat[0])):
                GLOBAL.board.collision_map[self.y+i][self.x+j] = 0
                GLOBAL.board.board[self.y+i][self.x+j] = ' '

    def mov(self, x, y):
        self.del_sprite()

        ch = False
        if 0 <= y+2 < config.boardHeight and 0 <= x+2 < config.boardWidth:
            ch = True
            for i in range(len(self.shape_mat)):
                for j in range(len(self.shape_mat[0])):
                    if GLOBAL.board.collision_map[y+i][x+j] == 10:
                        ch = False
                        break

        if ch:
            self.x = x
            self.y = y

        self.copy_sprite()

    def gravity(self):
        self.mov(self.x, self.y+1)

    def __del__(self):
        self.del_sprite()


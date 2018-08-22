import GLOBAL
import config


class Entity():

    def __init__(self, x, y, shape_mat, code="none"):
        self.x = x
        self.y = y
        self.shape_mat = shape_mat
        self.code = code
        self.copy_sprite()

    def copy_sprite(self):
        for i in range(len(self.shape_mat)):
            for j in range(len(self.shape_mat[0])):
                if self.code!= "none":
                     GLOBAL.board.collision_map[self.y + i][self.x + j] = self.code
                GLOBAL.board.board[self.y + i][self.x + j] = self.shape_mat[i][j]

    def del_sprite(self):
        for i in range(len(self.shape_mat)):
            for j in range(len(self.shape_mat[0])):
                if self.code!="none" and 0 <= self.y+i < len(GLOBAL.board.collision_map) and 0 <= self.x + j < len(GLOBAL.board.collision_map[0]):
                    # print(self.y+i)
                    # print(self.x+j)
                    GLOBAL.board.collision_map[self.y+i][self.x+j] = 0
                GLOBAL.board.board[self.y+i][self.x+j] = ' '

    def mov(self, x, y):
        self.del_sprite()

        ch = False
        if 0 <= y+len(self.shape_mat) < config.boardHeight and 0 <= x+len(self.shape_mat[0]) < config.boardWidth:
            ch = True
            for i in range(len(self.shape_mat)):
                for j in range(len(self.shape_mat[0])):
                    if GLOBAL.board.collision_map[y+i][x+j] == 10 or GLOBAL.board.collision_map[y+i][x+j]<0:
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


class Bullet(Entity):
    code = 200
    def __init__(self,x,y):
        Entity.__init__(self,x,y,config.bullet_sprite)
        self.code = Bullet.code 
        Bullet.code += 1

    
    def next(self):
        if GLOBAL.board.collision_map[self.y][self.x+1] == -200:
            GLOBAL.boss.health -= 1
            return
        self.mov(self.x+1, self.y)




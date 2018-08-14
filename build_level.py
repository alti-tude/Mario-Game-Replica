import config
import GLOBAL
import random
import time


def gen_block(x, y):
    ch = True
    for i in range(3):
        for j in range(6):
            if i+y>=config.boardHeight-3 or j+x>=config.boardWidth or GLOBAL.board.collision_map[y + i][x + j] > 1:
                ch = False
                break
    if ch:
        for i in range(3):
            for j in range(6):
                GLOBAL.board.collision_map[y + i][x + j] = 10
                GLOBAL.board.board[y + i][x + j] = '\033[44m \033[49m'


def gen_level():
    for i in range(config.boardWidth):
        GLOBAL.board.board[-1][i] = '\033[42m \033[49m'
        GLOBAL.board.collision_map[-1][i] = 10
        GLOBAL.board.board[-2][i] = '\033[42m \033[49m'
        GLOBAL.board.collision_map[-2][i] = 10
        GLOBAL.board.board[-3][i] = '\033[42m \033[49m'
        GLOBAL.board.collision_map[-3][i] = 10

    i = 10
    while i < config.boardWidth - config.dispWidth:
        if random.randint(0, 3)%2 == 0:
            gen_block(i, 24)
            i = i+6
            print(i)
        else:
            i = i+12


if __name__ == '__main__':
    # GLOBAL.init()

    gen_level()
    i = 0
    while i < config.boardWidth - config.dispWidth:
        time.sleep(0.02)
        GLOBAL.board.render(i)
        i = i+1

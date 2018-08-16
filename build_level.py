import config
import GLOBAL
import random
import time
import enemies


def valid(x):
    if GLOBAL.board.collision_map[21][x-4] == 10 or GLOBAL.board.collision_map[24][x-1] == 10:
        return True
    else:
        return False


def valid_pos(x, y):
    ch = True
    for i in range(3):
        for j in range(6):
            if i + y >= config.boardHeight - 3 or j + x >= config.boardWidth or GLOBAL.board.collision_map[y + i][x + j] > 1:
                ch = False
                break
    return ch


def gen_block(x, y):
    if valid_pos(x,y):
        for i in range(3):
            for j in range(6):
                GLOBAL.board.collision_map[y + i][x + j] = 10
                GLOBAL.board.board[y + i][x + j] = '\033[33m\\\033[39m'


def gen_decor():
    for i in range(config.boardWidth-config.dispWidth):
        for j in range(0, 12):
            if random.randint(0, 99)%99 == 0:
                for k in range(len(config.cloud_sprite)):
                    for l in range(len(config.cloud_sprite[0])):
                        GLOBAL.board.board[j+k][i+l] = config.cloud_sprite[k][l]


def gen_level():
    for i in range(config.boardWidth):
        GLOBAL.board.board[-1][i] = '\033[32m@\033[39m'
        GLOBAL.board.collision_map[-1][i] = 10
        GLOBAL.board.board[-2][i] = '\033[32m@\033[39m'
        GLOBAL.board.collision_map[-2][i] = 10
        GLOBAL.board.board[-3][i] = '\033[32m@\033[39m'
        GLOBAL.board.collision_map[-3][i] = 10

    ##### l1 gen #######
    i = 10
    while i < config.boardWidth - config.dispWidth:
        if random.randint(0, config.seed)%2 == 0:
            gen_block(i, 24)
            i = i+6
        else:
            i = i+12

    #### l2 gen #######
    i = 10
    while i < config.boardWidth - config.dispWidth:
        if random.randint(0, config.seed)%3 == 0 and valid(i):
            gen_block(i, 21)
            i = i+6
        else:
            i = i+9


def gen_enemies():
    i = 10

    while i < config.boardWidth - config.dispWidth:
        if random.randint(0, config.seed) % 11 == 0:
            if i%2==0 and valid_pos(i, 24):
                temp = enemies.Goomba(i, 24)
                GLOBAL.enemy_list[temp.co] = temp
            elif valid_pos(i, 21):
                temp = enemies.Goomba(i, 21)
                GLOBAL.enemy_list[temp.co] = temp

            i = i + 30
        else:
            i = i + 12


if __name__ == '__main__':
    # GLOBAL.init()

    gen_decor()
    gen_level()
    gen_enemies()
    i = 0
    while i < config.boardWidth - config.dispWidth:
        time.sleep(0.02)
        for j in GLOBAL.enemy_list:
            GLOBAL.enemy_list[j].next()
            GLOBAL.enemy_list[j].gravity()

        GLOBAL.board.render(i)
        i = i+1

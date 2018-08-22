import config
import GLOBAL
import random
import time
import enemies
import collectible


def valid(x):
    if GLOBAL.board.collision_map[21][x-4] == 10 or GLOBAL.board.collision_map[24][x-1] == 10:
        return True
    else:
        return False


def valid_pos(x, y):
    ch = True
    for i in range(3):
        for j in range(6):
            if i + y >= config.boardHeight - 3 or j + x >= config.boardWidth or GLOBAL.board.collision_map[y + i][x + j] != 0:
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
    f = 0
    while i < config.boardWidth - 10:
        if random.randint(0, config.seed)%2 == 0:
            gen_block(i, 24)
            i = i+6
            f=1
        else:
            i = i+12
            f=0
        if random.randint(0, config.seed)%19 == 0 and f==1:
            for k in range(6):
                for j in range(1,3):
                    GLOBAL.board.collision_map[-1-j][i+k]=0
                    GLOBAL.board.board[-1-j][i+k] = ' '
                GLOBAL.board.board[-1][i+k] = '\033[31m^\033[39m'

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
    for i in range(0,config.boardWidth - config.dispWidth, len(config.goomba_sprite[0]*2)):
        a = random.randint(0,1)
        b = random.randint(0,19)
        if a == 1 and b%19 == 0:
            temp = enemies.Goomba(i, 0)
            GLOBAL.enemy_list[temp.code] = temp
        elif a == 0 and b%19 == 0:
            temp = enemies.FastRoomba(i, 0)
            GLOBAL.enemy_list[temp.code] = temp
    
    for j in range(config.dispHeight):
        for i in GLOBAL.enemy_list:
            GLOBAL.enemy_list[i].gravity()

def gen_collectibles():
    i = 10
    for i in range(0,config.boardWidth - config.dispWidth, len(config.coin_sprite[0]*2)):
        if random.randint(0, config.seed)%29 == 0:
            temp = collectible.Coin(i,0)
            GLOBAL.coin_list[temp.code]=temp
    
    i = 100
    for i in range(0,config.boardWidth - config.dispWidth, len(config.health_sprite[0]*2)):
        if random.randint(0, config.seed)%199 == 0:
            temp = collectible.PowerUpHealth(i,0)
            GLOBAL.coin_list[temp.code]=temp
    
    for j in range(config.dispHeight):
        for i in GLOBAL.coin_list:
            GLOBAL.coin_list[i].gravity()

if __name__ == '__main__':

    gen_level()
    gen_collectibles()
    gen_decor()
    gen_enemies()
    
    # i = 0
    # while i < config.boardWidth - config.dispWidth:
    #     time.sleep(0.2)
    #     for j in GLOBAL.enemy_list:
    #         GLOBAL.enemy_list[j].next()
    #         GLOBAL.enemy_list[j].gravity()

    #     GLOBAL.board.render(i)
    #     i = i+1

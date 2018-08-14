import config
import GLOBAL


def gen_floor():
    for i in range(config.boardWidth):
        GLOBAL.board.board[-2][i] = '\033[42m \033[49m'
        GLOBAL.board.collision_map[-2][i] = 1
        GLOBAL.board.board[-3][i] = '\033[42m \033[49m'
        GLOBAL.board.collision_map[-3][i] = 1
        GLOBAL.board.board[-4][i] = '\033[42m \033[49m'
        GLOBAL.board.collision_map[-4][i] = 1


if __name__ == '__main__':
    # GLOBAL.init()
    gen_floor()
    GLOBAL.board.render(0)

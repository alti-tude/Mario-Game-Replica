import random
import config
from colorama import *
import time
import GLOBAL
import debug


def main():

    bgLayer = []
    ap = [' ' for i in range(config.bgWidth)]

    for i in range(config.bgHeight):
        bgLayer.append(ap[:])

    for i in range(config.bgStarCount):
        x = random.randint(0, config.bgWidth-1)
        y = random.randint(0, config.bgHeight-1)

        bgLayer[y][x] = '*'

    i = 0
    while True:
        i = i%(config.bgWidth-config.dispSize)
        time.sleep(0.02)
        disp = []
        debug.dprint("\033[2J \033[100A")

        for j in range(config.bgHeight):
            disp.append(bgLayer[j][i:i+config.dispSize])
            debug.dprint(''.join(disp[-1]))

        i = i + 1
        GLOBAL.printout = disp


if __name__ == "__main__":
    debug.debug = True
    main()


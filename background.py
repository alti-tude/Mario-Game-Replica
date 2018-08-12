import random
import config
from colorama import *
import time
import GLOBAL
import debug
import os


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
        if debug.debug:
            os.system("tput reset")

        for j in range(config.bgHeight):
            disp.append(bgLayer[j][i:i+config.dispSize])
            debug.dprint("\033[32m "+''.join(disp[-1])+" \033[0m")

        i = i + 1
        GLOBAL.printout = disp


if __name__ == "__main__":
    debug.debug = True
    main()


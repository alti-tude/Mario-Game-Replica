import GLOBAL
import background
import time
import _thread
from colorama import *
import os


_thread.start_new_thread(background.main, ())

for i in range(100):
    time.sleep(0.04)
    disp = GLOBAL.printout[:]
    # print(disp)

    # for i in range(len(disp)):
    #     print(''.join(disp[i][:]))

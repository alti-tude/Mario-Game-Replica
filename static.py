import GLOBAL
import background
import time
import _thread
from colorama import *

_thread.start_new_thread(background.main, ())
print(2)
for i in range(100):
    time.sleep(0.04)
    disp = GLOBAL.printout[:]
    # print(disp)

    disp[50][50] = 'W'


    for i in range(100):
        print(''.join(disp[i][:]))
    print("\033[100A")


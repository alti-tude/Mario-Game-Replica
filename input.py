import time
import queue
import threading


class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()
q = queue.Queue()
def startIp():
    # print(getch())  
    while True:
        print(q.qsize())
        q.put(getch())
        if q.get()=='q':
            exit(1)
        # print(q.get())

if __name__=='__main__':
    # threading.Thread(target=startIp, args=()
    startIp()
    # while True:
    #     time.sleep(0.2)
    #     if q.qsize()>0:
    #         print(q.get())
    #     else:
    #         pass

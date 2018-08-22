import Board
import queue
import Player
import enemies

level = 1
board = Board.Board()
coin_list = {}
points = 0
enemy_list = {}
q = queue.Queue()
player = Player.Player(0,0)
boss = enemies.Boss(50,1)
boss.del_sprite()
bullet_list ={}

def init():
    global player
    global q
    global enemy_list
    global points 
    global coin_list
    global board
    board = Board.Board()
    coin_list = {}
    points = 0
    enemy_list = {}
    bullet_list ={}

    q = queue.Queue()
    player = Player.Player(0,0)
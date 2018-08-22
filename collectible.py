import entity
import config
import GLOBAL

class Collectibles(entity.Entity):
    code = -1
    def __init__(self, x, y, sprite):
        entity.Entity.__init__(self, x, y, sprite, Collectibles.code)
        self.code = Collectibles.code
        Collectibles.code -= 1

    def __str__(self):
        return str(Collectibles.code) + " " + str(self.code)


class Coin(Collectibles):
    def __init__(self, x, y):
        Collectibles.__init__(self, x, y, config.coin_sprite)

    def __del__(self):
        self.del_sprite()
        GLOBAL.points += config.coin_points


class PowerUpHealth(Collectibles):
    def __init__(self, x, y):
        Collectibles.__init__(self, x, y, config.health_sprite)
    
    def __del__(self):
        self.del_sprite()
        GLOBAL.player.health += 1
        
if __name__=='__main__':
    for i in range(10):
        a = Coin(0,0)
        print(a)

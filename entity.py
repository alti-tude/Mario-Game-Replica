import GLOBAL


class entity:

    def __init__(self, y, x, layer):
        self.x = x
        self.y = y
        self.layer = layer
        GLOBAL.maxLayer = max(layer, GLOBAL.maxLayer)

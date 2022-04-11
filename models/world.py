class World(object):
    def __init__(self, heigth, width):
        lat = [None for _ in range(heigth)]
        self.map = [lat for _ in range(width)]

    def setPlayer(self, player):
        self.player = player

    def getMap(self):
        return self.player.getNickname()
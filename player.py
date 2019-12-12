class Player:
    name = "unnamed"    # player name: p1, p2, p3, ...
    inventory =  {'none': 0}
    location = 'none'   # player's location: none, building names

    def __init__(self, name):
        self.name = name
        self.inventory = {'money': 5, 'coal': 1, 'wood': 4 }
        self.location = 'none'

    @staticmethod
    def createPlayer(name):
        if name.lower() == "ai":
            return Player(name.upper())
        else:
            return Player(name.title())

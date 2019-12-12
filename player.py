class Player:
    name = "unnamed"    # player name: p1, p2, p3, ...
    inventory =  {'none': 0}
    location = 'none'   # player's location: none, building names
    type = 'undefined'  # player type: "human", "computer"

    def __init__(self, name, type):
        self.name = name
        self.inventory = {'money': 5, 'coal': 1, 'wood': 4 }
        self.location = 'none'
        self.type = type

    @staticmethod
    def create_player(name):
        if name.lower() == "ai":
            return Player(name.upper(), 'computer')
        else:
            return Player(name.title(), 'human')

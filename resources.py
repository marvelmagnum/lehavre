class Resource:
    name = "undefined"
    energy = 0
    food = 0
    value = 0

    def __init__(self, name, energy, food, value):
        self.name = name
        self.energy = energy
        self.food = food
        self.value = value


money = Resource('money', 0, 1, 1)
wood = Resource('wood', 1, 0, 1)
charcoal = Resource('charcoal', 3, 0, 2)
coal = Resource('coal', 3, 0, 3)
coke = Resource('coke', 10, 0, 5)
fish = Resource('fish', 0, 1, 1)
smoked_fish = Resource('smoked fish', 0, 2, 2)
grain = Resource('grain', 0, 0, 1)
bread = Resource('bread', 0, 2, 3)
clay = Resource('clay', 0, 0, 1)
brick = Resource('brick', 0, 0, 2)
iron = Resource('iron', 0, 0, 2)
steel = Resource('steel', 0, 0, 8)
cattle = Resource('cattle', 0, 0, 3)
meat = Resource('meat', 0, 3, 2)
hides = Resource('hides', 0, 0, 2)
leather = Resource('leather', 0, 0, 4)

resource_map = {'money': money,
                'fish': fish,
                'wood': wood,
                'clay': clay,
                'iron': iron,
                'grain': grain,
                'cattle': cattle,
                'coal': coal,
                'charcoal': charcoal,
                'coke': coke,
                'smoked fish': smoked_fish,
                'bread': bread,
                'brick': brick,
                'steel': steel,
                'meat': meat,
                'hides': hides,
                'leather': leather}


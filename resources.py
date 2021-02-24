class Resource:
    def __init__(self, name, energy, food, value, category):
        self.name = name
        self.energy = energy
        self.food = food
        self.value = value
        self.category = category    # standard, upgraded


loan = Resource('loan', 0, 0, 0, 'undefined')
money = Resource('money', 0, 1, 1, 'undefined')
wood = Resource('wood', 1, 0, 1, 'standard')
charcoal = Resource('charcoal', 3, 0, 2, 'upgraded')
coal = Resource('coal', 3, 0, 3, 'standard')
coke = Resource('coke', 10, 0, 5, 'upgraded')
fish = Resource('fish', 0, 1, 1, 'standard')
smoked_fish = Resource('smoked fish', 0, 2, 2, 'upgraded')
grain = Resource('grain', 0, 0, 1, 'standard')
bread = Resource('bread', 0, 2, 3, 'upgraded')
clay = Resource('clay', 0, 0, 1, 'standard')
brick = Resource('brick', 0, 0, 2, 'upgraded')
iron = Resource('iron', 0, 0, 2, 'standard')
steel = Resource('steel', 0, 0, 8, 'upgraded')
cattle = Resource('cattle', 0, 0, 3, 'standard')
meat = Resource('meat', 0, 3, 2, 'upgraded')
hides = Resource('hides', 0, 0, 2, 'standard')
leather = Resource('leather', 0, 0, 4, 'upgraded')

resource_map = {'loan': loan,
                'money': money,
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


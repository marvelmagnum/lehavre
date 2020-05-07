class Ship:
    # Ship side
    name = "undefined"
    type = "undefined" # wooden ship, iron ship, steel ship, luxury liner
    build_cost = {'item': -1}
    fuel = {'item': -1} # fuel cost to use ship
    value = 0
    price = 0 # cost to purchase ship . 0 means it cannot be purchased
    capacity = 0
    food = [0,0,0,0,0] # food provided at end of round per number of players (1-5)
    # Harvest side
    harvest = {0 : [0, False, 0, "none"]} # harvest round map: player count mapped to [sort order, has harvest, feeding requirement, town development (none/standard/special)]
    description = "blah blah blah"

    @staticmethod
    def setup_rounds(game_state):
        """ Setup harvest rounds for game """
        ''' Find available ships/harvest rounds '''
        pl_count = len(game_state.players)
        for ship in game_state.ship_designs:
            if pl_count in ship.harvest:
                game_state.harvest_stack.append(ship)

        ''' Sort the stack by round sort order with smallest on top (for pop()) '''
        game_state.harvest_stack.sort(key=lambda x: x.harvest[pl_count][0], reverse = True)


''' Wooden Ships '''
wship1 = Ship()
wship1.name = "appoline"
wship1.type = "wooden ship"
wship1.build_cost = {'wood': 5 }
wship1.fuel = {'energy': 3}
wship1.value = 2
wship1.price = 14
wship1.capacity = 2
wship1.food = [5,4,3,2,1]
wship1.harvest = {1 : [1, True, 5, 'special'],
                  2 : [1, True, 3, 'none'],
                  3 : [2, True, 2, 'none'],
                  4 : [1, True, 1, 'none'],
                  5 : [1, True, 0, 'none']}
wship1.description = "Can ship 2 goods by spending 3 energy."

wship2 = Ship()
wship2.name = "lucie"
wship2.type = "wooden ship"
wship2.build_cost = {'wood': 5 }
wship2.fuel = {'energy': 3}
wship2.value = 4
wship2.price = 14
wship2.capacity = 2
wship2.food = [5,4,3,2,1]
wship2.harvest = {1 : [2, True, 10, 'standard'],
                  2 : [3, True, 5, 'special'],
                  3 : [4, True, 3, 'special'],
                  4 : [4, True, 2, 'standard'],
                  5 : [4, True, 1, 'standard']}
wship2.description = "Can ship 2 goods by spending 3 energy."

wship3 = Ship()
wship3.name = "blanche"
wship3.type = "wooden ship"
wship3.build_cost = {'wood': 5 }
wship3.fuel = {'energy': 3}
wship3.value = 2
wship3.price = 14
wship3.capacity = 2
wship3.food = [5,4,3,2,1]
wship3.harvest = {2 : [2, True, 4, 'standard'],
                  3 : [3, True, 3, 'standard'],
                  4 : [2, True, 1, 'none'],
                  5 : [2, True, 1, 'none']}
wship3.description = "Can ship 2 goods by spending 3 energy."

wship4 = Ship()
wship4.name = "noemi"
wship4.type = "wooden ship"
wship4.build_cost = {'wood': 5 }
wship4.fuel = {'energy': 3}
wship4.value = 4
wship4.price = 14
wship4.capacity = 2
wship4.food = [5,4,3,2,1]
wship4.harvest = {2 : [4, True, 7, 'none'],
                  3 : [5, True, 4, 'none'],
                  4 : [5, True, 2, 'special'],
                  5 : [5, True, 1, 'special']}
wship4.description = "Can ship 2 goods by spending 3 energy."

wship5 = Ship()
wship5.name = "ophelie"
wship5.type = "wooden ship"
wship5.build_cost = {'wood': 5 }
wship5.fuel = {'energy': 3}
wship5.value = 6
wship5.price = 14
wship5.capacity = 2
wship5.food = [5,4,3,2,1]
wship5.harvest = {2 : [5, True, 9, 'standard'],
                  3 : [7, True, 6, 'standard'],
                  4 : [7, True, 3, 'standard'],
                  5 : [7, True, 2, 'standard']}
wship5.description = "Can ship 2 goods by spending 3 energy."

wship6 = Ship()
wship6.name = "dina"
wship6.type = "wooden ship"
wship6.build_cost = {'wood': 5 }
wship6.fuel = {'energy': 3}
wship6.value = 2
wship6.price = 14
wship6.capacity = 2
wship6.food = [5,4,3,2,1]
wship6.harvest = {3 : [1, False, 2, 'none'],
                  4 : [3, False, 2, 'none'],
                  5 : [3, False, 1, 'none']}
wship6.description = "Can ship 2 goods by spending 3 energy."

wship7 = Ship()
wship7.name = "salomee"
wship7.type = "wooden ship"
wship7.build_cost = {'wood': 5 }
wship7.fuel = {'energy': 3}
wship7.value = 6
wship7.price = 14
wship7.capacity = 2
wship7.food = [5,4,3,2,1]
wship7.harvest = {4 : [9, False, 4, 'none'],
                  5 : [9, False, 2, 'none']}
wship7.description = "Can ship 2 goods by spending 3 energy."


''' Iron Ships '''
iship1 = Ship()
iship1.name = "saint-malo"
iship1.type = "iron ship"
iship1.build_cost = {'iron': 4 }
iship1.fuel = {'energy': 3}
iship1.value = 6
iship1.price = 20
iship1.capacity = 3
iship1.food = [7,5,4,3,2]
iship1.harvest = {1 : [3, True, 15, 'special'],
                  2 : [7, True, 13, 'none'],
                  3 : [9, True, 8, 'none'],
                  4 : [10, True, 5, 'standard'],
                  5 : [10, True, 3, 'standard']}
iship1.description = "Can ship 3 goods by spending 3 energy."

iship2 = Ship()
iship2.name = "caen"
iship2.type = "iron ship"
iship2.build_cost = {'iron': 4 }
iship2.fuel = {'energy': 3}
iship2.value = 10
iship2.price = 20
iship2.capacity = 3
iship2.food = [7,5,4,3,2]
iship2.harvest = {1 : [4, True, 20, 'standard'],
                  2 : [9, True, 16, 'special'],
                  3 : [12, True, 11, 'special'],
                  4 : [13, True, 7, 'standard'],
                  5 : [13, True, 4, 'standard']}
iship2.description = "Can ship 3 goods by spending 3 energy."

iship3 = Ship()
iship3.name = "boulogne"
iship3.type = "iron ship"
iship3.build_cost = {'iron': 4 }
iship3.fuel = {'energy': 3}
iship3.value = 4
iship3.price = 20
iship3.capacity = 3
iship3.food = [7,5,4,3,2]
iship3.harvest = {2 : [6, True, 11, 'special'],
                  3 : [8, True, 7, 'special'],
                  4 : [8, True, 4, 'special'],
                  5 : [8, True, 2, 'special']}
iship3.description = "Can ship 3 goods by spending 3 energy."

iship4 = Ship()
iship4.name = "dunkerque"
iship4.type = "iron ship"
iship4.build_cost = {'iron': 4 }
iship4.fuel = {'energy': 3}
iship4.value = 8
iship4.price = 20
iship4.capacity = 3
iship4.food = [7,5,4,3,2]
iship4.harvest = {2 : [8, True, 15, 'standard'],
                  3 : [10, True, 9, 'none'],
                  4 : [11, True, 5, 'special'],
                  5 : [11, True, 3, 'special']}
iship4.description = "Can ship 3 goods by spending 3 energy."

iship5 = Ship()
iship5.name = "cherbourg"
iship5.type = "iron ship"
iship5.build_cost = {'iron': 4 }
iship5.fuel = {'energy': 3}
iship5.value = 2
iship5.price = 20
iship5.capacity = 3
iship5.food = [7,5,4,3,2]
iship5.harvest = {3 : [6, False, 5, 'none'],
                  4 : [6, False, 3, 'none'],
                  5 : [6, False, 2, 'none']}
iship5.description = "Can ship 3 goods by spending 3 energy."

iship6 = Ship()
iship6.name = "calais"
iship6.type = "iron ship"
iship6.build_cost = {'iron': 4 }
iship6.fuel = {'energy': 3}
iship6.value = 12
iship6.price = 20
iship6.capacity = 3
iship6.food = [7,5,4,3,2]
iship6.harvest = {4 : [15, False, 9, 'none'],
                  5 : [15, False, 4, 'none']}
iship6.description = "Can ship 3 goods by spending 3 energy."


''' Steel Ships '''
sship1 = Ship()
sship1.name = "bremerhaven"
sship1.type = "steel ship"
sship1.build_cost = {'steel': 2 }
sship1.fuel = {'energy': 3}
sship1.value = 16
sship1.price = 30
sship1.capacity = 4
sship1.food = [10,7,6,5,3]
sship1.harvest = {1 : [5, True, 25, 'special'],
                  2 : [10, True, 17, 'none'],
                  3 : [13, True, 12, 'none'],
                  4 : [14, True, 8, 'special'],
                  5 : [14, True, 4, 'special']}
sship1.description = "Can ship 4 goods by spending 3 energy."

sship2 = Ship()
sship2.name = "amsterdam"
sship2.type = "steel ship"
sship2.build_cost = {'steel': 2 }
sship2.fuel = {'energy': 3}
sship2.value = 20
sship2.price = 30
sship2.capacity = 4
sship2.food = [10,7,6,5,3]
sship2.harvest = {1 : [6, True, 30, 'standard'],
                  2 : [11, True, 18, 'standard'],
                  3 : [14, True, 13, 'standard'],
                  4 : [16, True, 10, 'standard'],
                  5 : [16, True, 5, 'standard']}
sship2.description = "Can ship 4 goods by spending 3 energy."

sship3 = Ship()
sship3.name = "lissabohn"
sship3.type = "steel ship"
sship3.build_cost = {'steel': 2 }
sship3.fuel = {'energy': 3}
sship3.value = 24
sship3.price = 30
sship3.capacity = 4
sship3.food = [10,7,6,5,3]
sship3.harvest = {2 : [12, True, 19, 'special'],
                  3 : [15, True, 14, 'special'],
                  4 : [17, True, 10, 'special'],
                  5 : [17, True, 5, 'special']}
sship3.description = "Can ship 4 goods by spending 3 energy."

sship4 = Ship()
sship4.name = "triest"
sship4.type = "steel ship"
sship4.build_cost = {'steel': 2 }
sship4.fuel = {'energy': 3}
sship4.value = 10
sship4.price = 30
sship4.capacity = 4
sship4.food = [10,7,6,5,3]
sship4.harvest = {3 : [11, False, 10, 'standard'],
                  4 : [12, False, 6, 'none'],
                  5 : [12, False, 3, 'none']}
sship4.description = "Can ship 4 goods by spending 3 energy."


''' Luxury Liners '''
lship1 = Ship()
lship1.name = "ms andrea"
lship1.type = "luxury liner"
lship1.build_cost = {'steel': 3 }
lship1.fuel = {}
lship1.value = 30
lship1.harvest = {1 : [7, False, 35, 'none'],
                  2 : [14, False, 20, 'none'],
                  3 : [18, False, 15, 'none'],
                  4 : [20, False, 11, 'none'],
                  5 : [20, False, 6, 'none']}
lship1.description = "High value ship but cannot ship goods. Can only be built."

lship2 = Ship()
lship2.name = "ms doris"
lship2.type = "luxury liner"
lship2.build_cost = {'steel': 3 }
lship2.fuel = {}
lship2.value = 34
lship2.harvest = {2 : [13, True, 20, 'none'],
                  3 : [17, True, 15, 'none'],
                  4 : [19, True, 11, 'none'],
                  5 : [19, True, 6, 'none']}
lship2.description = "High value ship but cannot ship goods. Can only be built."

lship3 = Ship()
lship3.name = "ms susanne"
lship3.type = "luxury liner"
lship3.build_cost = {'steel': 3 }
lship3.fuel = {}
lship3.value = 38
lship3.harvest = {3 : [16, False, 14, 'none'],
                  4 : [18, False, 11, 'none'],
                  5 : [18, False, 5, 'none']}
lship3.description = "High value ship but cannot ship goods. Can only be built."
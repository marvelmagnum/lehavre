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
    unlocked = False  # is this ship available to build/purchase?
    # Harvest side
    players = { 0 : [0, 0, "none"]} # harvest round map: player count mapped to [sort order, feeding requirement, town development (none/standard/special)]
    description = "blah blah blah"

''' Wooden Ships '''
wship1 = Ship()
wship1.name = "appoline"
wship1.type = "wooden ship"
wship1.build_cost = {'wood': 5, 'energy': 3}
wship1.fuel = {'energy': 3}
wship1.value = 2
wship1.price = 14
wship1.capacity = 2
wship1.food = [5,4,3,2,1]
wship1.players = { 1 : [1, 5, 'special'],
                   2 : [1, 3, 'none'],
                   3 : [2, 2, 'none'],
                   4 : [1, 1, 'none'],
                   5 : [1, 0, 'none']}
wship1.description = "Can ship 2 goods by spending 3 energy."

wship2 = Ship()
wship2.name = "lucie"
wship2.type = "wooden ship"
wship2.build_cost = {'wood': 5, 'energy': 3}
wship2.fuel = {'energy': 3}
wship2.value = 4
wship2.price = 14
wship2.capacity = 2
wship2.food = [5,4,3,2,1]
wship2.players = { 1 : [2, 10, 'standard'],
                   2 : [3, 5, 'special'],
                   3 : [4, 3, 'special'],
                   4 : [4, 2, 'standard'],
                   5 : [4, 1, 'standard']}
wship2.description = "Can ship 2 goods by spending 3 energy."

wship3 = Ship()
wship3.name = "blanche"
wship3.type = "wooden ship"
wship3.build_cost = {'wood': 5, 'energy': 3}
wship3.fuel = {'energy': 3}
wship3.value = 2
wship3.price = 14
wship3.capacity = 2
wship3.food = [5,4,3,2,1]
wship3.players = { 2 : [2, 4, 'standard'],
                   3 : [3, 3, 'standard'],
                   4 : [2, 1, 'none'],
                   5 : [2, 1, 'none']}
wship3.description = "Can ship 2 goods by spending 3 energy."

wship4 = Ship()
wship4.name = "noemi"
wship4.type = "wooden ship"
wship4.build_cost = {'wood': 5, 'energy': 3}
wship4.fuel = {'energy': 3}
wship4.value = 4
wship4.price = 14
wship4.capacity = 2
wship4.food = [5,4,3,2,1]
wship4.players = { 2 : [4, 7, 'none'],
                   3 : [5, 4, 'none'],
                   4 : [5, 2, 'special'],
                   5 : [5, 1, 'special']}
wship4.description = "Can ship 2 goods by spending 3 energy."

wship5 = Ship()
wship5.name = "ophelie"
wship5.type = "wooden ship"
wship5.build_cost = {'wood': 5, 'energy': 3}
wship5.fuel = {'energy': 3}
wship5.value = 6
wship5.price = 14
wship5.capacity = 2
wship5.food = [5,4,3,2,1]
wship5.players = { 2 : [5, 9, 'standard'],
                   3 : [7, 6, 'standard'],
                   4 : [7, 3, 'standard'],
                   5 : [7, 2, 'standard']}
wship5.description = "Can ship 2 goods by spending 3 energy."

wship6 = Ship()
wship6.name = "dina"
wship6.type = "wooden ship"
wship6.build_cost = {'wood': 5, 'energy': 3}
wship6.fuel = {'energy': 3}
wship6.value = 2
wship6.price = 14
wship6.capacity = 2
wship6.food = [5,4,3,2,1]
wship6.players = { 3 : [1, 2, 'none'],
                   4 : [3, 2, 'none'],
                   5 : [3, 1, 'none']}
wship6.description = "Can ship 2 goods by spending 3 energy."

wship7 = Ship()
wship7.name = "salomee"
wship7.type = "wooden ship"
wship7.build_cost = {'wood': 5, 'energy': 3}
wship7.fuel = {'energy': 3}
wship7.value = 6
wship7.price = 14
wship7.capacity = 2
wship7.food = [5,4,3,2,1]
wship7.players = { 4 : [9, 4, 'none'],
                   5 : [9, 2, 'none']}
wship7.description = "Can ship 2 goods by spending 3 energy."


''' Iron Ships '''
iship1 = Ship()
iship1.name = "saint-malo"
iship1.type = "iron ship"
iship1.build_cost = {'iron': 4, 'energy': 3}
iship1.fuel = {'energy': 3}
iship1.value = 6
iship1.price = 20
iship1.capacity = 3
iship1.food = [7,5,4,3,2]
iship1.players = { 1 : [3, 15, 'special'],
                   2 : [7, 13, 'none'],
                   3 : [9, 8, 'none'],
                   4 : [10, 5, 'standard'],
                   5 : [10, 3, 'standard']}
iship1.description = "Can ship 3 goods by spending 3 energy."

iship2 = Ship()
iship2.name = "caen"
iship2.type = "iron ship"
iship2.build_cost = {'iron': 4, 'energy': 3}
iship2.fuel = {'energy': 3}
iship2.value = 10
iship2.price = 20
iship2.capacity = 3
iship2.food = [7,5,4,3,2]
iship2.players = { 1 : [4, 20, 'standard'],
                   2 : [9, 16, 'special'],
                   3 : [12, 11, 'special'],
                   4 : [13, 7, 'standard'],
                   5 : [13, 4, 'standard']}
iship2.description = "Can ship 3 goods by spending 3 energy."

iship3 = Ship()
iship3.name = "boulogne"
iship3.type = "iron ship"
iship3.build_cost = {'iron': 4, 'energy': 3}
iship3.fuel = {'energy': 3}
iship3.value = 4
iship3.price = 20
iship3.capacity = 3
iship3.food = [7,5,4,3,2]
iship3.players = { 2 : [6, 11, 'special'],
                   3 : [8, 7, 'special'],
                   4 : [8, 4, 'special'],
                   5 : [8, 2, 'special']}
iship3.description = "Can ship 3 goods by spending 3 energy."

iship4 = Ship()
iship4.name = "dunkerque"
iship4.type = "iron ship"
iship4.build_cost = {'iron': 4, 'energy': 3}
iship4.fuel = {'energy': 3}
iship4.value = 8
iship4.price = 20
iship4.capacity = 3
iship4.food = [7,5,4,3,2]
iship4.players = { 2 : [8, 15, 'standard'],
                   3 : [10, 9, 'none'],
                   4 : [11, 5, 'special'],
                   5 : [11, 3, 'special']}
iship4.description = "Can ship 3 goods by spending 3 energy."

iship5 = Ship()
iship5.name = "cherbourg"
iship5.type = "iron ship"
iship5.build_cost = {'iron': 4, 'energy': 3}
iship5.fuel = {'energy': 3}
iship5.value = 2
iship5.price = 20
iship5.capacity = 3
iship5.food = [7,5,4,3,2]
iship5.players = { 3 : [6, 5, 'none'],
                   4 : [6, 3, 'none'],
                   5 : [6, 2, 'none']}
iship5.description = "Can ship 3 goods by spending 3 energy."

iship6 = Ship()
iship6.name = "calais"
iship6.type = "iron ship"
iship6.build_cost = {'iron': 4, 'energy': 3}
iship6.fuel = {'energy': 3}
iship6.value = 12
iship6.price = 20
iship6.capacity = 3
iship6.food = [7,5,4,3,2]
iship6.players = { 4 : [15, 9, 'none'],
                   5 : [15, 4, 'none']}
iship6.description = "Can ship 3 goods by spending 3 energy."


''' Steel Ships '''
sship1 = Ship()
sship1.name = "bremerhaven"
sship1.type = "steel ship"
sship1.build_cost = {'steel': 2, 'energy': 3}
sship1.fuel = {'energy': 3}
sship1.value = 16
sship1.price = 30
sship1.capacity = 4
sship1.food = [10,7,6,5,3]
sship1.players = { 1 : [5, 25, 'special'],
                   2 : [10, 17, 'none'],
                   3 : [13, 12, 'none'],
                   4 : [14, 8, 'special'],
                   5 : [14, 4, 'special']}
sship1.description = "Can ship 4 goods by spending 3 energy."

sship2 = Ship()
sship2.name = "amsterdam"
sship2.type = "steel ship"
sship2.build_cost = {'steel': 2, 'energy': 3}
sship2.fuel = {'energy': 3}
sship2.value = 20
sship2.price = 30
sship2.capacity = 4
sship2.food = [10,7,6,5,3]
sship2.players = { 1 : [6, 30, 'standard'],
                   2 : [11, 18, 'standard'],
                   3 : [14, 13, 'standard'],
                   4 : [16, 10, 'standard'],
                   5 : [16, 5, 'standard']}
sship2.description = "Can ship 4 goods by spending 3 energy."

sship3 = Ship()
sship3.name = "lissabohn"
sship3.type = "steel ship"
sship3.build_cost = {'steel': 2, 'energy': 3}
sship3.fuel = {'energy': 3}
sship3.value = 24
sship3.price = 30
sship3.capacity = 4
sship3.food = [10,7,6,5,3]
sship3.players = { 2 : [12, 19, 'special'],
                   3 : [15, 14, 'special'],
                   4 : [17, 10, 'special'],
                   5 : [17, 5, 'special']}
sship3.description = "Can ship 4 goods by spending 3 energy."

sship4 = Ship()
sship4.name = "triest"
sship4.type = "steel ship"
sship4.build_cost = {'steel': 2, 'energy': 3}
sship4.fuel = {'energy': 3}
sship4.value = 10
sship4.price = 30
sship4.capacity = 4
sship4.food = [10,7,6,5,3]
sship4.players = { 3 : [11, 10, 'standard'],
                   4 : [12, 6, 'none'],
                   5 : [12, 3, 'none']}
sship4.description = "Can ship 4 goods by spending 3 energy."


''' Luxury Liners '''
lship1 = Ship()
lship1.name = "ms andrea"
lship1.type = "luxury liner"
lship1.build_cost = {'steel': 3, 'energy': 3}
lship1.fuel = {}
lship1.value = 30
lship1.players = { 1 : [7, 35, 'none'],
                   2 : [14, 20, 'none'],
                   3 : [18, 15, 'none'],
                   4 : [20, 11, 'none'],
                   5 : [20, 6, 'none']}
lship1.description = "High value ship but cannot ship goods. Can only be built."

lship2 = Ship()
lship2.name = "ms doris"
lship2.type = "luxury liner"
lship2.build_cost = {'steel': 3, 'energy': 3}
lship2.fuel = {}
lship2.value = 34
lship2.players = { 2 : [13, 20, 'none'],
                   3 : [17, 15, 'none'],
                   4 : [19, 11, 'none'],
                   5 : [19, 6, 'none']}
lship2.description = "High value ship but cannot ship goods. Can only be built."

lship3 = Ship()
lship3.name = "ms susanne"
lship3.type = "luxury liner"
lship3.build_cost = {'steel': 3, 'energy': 3}
lship3.fuel = {}
lship3.value = 38
lship3.players = { 3 : [16, 14, 'none'],
                   4 : [18, 11, 'none'],
                   5 : [18, 5, 'none']}
lship3.description = "High value ship but cannot ship goods. Can only be built."
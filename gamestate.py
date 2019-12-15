import buildings
import ships
import player

class GameState:
    offers = {'money': 2, 'fish': 2, 'wood': 2, 'clay': 1, 'iron': 0, 'grain': 0, 'cattle': 0}
    # inventory = {'money': 5, 'coal': 1 }
    current_player = 'none'  # current player: p1, p2, p3, ...
    # location = {'p1': 'none'}  # player's location: none, building names
    players = [] # list of players in the current game

    ship_designs = [  ships.wship1,
                      ships.wship2,
                      ships.wship3,
                      ships.wship4,
                      ships.wship5,
                      ships.wship6,
                      ships.wship7,
                      ships.iship1,
                      ships.iship2,
                      ships.iship3,
                      ships.iship4,
                      ships.iship5,
                      ships.iship6,
                      ships.sship1,
                      ships.sship2,
                      ships.sship3,
                      ships.sship4,
                      ships.lship1,
                      ships.lship2,
                      ships.lship3]

    bases = [['money', 'wood'],
             ['wood', 'fish', 'interest'],
             ['clay', 'fish'],
             ['money', 'iron'],
             ['grain', 'fish'],
             ['wood', 'clay'],
             ['wood', 'cattle']]

    constructed = [buildings.building_firm_a,
                   buildings.building_firm_b,
                   buildings.construction_firm]


    stacks = [[],[],[]] # 3 stacks of available building cards during the game
    harvest = [] # harvest round stack according to number of players
    ships = { 'game' : { 'wooden' : [],
                         'iron' : [],
                         'steel' : [],
                         'liner' : [] } } # available ships during the game. belonging to game and players. players don't have a dictionary. Just a list of owned ships.

    blueprints = [buildings.abattoir,
                  buildings.arts_center,
                  buildings.bakehouse,
                  buildings.bank,
                  buildings.black_market,
                  buildings.brick_works,
                  buildings.bridge_over_seine,
                  buildings.business_office,
                  buildings.charcoal_kiln,
                  buildings.church,
                  buildings.clay_mound,
                  buildings.colliery,
                  buildings.cokery,
                  buildings.dock,
                  buildings.fishery,
                  buildings.grocery,
                  buildings.hardware,
                  buildings.ironworks,
                  buildings.joinery,
                  buildings.court,
                  buildings.market,
                  buildings.sawmill,
                  buildings.shipping_line,
                  buildings.smokehouse,
                  buildings.tannery,
                  buildings.town_hall,
                  buildings.wharf1,
                  buildings.wharf2]

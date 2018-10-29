import buildings


class GameState:
    offers = {'money': 2, 'fish': 2, 'wood': 2, 'clay': 1, 'iron': 0, 'grain': 0, 'cattle': 0}
    inventory = {'money': 5, 'coal': 1}
    current_player = 'p1'  # current player: p1, p2, p3, ...
    location = {'p1': 'none'}  # player's location: none, building names

    bases = [['money', 'wood'],
             ['wood', 'fish', 'interest'],
             ['clay', 'fish'],
             ['money', 'iron'],
             ['grain', 'fish'],
             ['wood', 'clay'],
             ['wood', 'cattle']]

    constructed = [buildings.construction_firm]

    blueprints = [buildings.abattoir,
                  buildings.arts_center,
                  buildings.bakehouse,
                  buildings.black_market,
                  buildings.brick_works,
                  buildings.bridge_over_seine]


game_state = GameState()
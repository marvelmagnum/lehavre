import buildings
import ships

class GameState:
    offers = {'money': 2, 'fish': 2, 'wood': 2, 'clay': 1, 'iron': 0, 'grain': 0, 'cattle': 0}
    inventory = {'money': 5, 'coal': 1 }
    current_player = 'p1'  # current player: p1, p2, p3, ...
    location = {'p1': 'none'}  # player's location: none, building names
    ships = {'game':[ ships.wship1,
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
                      ships.lship3],
                'p1':[]}

    bases = [['money', 'wood'],
             ['wood', 'fish', 'interest'],
             ['clay', 'fish'],
             ['money', 'iron'],
             ['grain', 'fish'],
             ['wood', 'clay'],
             ['wood', 'cattle']]

    constructed = [buildings.building_firm_a,
                   buildings.building_firm_b,
                   buildings.construction_firm
                   ]


    blueprints = [buildings.abattoir,
                  buildings.arts_center,
                  buildings.bakehouse,
                  buildings.bank,
                  buildings.bakehouse,
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
                  ]


game_state = GameState()
import requestblocks
import actionblocks

# TODO: Handle end of game building abilities

class Building:
    name = "undefined"
    build_cost = {'item' : -1}
    fees = {'item' : -1}
    rank = 0
    value = 0
    price = 0   # for buildings which has different purchase cost than value. otherwise equal to value
    type = "none" # types: none, craftsman, economic, industrial, public
    icon = ['none'] # icons: none, hammer, fisherman
    owner = "undefined" # owners: blueprint, game, p1, p2, ...
    current_user = 0  #users: 0, Player objects [p1(), p2(), ...]
    usage_limit = 0 #how many times building can use used. unusable building are 0
    description = "blah blah blah"

    ''' 
    requests: a list of request objects to get the use params for the building. 
    the objects are executed sequentially generating a list of args that is passed back
    
    actions: a list of action objects to create the effect of the card
    each object returns a true / false and are called in order. 
    If any object returns False, the card is unusable by player
    '''
    requests = []   # request  objects: these create a list of params passed on to the action objects
    actions = []    # action objects

    def ask(self, game_state):
        params = [game_state]       # first element is the game state
        for request in self.requests:
            params.append(request.get(game_state))  # returned values from the request objects are appended
        return params

    def use(self, args):
        for action in self.actions:
            if not action.do(args):  # list of params generated from requests
                return False         # action failed. any action failure usually means the building use failed
        return True           # building used normally


''' A '''
abattoir = Building()
abattoir.name = "abattoir"
abattoir.build_cost = {'wood' : 1, 'clay' : 1, 'iron' : 1}
abattoir.fees = [{'money' : 2}]
abattoir.rank = 9
abattoir.value = abattoir.price = 8
abattoir.type = "craftsman"
abattoir.icon = ['none']
abattoir.owner = "blueprint"
abattoir.usage_limit = 1
abattoir.description = "Slaughter Cattle for Meat. Also receive 1 Hides for every 2 Cattle slaughtered."
abatr_get_quantity = requestblocks.GetQuantity('cattle')
abattoir.requests = [abatr_get_quantity]
abatr_give_cattle = actionblocks.RemoveItems('cattle', 1)
abatr_get_meat = actionblocks.AddItems('meat',1)
abatr_get_hide = actionblocks.AddItems('hides',0.5)
abattoir.actions = [abatr_give_cattle, abatr_get_meat, abatr_get_hide]

arts_center = Building()
arts_center.name = "arts center"
arts_center.build_cost = {'wood': 1, 'clay': 1}
arts_center.fees = [{'food' : 1}]
arts_center.rank = 11
arts_center.value = arts_center.price = 10
arts_center.type = "craftsman"
arts_center.icon = ['fisherman']
arts_center.owner = "blueprint"
arts_center.usage_limit = 1
arts_center.description = "Receive 4 Money for each player using your buildings."
artct_get_player = requestblocks.SelectPlayer()
arts_center.requests = [artct_get_player]
artct_collect_tickets = actionblocks.CollectTickets(4)
arts_center.actions = [artct_collect_tickets]

''' B '''
bakehouse = Building()
bakehouse.name = "bakehouse"
bakehouse.build_cost = {'clay': 2}
bakehouse.fees = [{'food' : 1}]
bakehouse.rank = 5
bakehouse.value = bakehouse.price = 8
bakehouse.type = "craftsman"
bakehouse.icon = ['none']
bakehouse.owner = "blueprint"
bakehouse.usage_limit = 1
bakehouse.description = "Bake Bread with Grain. Spend 1 Energy and receive 1 Money for every 2 Bread baked."
bakeh_get_quantity = requestblocks.GetQuantity('grain')
bakehouse.requests = [bakeh_get_quantity]
bakeh_give_grain = actionblocks.RemoveItems('grain', 1)
bakeh_spend_energy = actionblocks.SpendEnergy(0.5)
bakeh_get_bread = actionblocks.AddItems('bread',1)
bakeh_get_money = actionblocks.AddItems('money',0.5)
bakehouse.actions = [bakeh_give_grain, bakeh_spend_energy, bakeh_get_bread, bakeh_get_money]

black_market = Building()
black_market.name = "black market"
black_market.build_cost = {}
black_market.fees = [{'food' : 1}]
black_market.rank = 13
black_market.value = black_market.price = 2
black_market.type = "none"
black_market.icon = ['none']
black_market.owner = "blueprint"
black_market.usage_limit = 1
black_market.description = "Un-buildable. Collect 2 of each item whose offer space is empty."
blkmkt_get_empty_offers = requestblocks.GetEmptyOffers()
black_market.requests = [blkmkt_get_empty_offers]
blkmkt_collect_empty_offers = actionblocks.CollectEmptyOffers(2)
black_market.actions = [blkmkt_collect_empty_offers]

bank = Building()
bank.name = "bank"
bank.build_cost = {'brick': 4, 'steel': 1}
bank.fees = []
bank.rank = 29
bank.value = 16
bank.price = 40
bank.type = "economic"
bank.icon = ['none']
bank.owner = "blueprint"
bank.usage_limit = 0
bank.description = "Unusable. Endgame value. Industrial buildings add 3 value each. Economic buildings add 2 each."

brick_works = Building()
brick_works.name = "brickworks"
brick_works.build_cost = {'wood' : 2, 'clay' : 1, 'iron' : 1}
brick_works.fees = [{'food' : 1}]
brick_works.rank = 14
brick_works.value = brick_works.price = 14
brick_works.type = "industrial"
brick_works.icon = ['none']
brick_works.owner = "blueprint"
brick_works.usage_limit = 1
brick_works.description = "Make Bricks from Clay. Spend 1 Energy and receive 1 Money for every 2 Bricks made."
brkwrks_get_quantity = requestblocks.GetQuantity('clay')
brick_works.requests = [brkwrks_get_quantity]
brkwrks_give_clay = actionblocks.RemoveItems('clay', 1)
brkwrks_spend_energy = actionblocks.SpendEnergy(0.5)
brkwrks_get_brick = actionblocks.AddItems('brick',1)
brkwrks_get_money = actionblocks.AddItems('money',0.5)
brick_works.actions = [brkwrks_give_clay, brkwrks_spend_energy, brkwrks_get_brick, brkwrks_get_money]

bridge_over_seine = Building()
bridge_over_seine.name = "bridge over the seine"
bridge_over_seine.build_cost = {'iron' : 3}
bridge_over_seine.fees = [{'money' : 2}]
bridge_over_seine.rank = 27
bridge_over_seine.value = bridge_over_seine.price = 16
bridge_over_seine.type = "none"
bridge_over_seine.icon = ['none']
bridge_over_seine.owner = "blueprint"
bridge_over_seine.usage_limit = 1
bridge_over_seine.description = "Sell goods for money. Receive 1 Money for each upgraded item or 3 standard items."
bridge_select_items = requestblocks.SelectInventoryItems()
bridge_over_seine.requests = [bridge_select_items]
bridge_sell_items = actionblocks.SellItems(3,1)
bridge_over_seine.actions = [bridge_sell_items]

building_firm_a = Building()
building_firm_a.name = "building firm (a)"
building_firm_a.build_cost = {}
building_firm_a.fees = []
building_firm_a.rank = 0
building_firm_a.value = building_firm_a.price = 4
building_firm_a.type = "craftsman"
building_firm_a.icon = ['hammer']
building_firm_a.owner = "game"
building_firm_a.usage_limit = 1
building_firm_a.description = "Build 1 building from the available blueprints."
bfirma_get_blueprint = requestblocks.SelectBlueprint()
bfirma_get_player = requestblocks.SelectPlayer()
building_firm_a.requests = [bfirma_get_blueprint, bfirma_get_player]
bfirma_build = actionblocks.Construct({})
building_firm_a.actions = [bfirma_build]

building_firm_b = Building()
building_firm_b.name = "building firm (b)"
building_firm_b.build_cost = {}
building_firm_b.fees = [{'food' : 1}]
building_firm_b.rank = 0
building_firm_b.value = building_firm_b.price = 6
building_firm_b.type = "craftsman"
building_firm_b.icon = ['hammer']
building_firm_b.owner = "game"
building_firm_b.usage_limit = 1
building_firm_b.description = "Build 1 building from the available blueprints."
bfirmb_get_blueprint = requestblocks.SelectBlueprint()
bfirmb_get_player = requestblocks.SelectPlayer()
building_firm_b.requests = [bfirmb_get_blueprint, bfirmb_get_player]
bfirmb_build = actionblocks.Construct({})
building_firm_b.actions = [bfirmb_build]

business_office = Building()
business_office.name = "business office"
business_office.build_cost = {'wood' : 4, 'clay' : 1}
business_office.fees = [{'money' : 1}]
business_office.rank = 21
business_office.value = business_office.price = 12
business_office.type = "economic"
business_office.icon = ['hammer', 'fisherman']
business_office.owner = "blueprint"
business_office.usage_limit = 1
business_office.description = "Trade 4 goods for 1 Steel and/or 1 item for 1 Charcoal, Leather or Brick."
boffice_request_steel = requestblocks.SetTradeRequest(['steel'])
boffice_request_ChLeBr = requestblocks.SetTradeRequest(['charcoal', 'leather', 'brick'])
business_office.requests = [boffice_request_steel, boffice_request_ChLeBr]
boffice_trade_steel = actionblocks.TradeItems([('any',4)],['steel'])
boffice_trade_ChLeBr = actionblocks.TradeItems([('any',1)],['charcoal', 'leather', 'brick'])
business_office.actions = [boffice_trade_steel, boffice_trade_ChLeBr]

''' C '''
charcoal_kiln = Building()
charcoal_kiln.name = "charcoal kiln"
charcoal_kiln.build_cost = {'clay' : 1}
charcoal_kiln.fees = []
charcoal_kiln.rank = 7
charcoal_kiln.value = charcoal_kiln.price = 8
charcoal_kiln.type = "craftsman"
charcoal_kiln.icon = ['none']
charcoal_kiln.owner = "blueprint"
charcoal_kiln.usage_limit = 1
charcoal_kiln.description = "Convert Wood to Charcoal."
ckiln_get_quantity = requestblocks.GetQuantity('wood')
charcoal_kiln.requests = [ckiln_get_quantity]
ckiln_give_wood = actionblocks.RemoveItems('wood', 1)
ckiln_get_charcoal = actionblocks.AddItems('charcoal',1)
charcoal_kiln.actions = [ckiln_give_wood, ckiln_get_charcoal]

church = Building()
church.name = "church"
church.build_cost = {'wood' : 5, 'brick' : 3, 'iron' : 1}
church.fees = []
church.rank = 30
church.value = 26
church.price = 0
church.type = "public"
church.icon = ['none']
church.owner = "blueprint"
church.usage_limit = 1
church.description = "Un-purchasable. Receive an additional 5 Bread and 3 Fish if you have 5 Bread and 2 Fish."
church_check_resources = actionblocks.CheckResources({'bread' : 5, 'fish' : 2})
church_get_bread = actionblocks.ReceiveItems('bread', 5)
church_get_fish = actionblocks.ReceiveItems('fish', 3)
church.actions = [church_check_resources, church_get_bread, church_get_fish]

clay_mound = Building()
clay_mound.name = "clay mound"
clay_mound.build_cost = {}
clay_mound.fees = [{'food': 1}]
clay_mound.rank = 10
clay_mound.value = clay_mound.price = 2
clay_mound.type = "none"
clay_mound.icon = ['none']
clay_mound.owner = "blueprint"
clay_mound.usage_limit = 1
clay_mound.description = "Un-buildable. Receive 3 Clay plus an additional 1 Clay for each owned 'Hammer' buildings."
cmound_select_player = requestblocks.SelectPlayer()
clay_mound.requests = [cmound_select_player]
cmound_get_clay = actionblocks.ReceiveItems('clay',3, 'hammer', 1)
clay_mound.actions = [cmound_get_clay]

cokery = Building()
cokery.name = "cokery"
cokery.build_cost = {'brick' : 2, 'iron' : 2}
cokery.fees = [{'money' : 1}]
cokery.rank = 25
cokery.value = cokery.price = 18
cokery.type = "industrial"
cokery.icon = ['none']
cokery.owner = "blueprint"
cokery.usage_limit = 1
cokery.description = "Convert Coal to Coke. Receive 1 Money for every Coke made."
cokery_get_quantity = requestblocks.GetQuantity('coal')
cokery.requests = [cokery_get_quantity]
cokery_give_coal = actionblocks.RemoveItems('coal', 1)
cokery_get_coke = actionblocks.AddItems('coke',1)
cokery_get_money = actionblocks.AddItems('money',1)
cokery.actions = [cokery_give_coal, cokery_get_coke, cokery_get_money]

colliery = Building()
colliery.name = "colliery"
colliery.build_cost = {'wood': 1, 'clay': 3}
colliery.fees = [{'food': 2}]
colliery.rank = 16
colliery.value = colliery.price = 10
colliery.type = "industrial"
colliery.icon = ['none']
colliery.owner = "blueprint"
colliery.usage_limit = 1
colliery.description = "Receive 3 Coal plus an additional 1 Coal if you own any 'Hammer' buildings."
colliery_select_player = requestblocks.SelectPlayer()
colliery.requests = [colliery_select_player]
colliery_get_coal = actionblocks.ReceiveItems('coal',3, 'hammer', 1, 1)
colliery.actions = [colliery_get_coal]

construction_firm = Building()
construction_firm.name = "construction firm"
construction_firm.build_cost = {}
construction_firm.fees = [{'food' : 2}]
construction_firm.rank = 0
construction_firm.value = construction_firm.price = 8
construction_firm.type = "industrial"
construction_firm.icon = ['hammer']
construction_firm.owner = "game"
construction_firm.usage_limit = 2
construction_firm.description = "Build up to 2 buildings from the available blueprints."
cfirm_get_blueprint = requestblocks.SelectBlueprint()
cfirm_get_player = requestblocks.SelectPlayer()
construction_firm.requests = [cfirm_get_blueprint, cfirm_get_player]
cfirm_build = actionblocks.Construct({})
construction_firm.actions = [cfirm_build]

''' D '''
dock = Building()
dock.name = "dock"
dock.build_cost = {'wood': 1, 'brick': 2, 'iron': 2}
dock.fees = []
dock.rank = 26
dock.value = 10
dock.price = 24
dock.type = "industrial"
dock.icon = ['none']
dock.owner = "blueprint"
dock.usage_limit = 0
dock.description = "Unusable. Endgame value. Ships add 4 value each."

''' F '''
fishery = Building()
fishery.name = "fishery"
fishery.build_cost = {'wood': 1, 'clay': 1}
fishery.fees = []
fishery.rank = 3
fishery.value = fishery.price = 10
fishery.type = "commercial"
fishery.icon = ['fisherman']
fishery.owner = "blueprint"
fishery.usage_limit = 1
fishery.description = "Receive 3 Fish plus an additional 1 Fish for each owned 'Fisherman' buildings."
fishery_select_player = requestblocks.SelectPlayer()
fishery.requests = [fishery_select_player]
fishery_get_fish = actionblocks.ReceiveItems('fish',3, 'fisherman', 1)
fishery.actions = [fishery_get_fish]

''' G '''
grocery = Building()
grocery.name = "grocery market"
grocery.build_cost = {'wood' : 1, 'brick' : 1}
grocery.fees = [{'money': 1}]
grocery.rank = 19
grocery.value = grocery.price = 10
grocery.type = "economic"
grocery.icon = ['none']
grocery.owner = "blueprint"
grocery.usage_limit = 1
grocery.description = "Receive 1 Cattle, 1 Meat, 1 Fish, 1 Smoked Fish, 1 Grain and 1 Bread."
grocery_get_cattle = actionblocks.ReceiveItems('cattle', 1)
grocery_get_meat = actionblocks.ReceiveItems('meat', 1)
grocery_get_fish = actionblocks.ReceiveItems('fish', 1)
grocery_get_smokedfish = actionblocks.ReceiveItems('smoked fish', 1)
grocery_get_grain = actionblocks.ReceiveItems('grain', 1)
grocery_get_bread = actionblocks.ReceiveItems('bread', 1)
grocery.actions = [grocery_get_cattle, grocery_get_meat, grocery_get_fish, grocery_get_smokedfish, grocery_get_grain, grocery_get_bread]

''' H '''
hardware = Building()
hardware.name = "hardware store"
hardware.build_cost = {'wood' : 3, 'clay' : 1}
hardware.fees = [{'food': 1}]
hardware.rank = 6
hardware.value = hardware.price = 8
hardware.type = "commercial"
hardware.icon = ['hammer', 'fisherman']
hardware.owner = "blueprint"
hardware.usage_limit = 1
hardware.description = "Receive 1 Wood, 1 Brick and 1 Iron."
hardware_get_wood = actionblocks.ReceiveItems('wood', 1)
hardware_get_brick = actionblocks.ReceiveItems('brick', 1)
hardware_get_iron = actionblocks.ReceiveItems('iron', 1)
hardware.actions = [hardware_get_wood, hardware_get_brick, hardware_get_iron]

''' I '''
ironworks = Building()
ironworks.name = "ironworks"
ironworks.build_cost = {'wood': 1, 'brick': 2}
ironworks.fees = [{'food': 3}, {'money': 1}]
ironworks.rank = 22
ironworks.value = ironworks.price = 12
ironworks.type = "industrial"
ironworks.icon = ['hammer']
ironworks.owner = "blueprint"
ironworks.usage_limit = 1
ironworks.description = "Receive 3 Iron. An additional 1 Iron is available for 6 Energy."
ironworks_get_energy = requestblocks.GetQuantity ('energy')
ironworks.requests = [ironworks_get_energy]
ironworks_spend_energy = actionblocks.SpendEnergy(1)
ironworks_get_addon = actionblocks.AddItems('iron',0.17)
ironworks_get_iron = actionblocks.ReceiveItems('iron', 3)
ironworks.actions = [ironworks_spend_energy, ironworks_get_addon, ironworks_get_iron]

''' J '''
joinery = Building()
joinery.name = "joinery"
joinery.build_cost = {'wood': 3}
joinery.fees = [{'food': 1}]
joinery.rank = 4
joinery.value = joinery.price = 8
joinery.type = "commercial"
joinery.icon = ['hammer']
joinery.owner = "blueprint"
joinery.usage_limit = 1
joinery.description = "Sell 1-3 Wood for 5-7 Money."
joinery_exchange_wood = requestblocks.GetExchangeRequest('wood', [1,2,3])
joinery.requests = [joinery_exchange_wood]
joinery_get_money = actionblocks.ExchangeItem('money',[5,6,7])
joinery.actions = [joinery_get_money]

''' L '''
court = Building()
court.name = "local court"
court.build_cost = {'wood': 3, 'clay': 2}
court.fees = []
court.rank = 15
court.value = court.price = 16
court.type = "public"
court.icon = []
court.owner = "blueprint"
court.usage_limit = 1
court.description = "Close Loans. If you have 1, close it. If you have 2, close 1 and get 2 Money. If you have more, close 2."
court_close_loans = actionblocks.CloseLoans()
court.actions = [court_close_loans]

''' M '''
market = Building()
market.name = "marketplace"
market.build_cost = {'wood': 2}
market.fees = [{'food': 2}, {'money': 1}]
market.rank = 1
market.value = market.price = 6
market.type = "none"
market.icon = []
market.owner = "blueprint"
market.usage_limit = 1
market.description = "Receive 2 different standard item and an additional item for each owned 'Craftsman' building."
market_select_player = requestblocks.SelectPlayer()
market.requests = [market_select_player]
market_collect_items = actionblocks.CollectStandardItems(2,'craftsman')
market.actions = [market_collect_items]

''' S '''
sawmill = Building()
sawmill.name = "sawmill"
sawmill.build_cost = {'clay': 1, 'iron': 1}
sawmill.fees = []
sawmill.rank = 2
sawmill.value = sawmill.price = 14
sawmill.type = "industrial"
sawmill.icon = ['hammer']
sawmill.owner = "blueprint"
sawmill.usage_limit = 1
sawmill.description = "Build 1 building from the available blueprints that requires wood using 1 less wood."
sawmill_get_blueprint = requestblocks.SelectBlueprint('wood')
sawmill_get_player = requestblocks.SelectPlayer()
sawmill.requests = [sawmill_get_blueprint, sawmill_get_player]
sawmill_build = actionblocks.Construct({'wood': 1})
sawmill.actions = [sawmill_build]

shipping_line = Building()
shipping_line.name = "shipping line"
shipping_line.build_cost = {'wood': 2, 'brick': 3}
shipping_line.fees = [{'food': 2}]
shipping_line.rank = 18
shipping_line.value = shipping_line.price = 10
shipping_line.type = "economic"
shipping_line.icon = ['fisherman']
shipping_line.owner = "blueprint"
shipping_line.usage_limit = 1
shipping_line.description = "Ship goods for 3 Energy per loaded ship."
shipping_line_get_player = requestblocks.SelectPlayer()
shipping_line_get_shipment = requestblocks.GetShipment()
shipping_line.requests = [shipping_line_get_shipment, shipping_line_get_player]
shipping_line_do_shipping = actionblocks.DoShipping()
shipping_line.actions = [shipping_line_do_shipping]

smokehouse = Building()
smokehouse.name = "smokehouse"
smokehouse.build_cost = {'wood': 2, 'clay': 3}
smokehouse.fees = [{'food': 2}, {'money': 1}]
smokehouse.rank = 8
smokehouse.value = smokehouse.price = 6
smokehouse.type = "commercial"
smokehouse.icon = ['fisherman']
smokehouse.owner = "blueprint"
smokehouse.usage_limit = 1
smokehouse.description = "Make upto 6 Smoked Fish from Fish for 1 Energy. Receive 1 Money for every 3 Fish smoked."
smokehouse_get_quantity = requestblocks.GetQuantity('fish', 6)
smokehouse.requests = [smokehouse_get_quantity]
smokehouse_give_fish = actionblocks.RemoveItems('fish', 1)
smokehouse_spend_energy = actionblocks.SpendEnergy(0, 1)
smokehouse_get_smoked_fish = actionblocks.AddItems('smoked fish',1)
smokehouse_get_money = actionblocks.AddItems('money',0.34)
smokehouse.actions = [smokehouse_give_fish, smokehouse_spend_energy, smokehouse_get_smoked_fish, smokehouse_get_money]

''' T '''
tannery = Building()
tannery.name = "tannery"
tannery.build_cost = {'wood': 1, 'brick': 1}
tannery.fees = []
tannery.rank = 20
tannery.value = tannery.price = 12
tannery.type = "commercial"
tannery.icon = []
tannery.owner = "blueprint"
tannery.usage_limit = 1
tannery.description = "Make upto 4 Leather from Hides. Receive 1 money for every Hide tanned."
tannery_get_quantity = requestblocks.GetQuantity('hides', 4)
tannery.requests = [tannery_get_quantity]
tannery_give_hides = actionblocks.RemoveItems('hides', 1)
tannery_get_leather = actionblocks.AddItems('leather', 1)
tannery_get_money = actionblocks.AddItems('money', 1)
tannery.actions = [tannery_give_hides, tannery_get_leather, tannery_get_money]

town_hall = Building()
town_hall.name = "town hall"
town_hall.build_cost = {'wood': 4, 'brick': 3}
town_hall.fees = []
town_hall.rank = 28
town_hall.value = 6
town_hall.price = 30
town_hall.type = "public"
town_hall.icon = []
town_hall.owner = "blueprint"
town_hall.usage_limit = 0
town_hall.description = "Unusable. Endgame value. Each Public buildings add 4 value and Craftsman buildings add 2 value."

''' W '''
wharf1 = Building()
wharf1.name = "wharf 1"
wharf1.build_cost = {'wood': 2, 'clay': 2, 'iron': 2}
wharf1.fees = [{'food': 2}]
wharf1.rank = 12
wharf1.value = wharf1.price = 14
wharf1.type = "industrial"
wharf1.icon1 = []
wharf1.owner = "blueprint"
wharf1.usage_limit = 1
wharf1.description = "Build an available ship. "
wharf1.non_modern_desc = "Must be modernized with a 'Brick' once to build non-wooden ships."
wharf1.modern_desc = "Modernized. Can build all ships."
wharf1.modernized = False
wharf1_get_ship = requestblocks.SelectShipType()
wharf1_get_player = requestblocks.SelectPlayer()
wharf1.requests = [wharf1_get_ship, wharf1_get_player]
wharf1_build_ship = actionblocks.BuildShip(wharf1)
wharf1.actions = [wharf1_build_ship]

wharf2 = Building()
wharf2.name = "wharf 2"
wharf2.build_cost = {'wood': 2, 'clay': 2, 'iron': 2}
wharf2.fees = [{'food': 2}]
wharf2.rank = 17
wharf2.value = wharf1.price = 14
wharf2.type = "industrial"
wharf2.icon1 = []
wharf2.owner = "blueprint"
wharf2.usage_limit = 1
wharf2.description = "Build an available ship. "
wharf2.non_modern_desc = "Must be modernized with a 'Brick' once to build non-wooden ships."
wharf2.modern_desc = "Modernized. Can build all ships."
wharf2.modernized = False
wharf2_get_ship = requestblocks.SelectShipType()
wharf2_get_player = requestblocks.SelectPlayer()
wharf2.requests = [wharf2_get_ship, wharf2_get_player]
wharf2_build_ship = actionblocks.BuildShip(wharf2)
wharf2.actions = [wharf2_build_ship]
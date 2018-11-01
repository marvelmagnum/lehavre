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
    current_user = "none"  #users: none, p1, p2, ...
    usage_limit = 0
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
abattoir.fees = {'money' : 2}
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
arts_center.fees = {'food' : 1}
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
bakehouse.fees = {'food' : 1}
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
black_market.fees = {'food' : 1}
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
bank.fees = {}
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
brick_works.fees = {'food' : 1}
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
bridge_over_seine.fees = {'money' : 2}
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
building_firm_a.fees = {}
building_firm_a.rank = 0
building_firm_a.value = building_firm_a.price = 4
building_firm_a.type = "craftsman"
building_firm_a.icon = ['hammer']
building_firm_a.owner = "none"
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
building_firm_b.fees = {'food' : 1}
building_firm_b.rank = 0
building_firm_b.value = building_firm_b.price = 6
building_firm_b.type = "craftsman"
building_firm_b.icon = ['hammer']
building_firm_b.owner = "none"
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
business_office.fees = {'money' : 1}
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
charcoal_kiln.fees = {}
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
church.fees = {}
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
clay_mound.fees = {'food': 1}
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
cokery.fees = {'money' : 1}
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
colliery.fees = {'food': 2}
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
construction_firm.fees = {'food' : 2}
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
dock.fees = {}
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
fishery.fees = {}
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
grocery.fees = {'money': 1}
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
hardware.fees = {'food': 1}
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
ironworks.name = "hardware store"
ironworks.build_cost = {'wood' : 3, 'clay' : 1}
ironworks.fees = {'food': 3} # food or money ??
ironworks.rank = 22
ironworks.value = ironworks.price = 12
ironworks.type = "industrial"
ironworks.icon = ['hammer', 'fisherman']
ironworks.owner = "blueprint"
ironworks.usage_limit = 1
ironworks.description = "Receive 3 Iron. An additional 1 Iron is available for 6 Energy."
ironworks_get_wood = actionblocks.ReceiveItems('wood', 1)
ironworks_get_brick = actionblocks.ReceiveItems('brick', 1)
ironworks_get_iron = actionblocks.ReceiveItems('iron', 1)
ironworks.actions = []
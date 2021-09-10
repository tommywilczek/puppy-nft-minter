from brownie import AdvancedCollectible, accounts, config, interface, network

def get_breed(breed_number):
    breed_dict = {0: 'PUG', 1: 'SHIBA_INU', 2: 'ST_BERNARD'}
    return breed_dict[breed_number]

def fund_advanced_collectible(nft_contract):
    devAccount = accounts.add(config['wallets']['from_key'])
    link_token = interface.LinkTokenInterface(config['networks'][network.show_active()]['link_token'])
    link_token.transfer(nft_contract, 100000000000000000, {"from": devAccount})
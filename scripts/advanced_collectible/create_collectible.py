from brownie import AdvancedCollectible, accounts, config
from scripts.helpful_scripts import get_breed
import time

def main():
    devAccount = accounts.add(config['wallets']['from_key'])
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    transaction = advanced_collectible.createCollectible("None", {"from": devAccount})
    transaction.wait(1)
    request_id = transaction.events['requestedCollectible']['requestId']
    token_id = advanced_collectible.requestIdToTokenId(request_id)
    time.sleep(35) # wait for collectible to be funded with LINK
    breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
    print('Dog breed of token_id {} is {}'.format(token_id, breed))
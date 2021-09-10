from brownie import AdvancedCollectible
from scripts.helpful_scripts import fund_advanced_collectible

def main():
    # funds most recently minted collectible
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    fund_advanced_collectible(advanced_collectible)
from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000
LOCAL_BLOCKCHAIN_ENV = ['development', 'ganache-local']
FORKED_LOCAL_ENV = ['mainnet-fork-dev']

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENV or network.show_active() in FORKED_LOCAL_ENV:
        return accounts[0]
    else:
        # account = accounts.load("my-account")
        # print(account)
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f'The active network is {network.show_active()}')
    print('Deploying mocks...  ')
    if len(MockV3Aggregator) < 1:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("Mocks Deployed!!")
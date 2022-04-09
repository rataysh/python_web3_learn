from web3 import Web3
import json
from old_projects.keys import https_infura_mainnet

# infura_url = https_infura_kovan
# infura_url = https_infura_goerli
infura_url = https_infura_mainnet
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())

print(web3.eth.blockNumber)
balance_1 = web3.eth.getBalance()
balance_2 = web3.eth.getBalance()
print(Web3.fromWei(balance_1, 'ether'))
print(Web3.fromWei(balance_2, 'ether'))

# Проверяем инфу о токенах из ERC20 mainnet
abi = json.loads()
address = ''
contract = web3.eth.contract(address=address, abi=abi)
#
totalSupply = contract.functions.totalSupply().call()
print(Web3.fromWei(totalSupply, 'ether'))
print(contract.functions.name().call())
print(contract.functions.symbol().call())
balance = contract.functions.balanceOf('').call()
print(web3.fromWei(balance, 'ether'))


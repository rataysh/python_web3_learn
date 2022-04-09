from web3 import Web3
import json

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())
web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.loads('[{"inputs":[],"name":"Greeter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"greet","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
address = web3.toChecksumAddress("0xBFf9201698cC6B342977185c4D181Ce031E46f46")
GreeterContr = web3.eth.contract(address=address, abi=abi)
print(GreeterContr.functions.greet().call())

tx_hash = GreeterContr.functions.setGreeting('Nomber_2').transact()

web3.eth.waitForTransactionReceipt(tx_hash)
print('Updated greeting: {}'.format(
    GreeterContr.functions.greet().call()
))




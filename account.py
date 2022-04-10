from web3 import Web3
import json
from keys import https_infura_mainnet, https_infura_kovan, https_infura_goerli


# infura_url = https_infura_kovan
# infura_url = https_infura_goerli
infura_url = https_infura_mainnet
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())
## получение информации из блока в сети Ethereum
print(web3.eth.blockNumber)
latest_block = web3.eth.blockNumber
print(web3.eth.getBlock(latest_block))

# Создание и работа с новым аккаунтом:
account = web3.eth.account.create()
print(account.privateKey.hex())
keystore = account.encrypt('qwerty')
print(keystore)
print(web3.eth.account.decrypt(keystore, 'qwerty').hex())
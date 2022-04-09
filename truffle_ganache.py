from web3 import Web3


ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())

account_1 = "0x193B4e678c507b8cd990f134Ee33855A062984C2"
account_2 = "0x2481eA2EF56E5Ea6a1f6E442FA6024508B91A11c"

private_key = "4f43c5eb572fceaeda8d0cbb68a276bf40465fa479c91918d528d8066f50368f"

#Создаем nonce
nonce = web3.eth.getTransactionCount(account_1)
#Создаем транзакцию в ganache
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(10, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

#Подписываем транзакцию
signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(tx_hash.hex()) # .hex() для отображения в правильной кодировке
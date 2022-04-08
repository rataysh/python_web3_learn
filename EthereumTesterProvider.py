from web3 import Web3


# Основные команды в  web3 (Часть 1)
w3 = Web3(Web3.EthereumTesterProvider()) #Тестовый блокчейн
print(Web3.toWei(1, 'ether')) #1 eth в еденицах Wei

print(w3.isConnected()) #Проверка соединения (должно быть True)
print(w3.eth.accounts) #Тестовые аккаунты
print(w3.eth.get_balance(w3.eth.accounts[0]))
print(w3.eth.get_balance(w3.eth.accounts[1])) #баланс 1-го в Wei
print(w3.eth.get_block('latest')) #Информация по последнему блоку
# Создадим новую транзакцию
tx_hash = w3.eth.send_transaction({
   'from': w3.eth.accounts[0],
   'to': w3.eth.accounts[1],
   'value': w3.toWei(3, 'ether')
})
print(w3.eth.wait_for_transaction_receipt(tx_hash)) #Иметируем работу майнеров
print(w3.eth.get_balance(w3.eth.accounts[0]))
print(w3.eth.get_balance(w3.eth.accounts[1]))
print(w3.eth.get_transaction(tx_hash)) #Информация о транзакции

# Основные команды в  web3 (Часть 2)
w3 = Web3(Web3.EthereumTesterProvider())
acct_one = w3.eth.accounts[0]
print(acct_one)
print(w3.eth.get_balance(acct_one))
# Создаем отдельный аккаунт не в тестируемой сети (EthereumTesterProvider)
acct_two = w3.eth.account.create()
print(acct_two.address)
print(acct_two.key.hex()) # .hex() для отображения в правильной кодировке
# Для транзакции  такого аккаунта нужно 3 действия

tx_hash = w3.eth.send_transaction({
	'from': acct_one,
	'to': acct_two.address,
	'value': Web3.toWei(1, 'ether')
})
tx = {
	'to': acct_one,
	'value': 10000000,
	'gas': 21000,
	'gasPrice': w3.eth.get_block('pending')['baseFeePerGas'],
	'nonce': 0 # nonce - это просто количество транзакций на счете. Протокол Ethereum отслеживает это значение для предотвращения двойных трат.
} # 1) вручную создать транзакцию
signed = w3.eth.account.sign_transaction(tx, acct_two.key) # 2) подписать транзакцию закрытым ключом отправителя
tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction) # 3) отправить "raw" транзакцию
print(w3.eth.get_balance(acct_one))

# взаимодействовать с существующим контрактом:
# myContract = web3.eth.contract(address=address, abi=abi)
# twentyone = myContract.functions.multiply7(3).call()

# развернуть новый контракт:
# Example = w3.eth.contract(abi=abi, bytecode=bytecode)
# tx_hash = Example.constructor().transact()
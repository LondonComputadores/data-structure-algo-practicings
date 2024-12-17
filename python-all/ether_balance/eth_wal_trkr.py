from requests import get
from datetime import datetime

API_KEY = 'NC7PCVVP43YJTQXAEFD6H6ZXHI751HGFFY'
BASE_URL = 'https://api.etherscan.io/api'
ETHER_VALUE = 10 ** 18
address = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D'
contractaddress=0xaaaebe6fe48e54f431b0c390cfaf0b017d09d42d

def make_api_url(module, action, address, **kwargs):
	
	url = BASE_URL + f'?module={module}&action={action}&address={address}&apikey={API_KEY}'

	for key, value in kwargs.items():
		url += f'&{key}={value}'

	return url

def get_account_balance(address):
	get_balance_url = make_api_url('account', 'balance', address=address, tag='latest')
	response = get(get_balance_url)
	data = response.json()
	value = data #/ ETHER_VALUE
	# value = int(data['result']) / ETHER_VALUE
	return value

def get_total_supply(address):
	get_total_url = make_api_url('token', 'tokenholderlist', address=address, contractaddress=contractaddress, page=1, offset=10)
	response = get(get_total_url)
	data = response.json()
	value = data #/ ETHER_VALUE
	# value = int(data['result']) / ETHER_VALUE
	return value

# def get_transactions(address):
# 	get_transactions_url = make_api_url('account', 'txlist', address, startblock=0, endblock=99999999, page=1, offset=10000, sort='asc')
# 	response = get(get_transactions_url)
# 	data = response.json()['result']
# 	for tx in data:
# 		to = tx['to']
# 		from_addr = tx['from']
# 		value = tx['value']
# 		gas = tx['gasUsed']
# 		time = datetime.fromtimestamp(int(tx['timeStamp']))
# 		print('--------------------')
# 		print('To:', to)
# 		print('From:', from_addr)
# 		print('Value:', value)
# 		print('Gas Used:', gas)
# 		print('Time:', time)
		


eth = get_account_balance(address)
print(eth)

total_sup = get_total_supply(address)
print(total_sup)

# get_transactions(address)




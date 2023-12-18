import json
from web3 import Web3

#specify which blockchain using a rpc url
rpc_url = "https://sepolia-rpc.scroll.io/"
# connection to the blockchain
web3 = Web3(Web3.HTTPProvider(rpc_url))

abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"stateMutability":"view","type":"function"}]')

address ="0x268d4A9c3Ba20C938B9f3Db634786aB93628A7Cb"

contract = web3.eth.contract(address=address,abi=abi)
# Call the greet variable
greet_value = contract.functions.greet().call()

print("Greet value:", greet_value)
from web3 import Web3
import time
import sys

url = "HTTP://127.0.0.1:7545" #Ganache RPC server

web3 = Web3(Web3.HTTPProvider(url))
account = input("Enter your Account number : ")
while(1):
	print("Enter your choice : ")
	print("1. Get Balance")
	print("2. Transfer")
	print("3. Exit")
	c = int(input())
	if(c==1):
		try:
			balance = web3.fromWei(web3.eth.getBalance(account),'ether')
			print("\n")
			print("Balance : ",balance)
			print("\n")
		except:
			print("Wrong account number! Exiting...")
			time.sleep(3)
			sys.exit()
	if(c==2):
		try:
			print("\n")
			account2 = input("Enter the destination account : ")
			amount = int(input("Enter the amount to Send : "))
			pvtKey = input("Enter your Private Key : ")
			nonce = web3.eth.getTransactionCount(account)
			tx={
				'nonce': nonce,
				'to': account2,
				'value': web3.toWei(amount,'ether'),
				'gas': 2000000,
				'gasPrice': web3.toWei('50', 'gwei')
				}
			signed_tx = web3.eth.account.signTransaction(tx, pvtKey)
			tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
			print("Transaction successful!")
			print("Transaction Hash:  ",web3.toHex(tx_hash))
			balance = web3.fromWei(web3.eth.getBalance(account),'ether')
			print("Account balance after Transaction : ",balance)
			print("\n")
		except:
			print("Transaction failed! Try Again...")
			time.sleep(2)
	if(c==3):
		print("Exiting...")
		time.sleep(1)
		sys.exit()

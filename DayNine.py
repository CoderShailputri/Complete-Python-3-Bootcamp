#Day Nine

#Create bank account class with 2 attributes and two methods
class Account:
	def __init__(self,owner,balance):
		self.owner = owner
		self.balance = balance
	def deposit(self, amt):
		print("Deposit accepted")
		self.balance = self.balance + amt
	def withdraw(self, amt):
		if amt<= self.balance: #Condition that withdrawls should not exceed available balance
			print("Withdrawl accepted")
			self.balance = self.balance - amt
		else:
			print ("Funds Unavailable!")
	def __str__(self):
		return f"Account owner : {self.owner}\nAccount balance : ${self.balance}" #Remember this will have a return

acc1 = Account('Jose',100)
print(acc1)
print(acc1.owner)
print(acc1.balance)
acc1.deposit(50)
print("Now the balance is:{}".format(acc1.balance))
acc1.withdraw(75)
print("Now the balance is:{}".format(acc1.balance))
acc1.withdraw(500)
print("Now the balance is:{}".format(acc1.balance))







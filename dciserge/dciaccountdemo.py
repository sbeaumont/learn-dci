"""
DCI proof of concept
Author: Serge Beaumont
Created: 1 October 2008
Edit 4 dec 2011: Tidying up and changing names to true DCI naming.
"""
from moneytransfer import MoneyTransfer

class Account(object):
	"""An Account is a Domain object that represents any kind of account."""
	def __init__(self):
		super(Account, self).__init__()
		self.balance = 0

if __name__ == '__main__':
	# Initialize the test case
	myAccount = Account()
	myAccount.balance = 1000
	yourAccount = Account()

	print "Balance of my account: ", myAccount.balance
	print "Balance of your account: ", yourAccount.balance

	print "Transferring 200 money..."
	context = MoneyTransfer()
	context.transfer(myAccount, yourAccount, 200)
	
	print "Balance of my account: ", myAccount.balance
	print "Balance of your account: ", yourAccount.balance
	
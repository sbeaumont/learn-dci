from moneytransfer import MoneyTransfer

# -------------------------------------------------- Data

class Account(object):
	def __init__(self, amount):
		self.balance = amount
		super(Account, self).__init__()

# -------------------------------------------------- MAIN

if __name__ == '__main__':
	src = Account(1000)
	dst = Account(0)
	transferAmount = 100

	print "Source account", src, "has a balance of", src.balance
	print "Destination account", dst, "has a balance of", dst.balance
	print "Transferring", transferAmount, "from source to destination."
	
	t = MoneyTransfer(src, dst)
	t.transfer(transferAmount)

	print "Source account", src, "now has a balance of", src.balance
	print "Destination account", dst, "now has a balance of", dst.balance
	print
	print "The following test shows that you can't use object equality"
	print "because an object is wrapped in a Role. However, for all other"
	print "purposes the Role base class does magic to make this wrapping"
	print "totally transparent."
	print
	print "Object equality?", dst == t.sink

from moneytransfer import MoneyTransfer

# ====================================================================

class Account(object):
	def __init__(self, amount):
		self.balance = amount
		super(Account, self).__init__()

# ====================================================================

if __name__ == '__main__':
	src = Account(1000)
	dst = Account(0)

	t = MoneyTransfer(src, dst)
	t.transfer(100)

	print src.balance
	print dst.balance
	
	print "Object equality?", dst == t.sink

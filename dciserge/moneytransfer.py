from dciserge import Context

class MoneyTransfer(Context):
	def __init__(self):
		super(MoneyTransfer, self).__init__()

	def wire(self):
		self.addRole(self.source, MoneySource)
		self.addRole(self.sink, MoneySink)
		
	def unwire(self):
		self.removeRole(self.source, MoneySource)
		self.removeRole(self.sink, MoneySink)

	def transfer(self, source, sink, amount):
		self.source = source
		self.sink = sink

		self.wire();
		source.transferTo(amount, self.sink)
		self.unwire();

class MoneySource():
	"""Transfers money to a MoneySink"""
	
	def transferTo(self, amount, sink):
		if self.balance >= amount:
			self.withdraw(amount)
			sink.receive(amount)
		else:
			print "Balance too low to allow withdraw"

	def withdraw(self, amount):
		self.balance -= amount

class MoneySink():
	"""Can accept money."""
	
	def receive(self, amount):
		self.balance += amount


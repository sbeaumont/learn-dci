from dci import Role

# -------------------------------------------------- Role base class

class HasABalance(Role):
	"""Yay, we can do this in Python. If a Data object does not have an attribute yet,
	just initialize it to a sensible value..."""
	def __init__(self, ob, context=None):
		if not hasattr(self, "balance"):
			self.balance = 0

# -------------------------------------------------- Context

class MoneyTransfer():
	"""
	Transfer money from a source to a sink.
	
	This context attaches roles to the objects it gets as it gets constructed.
	This means that an instance of this Context needs to be constructed for each
	unique "one-way pipeline" of money.
	"""

	def __init__(self, source, sink):
		self.source = MoneySource(source)
		self.sink = MoneySink(sink)

	def transfer(self, amount):
		self.source.transferTo(self.sink, amount)

# -------------------------------------------------- Roles

class MoneySource(HasABalance):	
	def transferTo(self, sink, amount):
		if self.balance >= amount:
			self.balance -= amount
			sink.receive(amount)
			print "Here", sink, "have", amount, "from me,", self

class MoneySink(HasABalance):
	def receive(self, amount):
		self.balance += amount
from dci import Role
from moneytransfer import MoneyTransfer

# -------------------------------------------------- Role base class

class RoleThatCanFindOtherRolePlayers(Role):
	"""
	Role class that can look up attributes from an embedded context.
	This is a way that we could look up other RolePlayers other than 'injection' by the Context.
	"""
	
	def findByName(self, name):
		"""Returns value of an attribute of context by name."""
		return getattr(self.__context__, name)


# -------------------------------------------------- Context

class RomeoAndJulietPlay():
	"""
	A Context setting the stage for a Shakespeare play. Very direct analogy of DCI to acting.
	
	This context shows another way to attach Data objects to roles, through setters.
	"""
	
	def setMaleLead(self, actor):
		self.romeo = Romeo(actor)

	def setFemaleLead(self, actor):
		self.juliet = Juliet(actor, self)

	def sceneOne(self):
		"Here is a case where a Context plays a Role by being part of a MoneyTransfer."
		self.balance = 1000
		nested = MoneyTransfer(self, self.juliet)
		nested.transfer(self.balance)
		print self.juliet.name(), "is a rich girl with", self.juliet.balance, "ducats to her name."
		
		self.juliet.whereArtThou("romeo")
		
		self.romeo.lendMoneyFrom(self.juliet, 100)

# -------------------------------------------------- Roles

class Romeo(Role):
	def name(self):
		return "Romeo"
	
	def lendMoneyFrom(self, other, amount):
		"""
		Oh, that Romeo is such a deadbeat. Always lending money. Tsk.
		Incidentally shows a case where a Role kicks off a nested context.
		Note that this will fail if the Data Objects don't have a balance...
		"""
		print self.name(), "sayeth: 'Could thou lendeth me the pitiful sum of", amount, "ducats?'"
		
		nested = MoneyTransfer(other, self)
		nested.transfer(amount)
		
		print "'Oh, thank thee! I now have", self.balance, "lovely, shiny ducats to my name!"

class Juliet(RoleThatCanFindOtherRolePlayers):
	def name(self):
		return "Juliet"
	
	def whereArtThou(self, name):
		"""Illustrates the retrieval of another roleplayer through an embedded context."""
		thou = self.findByName(name)
		print self.name(), "asketh: '" + name + ",", name + ",", "where art thou", name + "?'."
		print "And", thou, "respondeth: '" + thou.name(), "is my name!'."
	
	
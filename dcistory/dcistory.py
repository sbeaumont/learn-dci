from dci import Role, Data
from romeoandjuliet import RomeoAndJulietPlay

class Person(Role):
	pass
	
class ADayAtTheTheater():
	"""This context attaches roles in the 'use case' method. Note that it is stateless."""
	
	def doShakespeare(self, male, female):
		bob = Person(male)
		annie = Person(female)

		print "The Magical Theater says: 'Welcome, you two!'"
		print
		print "'You,", bob, "I name Bob.'"
		print "'You,", annie, "I name Annie.'"

		print "'You'll be in a play!'"
		play = RomeoAndJulietPlay()
		print "'Bob, you'll be the male lead, and Annie, you'll be the female lead.'"
		play.setMaleLead(bob)
		play.setFemaleLead(annie)
		print "'Let scene one commence!'"
		print
		play.sceneOne()
		print
		print "The Magical Theater says: 'Did you like the play?'"

if __name__ == '__main__':

	# On purpose, we start with the most basic of objects...
	obj1 = Data()
	obj2 = Data()

	# Somewhere a balance is used, violation of encapsulation?
	# I guess that normally you'd pull a Data object out of a DB,
	# and that a vanilla object would get its data as it goes
	# though contexts.
	# Edit: I changed the MoneySource Role to add the attribute if it's not there. Good practice?
	# Edit2: I had the Romeo and Juliet do a MoneyTransfer to set up her riches...
	#obj1.balance = 0
	#obj2.balance = 1000
	
	print "Two data objects,", obj1, "and", obj2, "enter a theater."
	print
	
	context = ADayAtTheTheater()
	context.doShakespeare(obj1, obj2)
	
	print
	print obj1, "wonders where it got a balance of", obj1.balance
	print obj2, "wonders where it got a balance of", obj2.balance
	print "They say it's a Magical Theater..."
	

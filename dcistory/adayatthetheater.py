""""
adayatthetheater.py

Created by Serge Beaumont on 2011-12-05.
"""
from dci import Role
from romeoandjuliet import RomeoAndJulietPlay

# -------------------------------------------------- Context

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

# -------------------------------------------------- Roles

class Person(Role):
	"""Don't really know anything useful to do for this role, 
	but needed one to show the role wrapping used here."""
	pass
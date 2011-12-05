from dci import Data
from adayatthetheater import ADayAtTheTheater

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
	print "..."
	print "They say it's a Magical Theater..."

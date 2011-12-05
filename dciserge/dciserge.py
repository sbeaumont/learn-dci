import new

class Context(object):
	"""A scene in a play..."""
	
	# Class wiring. Just here for reference, I prefer the more precise instance wiring...
	
	def addRoleToClass(self, pyClass, traitClass):
		"""Add the trait (usually called mixins in Python) into the inheritance hierarchy of the Python class.
		   Note that this is not an object level construct, it is done here at the class level."""
		if traitClass not in pyClass.__bases__:
			pyClass.__bases__ = (traitClass,) + pyClass.__bases__

	def removeRoleFromClass(self, pyClass, traitClass):
		"""Remove trait from a class."""
		if traitClass in pyClass.__bases__:
			bases = list(pyClass.__bases__)
			bases.remove(traitClass)
			pyClass.__bases__ = tuple(bases)
			pass

	# Instance wiring. I wonder how to deal with naming clashes when different traits add methods with the same name?

	def addRole(self, instance, traitClass):
		"""Pulls methods out of the trait class and wires it into the given instance. Filters out the magic methods like __doc__ and __init__"""
		for methodName in dir(traitClass):
			if "__" not in methodName:
				method = getattr(traitClass, methodName)
				"""This is the magic formula that will wire the method of one class onto another."""
				setattr(instance, method.func_name, new.instancemethod(method.im_func, instance))
				#print "Wired", method.func_name, "to", instance

	def removeRole(self, instance, traitClass):
		"""Removes all methods from an instance that belong to a trait. Ignores magic methods like __doc__ and __init__"""
		for methodName in dir(traitClass):
			if "__" not in methodName:
				method = getattr(traitClass, methodName)
				delattr(instance, method.func_name)
				#print "Unwired", method.func_name, "from", instance



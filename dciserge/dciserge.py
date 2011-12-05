"""
Author: Serge Beaumont

This DCI proof of concept "physically" wires and unwires methods to an object or class
so that you can attach and detach role behavior. This solution has the advantage of zero
object/self schizophrenia. However, I prefer the other solution that David Byers came up
with which can be found in the dci.py file. That solution uses nifty wrapping magic with
the following advantages.

- the original object is unchanged, so "unwiring" happens automatically when the role
  goes out of scope,
- the role becomes part of the superclass hierarchy for this object so that you don't 
  get weird problems when you have name clashes. It simply becomes an overridden method 
  which actually makes sense from the perspective of the role.
- you can check for the role type

So by all means use the other solution. This one is just here in case an alternative 
solution is needed for some reason...
"""

import new

class Context(object):
	"""A scene in a play..."""
	
	# Class wiring. Just here for reference, I prefer the more precise instance wiring...
	
	def addRoleToClass(self, pyClass, roleClass):
		"""Add the role (usually called mixins in Python) into the inheritance hierarchy of the Python class.
		   Note that this is not an object level construct, it is done here at the class level."""
		if roleClass not in pyClass.__bases__:
			pyClass.__bases__ = (roleClass,) + pyClass.__bases__

	def removeRoleFromClass(self, pyClass, roleClass):
		"""Remove role from a class."""
		if roleClass in pyClass.__bases__:
			bases = list(pyClass.__bases__)
			bases.remove(roleClass)
			pyClass.__bases__ = tuple(bases)
			pass

	# Instance wiring. I wonder how to deal with naming clashes when different roles add methods with the same name?

	def addRole(self, instance, roleClass):
		"""
		Pulls methods out of the role class and wires it into the given instance.
		Filters out the magic methods like __doc__ and __init__
		"""
		for methodName in dir(roleClass):
			if "__" not in methodName:
				method = getattr(roleClass, methodName)
				"""This is the magic formula that will wire the method of one class onto another."""
				setattr(instance, method.func_name, new.instancemethod(method.im_func, instance))
				#print "Wired", method.func_name, "to", instance

	def removeRole(self, instance, roleClass):
		"""
		Removes all methods from an instance that belong to a role. Ignores magic methods like __doc__ and __init__
		"""
		for methodName in dir(roleClass):
			if "__" not in methodName:
				method = getattr(roleClass, methodName)
				delattr(instance, method.func_name)
				#print "Unwired", method.func_name, "from", instance



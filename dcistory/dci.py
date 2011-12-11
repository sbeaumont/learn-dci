"""
DCI proof of concept

Author: David Byers, Serge Beaumont
7 October 2008
"""
import new

class Context(object):
	"Just a marker"
	pass

# -------------------------------------------------- Data

class Data(object):
	"""
	You DON'T have to subclass from Data.
	
	The standard object() does not have a __dict__ so you can't attach attributes to it.
	This class is for convenience so you don't have to specify an empty class if you don't want to.
	"""
	pass
	
class FlexiData(Data):
	"""
	Convenience Data class that returns None for any attributes it does not contain.
	May be useful if you want to "lazy load" your Data Objects with state.
	"""
	def __getattr__(self, name):
		return None

# -------------------------------------------------- Role

class Role(object):
	"""A Role is a special class that never gets instantiated directly.
	Instead, when the user wants to create a new role instance, we
	create a new class that has the role and another object's class
	as it's superclasses, then create an instance of that class, and
	link the new object's dict to the original object's dict."""
	
	def __new__(cls, ob, context=None):
		members = dict(__context__ = context, __ob__ = ob)
		if hasattr(ob.__class__, '__slots__'):
			members['__setattr__'] = Role.___setattr
			members['__getattr__'] = Role.___getattr
			members['__delattr__'] = Role.___delattr

		c = new.classobj("%s as %s.%s" % (ob.__class__.__name__, cls.__module__, cls.__name__), (cls, ob.__class__), members)
		i = object.__new__(c)
		if hasattr(ob, '__dict__'): 
			i.__dict__ = ob.__dict__
			
		return i
	
	def __init__(self, ob, context=None):
		"""Do not call the superclass __init__. If we did, then
		we would call the __init__ function in the real class
		hierarcy too (i.e. Account, in this example)"""
		pass
	
	def ___getattr(self, attr):
		"""Proxy to object"""
		return getattr(self.__ob__, attr)
	
	def ___setattr(self, attr, val):
		"""Proxy to object"""
		setattr(self.__ob__, attr, val)
	
	def ___delattr(self, attr):
		"""Proxy to object"""
		delattr(self.__ob__, attr)
	
	def __eq__(self, other):
		if hasattr(other, '__ob__'):
			return self.__ob__ == other.__ob__
		else:
			return self.__ob__ == other

	def __ne__(self, other):
		if hasattr(other, '__ob__'):
			return self.__ob__ != other.__ob__
		else:
			return self.__ob__ != other

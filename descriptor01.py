#!/bin/python
# https://pabloariasal.github.io/2018/11/25/python-descriptors/
# https://www.blog.pythonlibrary.org/2016/06/10/python-201-what-are-descriptors/

"""
Objects that define either of these methods:

__get__(self, obj, type=None)
__set__(self, obj, value)
__del__(self, obj)

Are called descriptors.
If an objects implements all three, like property, it?s called a data descritor.
If only __get__ is present, the object is called a non-data descriptor.
"""

# Classes' property descriptor

class Computer():
	def __init__(self):
		self._operating_system = None

	def get_operating_system(self):
		return self._operating_system

	def set_operating_system(self, os):
		self._operating_system = os

	operating_system = property(get_operating_system, set_operating_system)
	
c=Computer()
c.operating_system = 'REL'
print c.operating_system

# Classes' property descriptor via decorator

class Computer():
	def __init__(self):
		self._operating_system = None

	@property
	def operating_system(self):
	    return self._operating_system

	@operating_system.setter
	def operating_system(self, os):
		self._operating_system = os

c=Computer()
c.operating_system = 'REL'
print c.operating_system
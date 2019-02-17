#!/usr/bin/env python3

from functools import wraps


class Value(object):
	"""
	stores property values
	"""

	def __init__(self, name, getter=None, _value=None):
		@wraps(getter)
		def _getter(_object):
			# print object, self.value
			_value = getter(_object)
			if _value:
				return _value
			if hasattr(self, 'value'):
				return self.value
			return None

		self.getter = _getter
		self.value = _value

	def setter(self, _object, value):
		# print 'setter=', value
		self.value = value

	def deleter(self, _object):
		self.value = None
		# print 'deleter=', self.value
		del self.value

#!/usr/bin/env python3

import inspect


def getRoot(fn):
	"""
	dig down the closure stack to find the root function
	"""
	# print('fn=', fn, ', name=', fn.__name)
	while hasattr(fn, 'func_closure') and fn.func_closure:
		# print('fn.func_closure=', fn.func_closure)
		if len(fn.func_closure) == 0:
			break
		fn = fn.func_closure[0].cell_contents
	return fn
	
	
def getSpec(fn):
	"""
	get functional specification
	"""
	params = inspect.getfullargspec(fn)
	_args = list()
	for a in params.args[1:]:
		_args.append(a)
	_kwargs = dict()
	values = []
	if params.defaults:
		values = list(params.defaults)
		values.reverse()
	for v in values:
		n = _args.pop()
		_kwargs[n] = v
	return fn, _args, _kwargs


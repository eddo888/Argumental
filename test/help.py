#!/usr/bin/env python3

# PYTHON_ARGCOMPLETE_OK

import sys, os, re

#sys.path.insert(0,'..')

from Argumental.Argue import Argue

args = Argue(help='''one
two''')

#_________________________________________________________________
@args.command(help='three\nfour')
class Helper(object):
	'''
	this is the helper class documentation
	with multiple lines
	'''

	@args.operation(help='five\nsix')
	def helping(self):
		'''
		this is the helping method documentation
		with multiplie lines
		'''

		return

	
#_________________________________________________________________
if __name__ == '__main__': args.execute()

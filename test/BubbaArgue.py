#!/usr/bin/env python3

import os, re, sys

sys.path.append('..')

from Argumental.Getters import getRoot
from Argumental.Argue import Argue

from MommaArgue import MommaArgue, args

@args.argument(short='d')
def debug():
	return False

@args.command(name='bub')
class BubbaArgue:

	@args.attribute
	def bubby(self):
		return '@bubby'
	
	@args.operation
	def momma(self):
		return super().momma()

	@args.operation
	def bubba(self):
		return self.bubby()

BubbaArgue.__bases__ += (MommaArgue,)

if __name__ == '__main__':
	print(args.execute())
	

#!/usr/bin/env python3

import os,re,sys

from io import StringIO

class HoldMe(object):

	def __init__(self,verbose=False):
		self.verbose = verbose
		self.stdout = sys.stdout
		self.stderr = sys.stderr
		
	def __del__(self):
		self.unset()
		
	def set(self):
		if self.verbose:
			self.stdout.write('\n==========================================================================================\n')
		sys.stdout = StringIO()
		sys.stderr = StringIO()
		
	def get(self, output=False):
		stdout = sys.stdout.getvalue()
		stderr = sys.stderr.getvalue()
		if self.verbose or output:
			self.stdout.write(stdout)
			self.stdout.flush()
			self.stderr.write(stderr)
			self.stderr.flush()
		return stdout, stderr
		
	def unset(self):
		if self.verbose:
			self.stderr.write('\n------------------------------------------------------------------------------------------\n')
		sys.stdout = self.stdout
		sys.stderr = self.stderr


#!/usr/bin/env python3

from Argumental.Argue import Argue

args = Argue()

@args.argument
def n1(): return 'value'

args.parse()
print n1()

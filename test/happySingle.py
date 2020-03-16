#!/usr/bin/env python3

import os,re,sys

from Argumental.Argue import Argue

args = Argue()

@args.command
class GoodBoy(object):

    @args.operation
    def gb1(self): return 'good'

@args.command(single=True)
class BadBoy(object):

    @args.operation
    def bb1(self): return 'bad'

if __name__ == '__main__':
    print args.execute()
    

    

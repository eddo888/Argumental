#!/usr/bin/env python2

import os,re,sys

from Tools.argue import Argue

args = Argue()

@args.command(single=True)
class GoodBoy(object):

    @args.operation
    def gb1(self): return 'good'

@args.command(single=True)
class BadBoy(object):

    @args.operation
    def bb1(self): return 'bad'

if __name__ == '__main__':
    print args.execute()
    

    

#!/usr/bin/env python3

# PYTHON_ARGCOMPLETE_OK

import os,re,sys,json

from Argumental.Argue import Argue

args = Argue()

@args.argument
def g1(): return

@args.argument(name='g2')
def G2(): return

@args.argument(name='g3', short='g')
def g3(): return

@args.argument(name='g4', default='g4')
def g4(): return
  
@args.argument(name='g5', oneof=['aye','bee','cee'], short=True, flag=True, required=True)  
def g5(): return

@args.argument(name='g6', oneof=['one','two','three'], required=True, type=int)  
def g6(): return

if __name__ == '__main__':
    ns = args.parse()
    json.dump(vars(ns),sys.stdout,indent=4)
    
    #args.execute()
    json.dump({
        'g1' : g1(),
        'g2' : G2(),
        'g3' : g3(),
        'g4' : g4(),
        'g5' : g5(),
        'g6' : g6()
    },sys.stdout,indent=4)


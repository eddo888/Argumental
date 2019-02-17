#!/usr/bin/env python2

import os,sys,re,json
from Tools.argue import Argue

args = Argue()

@args.argument(type=int)
def default(): return 2

@args.command(single=True)
class MyClass(object):
    '''
    some class
    '''
    
    @args.attribute(short='f', flag=True)
    def myFlag(self): return False

    @args.attribute(short='b', type=bool)
    def myBool(self): return False

    @args.attribute(short='i', type=int, nargs='*')
    def myInts(self): return ['2','3']

    @args.attribute(short='c', choices=['a','b'])
    def myChoice(self): return 'a'

    @args.attribute(short='r', required=True)
    def myRequired(self): return
    
    @args.operation
    def myMethod(self,p1,p2,p3='P3',p4=None):
        return {
            'default':default(),
            'flag':self.myFlag(),
            'bool':self.myBool(),
            'ints':self.myInts(),
            'choice':self.myChoice(),
            'required':self.myRequired(),
            'p1':p1,
            'p2':p2,
        }

if __name__ == '__main__': 
    argv = '-r ok -f -c b myMethod 1 2'.split(' ')
    args.parse(argv)
    result = args.execute()
    if result:
        print(json.dumps(result,indent=4))


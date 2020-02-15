#!/usr/bin/env python2

# PYTHON_ARGCOMPLETE_OK

import os,re,sys,json

from Argumental.Argue import Argue

args = Argue()

@args.command(single=True)
class Mucken(object):
    
    @args.property(default='abc')
    def prop1(self): return

    @args.property(default='xyz')
    def prop2(self): return
    
    @args.operation
    @args.parameter(name='param1', default=prop1)
    @args.parameter(name='param2', default=prop2)
    def doit(self, param1=None, param2=None):
        print json.dumps(dict(
            prop1=self.prop1,
            prop2=self.prop2,
            param1=param1,
            param2=param2,
        ),indent=4)
        
if __name__ == '__main__':
    args.execute()

    


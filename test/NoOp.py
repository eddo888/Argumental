#!/usr/bin/env bash

import sys,os,re

from Argumental.Argue import Argue

args = Argue()

@args.command(single=True)
class NoOp(object):
    
    @args.property(short='p', default='p1')
    def myProp(self): return
    
    @args.operation
    def __call__(self):
        return dict(p=self.myProp)
        
if __name__ == '__main__':
    print args.execute()
    

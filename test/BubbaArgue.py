#!/usr/bin/env python2

import os, re, sys

from Getters import getRoot
from Tools.argue import Argue

from MommaArgue import MommaArgue, args

@args.argument(short='d')
def debug():
    return False

@args.command(name='bub')
class BubbaArgue(getRoot(MommaArgue)):

    @args.attribute
    def bubby(self):
        return '@bubby'
    
    @args.operation
    def momma(self):
        return args.super(BubbaArgue,self).momma()

    @args.operation
    def bubba(self):
        return self.bubby()

if __name__ == '__main__':
    print args.execute()
    

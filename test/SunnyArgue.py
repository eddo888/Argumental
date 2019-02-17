#!/usr/bin/env python2

import os,re,sys

from Getters import getRoot
from Tools.argue import Argue

from DaddaArgue import DaddaArgue, args

@args.argument(short='d')
def debug():
    return False

# we expect to add to the parent
@args.command(single=True)
class SunnyArgue(getRoot(DaddaArgue)):

    # attributes replace parents
    @args.attribute(short='a')
    def attribute(self):
        '''
        Sons Attribute
        '''
        return '@sunny'

    #operations replace parents
    @args.operation
    def shared(self):
        '''
        Sons Operation
        '''
        return self.attribute()

if __name__ == '__main__':
    print args.execute()
    

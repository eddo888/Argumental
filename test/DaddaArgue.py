#!/usr/bin/env python3

import os,re,sys

from Argumental.Argue import Argue

args=Argue()

@args.argument(short='v')
def verbose():
    return False

@args.command(single=True)
class DaddaArgue(object):

    @args.attribute(short='a')
    def attribute(self):
        '''
        Dads Attribute
        '''
        return '@daddy'
    
    @args.operation
    def shared(self):
        '''
        Dads Operation
        '''
        return self.attribute()
        
if __name__ == '__main__':
    print(args.execute())
    

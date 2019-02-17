#!/usr/bin/env python2

import os,re,sys

from Tools.argue import Argue

args=Argue()

@args.argument(short='v')
def verbose():
    return False

@args.command(name='mum')
class MommaArgue(object):

    @args.attribute
    def mommy(self):
        return '@mommy'
    
    @args.operation
    def momma(self):
        return self.mommy()
        
if __name__ == '__main__':
    print args.execute()
    

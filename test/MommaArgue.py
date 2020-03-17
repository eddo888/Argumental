#!/usr/bin/env python3

import os,re,sys

sys.path.append('..')

from Argumental.Argue import Argue

args=Argue()

@args.argument(short='v')
def verbose():
    return False

@args.command(name='mum')
class MommaArgue:

    #@args.attribute
    def mommy(self):
        return '@mommy'
    
    #@args.operation
    def momma(self):
        return self.mommy()
        
if __name__ == '__main__':
    print(args.execute())
    

#!/usr/bin/env python2

import os,re,sys,json,gc

from Argumental.Argue import Argue

args = Argue()

@args.command(single=True, name='mc')
class MyClass(object):
    '''
    class MyClass(object):
    '''
    
    @args.attribute(short='f',flag=True)
    def myFlag(self):
        '''
        def myFlag(self):
        '''
        return False
  
    @args.operation
    def m1(self, p1, p2):
        '''
        def m3:
        :param p1: parameter 1
        :param p2: parameter 2
        '''
        return p1, p2
         
    @args.operation
    def m2(self, p1, p2='P2'):
        '''
        def m2:
        :param p1: parameter 1
        :param p2: parameter 2 defaut = 'P2'
        '''
        return p1, p2

    @args.operation
    def m3(self, p1='P1', p2='P2'):
        '''
        def m3:
        :param p1: parameter 1 default = 'P1'
        :param p2: parameter 2 default = 'P2'
        '''
        return p1, p2
        
if __name__ == '__main__':
    results = args.execute()
    json.dump(results,sys.stdout,indent=4)

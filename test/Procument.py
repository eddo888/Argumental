#!/usr/bin/env python2

import os,re,sys,json

from Tools.argue import Argue

args = Argue()

@args.argument(
    short='v', 
    flag=True, 
    help='yall'
)
def verbose(): return

@args.command(single=True)
class Procument(object):
    '''
    class doco
    '''
    
    @args.attribute(
        short='l', 
        flag=True, 
        help='sprekenzie'
    )
    def lang(self): return

    @args.operation
    def m1(self, p1, p2=None, _p3=None, p4=None):
        '''
        method doco colons
        
        @args.parameter(
            name='p1',
            type=int,
            default=2,
            help='arg 1'
        )
        
        @args.parameter(
            name='p2',
            choices=['a','b','c'],
            help='kwarg 2'
        )
        
        @args.parameter(
            param='_p3',
            name='p3',
            help='kwarg 2',
            oneof=['aye','bee','cee'],
            short=True,
            flag=True
        )
     
        @args.parameter(      
            name='p4',
            help='kwarg 4',
            oneof={
                'x':'help x',
                'y':'help y',
                'z':'help z'
            },
            short=True,
            type=int
        )
        
        @args.returns(
            type=dict,
            help='test values'
        )
        '''
        return {
            'p1' : p1,
            'p2' : p2,
            'p3' : _p3,
            'p4' : p4,
        }
        
    @args.operation
    def m2(self, p1, p2=None, _p3=None, p4=None):
        '''
        method doco decorates
        
        
        :param    p1: arg 1
        :type     p1: int
        :default  p1: 2
        
        :param    p2: kwarg 1
        :choices    : ['a','b','c']
        
        :param _p3: kwarg 2
        :name     : p3 
        :oneof    : ['aye','bee','cee']
        :short    : True
        :flag     : True
                
        :param p4: kwarg 4
        :oneof: {'x':'help x','y':'help y','z':'help z'}
        :short: True
        :type: int
        
        :rtype      : dict
        :returns    : test values
        '''
        return {
            'p1' : p1,
            'p2' : p2,
            'p3' : _p3,
            'p4' : p4,
        }
       
    @args.operation
    @args.parameter(
        name='p1',
        type=int,
        default=2,
        help='arg 1'
    )    
    @args.parameter(
        name='p2',
        choices=['a','b','c'],
        help='kwarg 2'
    )
    @args.parameter(
        param='_p3',
        name='p3',
        help='kwarg 2',
        oneof=['aye','bee','cee'],
        short=True,
        flag=True
    )
    @args.parameter(      
        name='p4',
        help='kwarg 4',
        oneof={
            'x':'help x',
            'y':'help y',
            'z':'help z'
        },
        short=True,
        type=int
    )
    @args.returns(
        type=dict,
        help='test values'
    )    
    def m3(self, p1, p2=None, _p3=None, p4=None):
        '''
        parameter definition outside doco
        '''
        return {
            'p1' : p1,
            'p2' : p2,
            'p3' : _p3,
            'p4' : p4,
        }        
       
if __name__ == '__main__':
    json.dump(args.execute(), sys.stdout, indent=4)

    

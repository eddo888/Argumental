#!/usr/bin/env python2

import os,re,sys,json,unittest,logging

from Tools.argue import Argue

args = Argue()

#=============================================================

@args.argument(short='v', flag=True)
def verbose(): return False

@args.argument
def level(): return 'INFO'

@args.argument(name='testing')
def testing(): return False

#=============================================================

@args.command
class ForTheSake(object):
    '''
    This the first level option and should be called 'ForTheSake'
    '''

    #_________________________________________________________

    @args.attribute(default='isdefault')
    def myAttribute(self):
        '''
        default attribute test
        '''
        return

    #_________________________________________________________

    @args.attribute(name='named')
    def myNamedMethod(self):
        '''
        should be called --named and returns 'isnamed'
        '''
        return 'isnamed'

    #_________________________________________________________

    @args.attribute(short='s')
    def myShortMethod(self):
        '''
        should be called -s and returns 'isshort'
        '''
        return 'isshort'

    #_________________________________________________________

    @args.attribute(required=True)
    def myRequired(self):
        '''
        should be called --myRequired and fail if not provided
        '''
        return None

    #_________________________________________________________

    @args.attribute(flag=True)
    def myFlag(self):
        '''
        this is a flag true if exists false if not
        '''
        return False

    #_________________________________________________________

    @args.attribute(choices=['a','b'])
    def myChoice(self):
        '''
        select for a list of choices,
        test if in or out of list
        '''
        return None

    #_________________________________________________________

    @args.attribute(short='n', type=int)
    def myNumber(self):
        '''
        this should expect an number of type int 
        '''
        return 0

    #_________________________________________________________

    settable = 'notset'

    def setSettable(self, value):
        ''' 
        this pattern allows decorated access and get/set object
        '''
        self.settable = value

    @args.attribute(name='settable')
    def getSettable(self):
        '''
        will be overriddent by decorator command line setting
        '''
        return self.settable

    #_________________________________________________________

    @args.operation
    def myMethod(self, p1, p2, p3='d3', p4='d4'):
        '''
        this should be called myMethod
        and is a good example

        :param   p1 : p1 should be expected
        :type    p1 : str

        :param   p2 : p2 should be expected
        :type    p2 : int
        :default p2 : 3

        :param   p3 : p3 is optional use --p3
        :default p3 : d3
        :param   p4 : p4 is optional use --p4

        :return     : json view of all variables
        :rtype      : dict

        :Example:

        $ ./forTheSake.py [--] <command> <operation> <parameters> [--parameter=optional]

        '''
        return {
            'verbose'   : verbose(),
            'level'     : level(),
            'attribute' : self.myAttribute(),
            'settable'  : self.getSettable(),
            'named'     : self.myNamedMethod(),
            'short'     : self.myShortMethod(),
            'required'  : self.myRequired(),
            'flag'      : self.myFlag(),
            'choice'    : self.myChoice(),
            'number'    : self.myNumber(),
            'p1'        : p1,
            'p2'        : p2,
            'p3'        : p3,
            'p4'        : p4
        }

    @args.operation(name='mulched')
    def myMulched(self):
        '''
        as a named operation
        '''
        return

#=============================================================
@args.command(name='mycommand')
class OtherCommand(object):
    '''
    this is another command and should be called 'mycommand'
    '''

    @args.operation
    def myParameters(self, shorted='s1', named='n1', flagged=False, chosen='a', nargue=['1','2']):
        '''
        test with arg overides on parameters

        :param shorted: this option is shortenated to s
        :short shorted: s

        :param named: this option is named to name
        :name named: name

        :param flagged: this is a flag
        :flag flagged: True

        :param chosen: this is from a list ['a','b']
        :choices chosen: ['a','b']

        :param nargue: this will be multiple '*'
        :nargs nargue: *
        '''
        return {
            'shorted' : shorted,
            'named'   : named,
            'flagged' : flagged,
            'chosen'  : chosen,
            'nargue'  : nargue
        }

    @args.operation
    def myCombinations(self, p1, nv=['a']):
        '''
        a mix of choices
        
        :param p1: argument in position 1
        :type p1: int
        :choices p1: [1,2,3]
        :nargs p1: *

        :param nv: name value argument
        :type nv: int
        :choices nv: [1,2,3]
        :nargs nv: *

        '''
        return {
            'p1':p1,
            'nv':nv
        }

    @args.operation
    def myRequirements(self, r1, r2, r3=None, r4=None, r5=None):
        '''
        a test of required attributes in args and kwargs positions

        :param    r1 : should be required by default
        
        :param    r2 : should ignore required as in args
        :required r2 : False

        :param    r3 : should be required overruled
        :required r3 : True

        :param    r4 : should be not required overruled
        :required r4 : False

        :param    r5 : should be default not required

        '''
        return {
            'r1': r1,
            'r2': r2,
            'r3': r3,
            'r4': r4,
            'r5': r5,
        }
    
#=============================================================
@args.command(short='c')
class ShortCommand(object):
    '''
    this is a short command and should be called 'c'
    '''

if __name__ == '__main__':
    results = args.execute()
    if results:
        if type(results) in [str,unicode]:
            print(results)
        else:
            json.dump(results,sys.stdout,indent=4)
    


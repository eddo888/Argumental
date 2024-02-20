#!/usr/bin/env python3

import os,re,sys,json

from Argumental.Argue import Argue

args = Argue()

#====================================================================================================
@args.argument(short='v', flag=True)
def verbose(): return False

#====================================================================================================
@args.command(single=True)
class OfTheEngagment(object):

    #________________________________________________________________________________________________
    @args.attribute(flag=True)
    def myFlag(self):
        '''
        this is a flag true if exists false if not
        '''
        return False

    #________________________________________________________________________________________________
    @args.attribute(choices=['a','b'])
    def myChoice(self):
        '''
        select for a list of choices,
        test if in or out of list
        '''
        return None

    #________________________________________________________________________________________________
    @args.attribute(short='n', type=int)
    def myNumber(self):
        '''
        this should expect an number of type int 
        '''
        return 0

    #________________________________________________________________________________________________
    @args.operation
    def myMethod(self, p1, p2, p3='d3', p4='d4'):
        '''
        this should be called myMethod
        and is a good example

        :param p1: p1 should be expected
        :type p1: str
        :param p2: p2 should be expected
        :type p2: int
        :param p3: p3 is optional use --p3 and defaults to d3
        :param p4: p3 is optional use --p4 and defaults to d4
        :return: json view of all variables
        :rtype: dict

        :Example:

        $ ./forTheSake.py [--] <command> <operation> <parameters> [--parameter=optional]

        '''
        return {
            'verbose' :  verbose(),
            'flag' :     self.myFlag(),
            'choice' :   self.myChoice(),
            'number' :   self.myNumber(),
            'p1' :       p1,
            'p2' :       p2,
            'p3' :       p3,
            'p4' :       p4
        }

#====================================================================================================
if __name__ == '__main__':
    print(json.dumps(args.execute(), indent=4))
    

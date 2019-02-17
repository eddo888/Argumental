#!/usr/bin/env python2

import os,sys,re,logging

from Tools.argue import Argue

logging.basicConfig(level=logging.INFO)
logging.disable(Argue.__name__)

args = Argue(name='testing', help='some test args')

@args.argument(name='outside', short='O')
def outside():
    '''
    this is a root level argument
    '''
    return 'default outside class'

@args.argument(name='flag', short='f', flag=True)
def flag():
    '''
    this is a store_true argument
    '''
    return False

@args.command(name='aClass',short='a')
class ClassA(object):
    '''
    This is a class with name and short in the decorator
    '''
    @args.attribute(name='insider',short='I')
    def inside(self):
        '''
        global attribute inside class
        '''
        return 'default inside class'

    @args.operation
    def a1m1(self,a1,k1=None):
        '''
        this is method with no args in the decorator and args and kwargs in the method signature
        '''
        return 'a1m1(a1="%s", k1="%s")'%(a1,k1)

    @args.operation
    def a1m2(self):
        '''
        this is a method with no args in the decorator and no args in the method signature
        '''
        return 'a1m2()'

    @args.operation(name='a1m3named')
    def a1m3(self):
        '''
        this is a method with name in the decoroator and no args in the method signature
        '''
        return 'a1m3()'

    @args.operation(name='a1m4named', short='b')
    def a1m4(self):
        '''
        this is a method with name and short in the decorator and no args in the method signature
        '''
        return 'a1m4()'


    @args.operation(name='a1m5named', short='c')
    def a1m5(self,a1,k1=None):
        '''
        this is method name and short in the decorator and args and kwargs in the method signature
        '''
        return 'a1m5(a1="%s", k1="%s")'%(a1,k1)

    def a1m6(self):
        '''
        this is a method with no decorator and no args in the method signature
        '''
        return 'a1m6()'

@args.command(name='bClass')
class ClassB(object):
    '''
    This is a class with name only in the decorator
    '''
    pass

@args.command
class ClassC(object):
    '''
    This is a class with no parameters in the decorator
    '''
    @args.operation
    def __init__(self):
        '''
        this is a constructor with a decorator
        '''
        return '__self__()'

class ClassD(object):
    '''
    This is a class with no command decorator
    '''
    @args.operation
    def d1m1(self):
        '''
        this is a method with an operator decorator and no command decorator
        '''
        return 'd1m1()'

if __name__ == '__main__':
    parsed = args.parse()
    result = args.execute()
    if result: print result


#!/usr/bin/env python3

from Argumental.Argue import Argue

args = Argue()

@args.command(single=True)
class MyClass(object):
    '''MyClass doco'''

    @args.operation
    def m1(self, p1):
        return p1

    @args.operation
    def m2(self, p2):
        return p2

@args.command
class MyOther(object):

    @args.operation
    def m3(self,p3):
        return p3
    
if __name__ == '__main__': print args.execute()



#!/usr/bin/env python3

from Argumental.Argue import Argue

args = Argue()

@args.command(single=True)
class MyCommand(object):

    @args.operation(short='m')
    def myOperation(self,p1,p2):
        
        @args.parameter(name='p1',required=True,type=int)
        def _p1(): return p1

        @args.parameter(name='p2',type=int)
        def _p2(): return p2

        return dict(p1=_p1(),p2=_p2())

if __name__ == '__main__':
    print args.execute()



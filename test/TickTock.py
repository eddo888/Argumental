#!/usr/bin/env python2

import os,re,sys,json

from datetime import datetime, date
import time

from Argumental.Argue import Argue
from Perdy.pretty import prettyPrint

args = Argue()

@args.argument(type=datetime,format='%Y-%m-%d %H:%M:%S')
def now_argument(): return None

@args.command(name='tick')
class TickTock(object):

    @args.attribute(type=datetime,format='%Y-%m-%d %H:%M:%S')
    def now_attribute(self): return None

    @args.operation
    @args.parameter(name='mytime', type=time)
    @args.parameter(name='mydate', type=date)
    @args.parameter(name='mydatetime', type=datetime)
    def tick(self, 
        mytime, 
        mydate, 
        mydatetime
    ):
        return dict(
            time=mytime,
            date=mydate,
            datetime=mydatetime
        )
        
    @args.operation
    def tock(self, p1, p2=None, p3=None):
        '''
        :param  p1: p1 datetime
        :type   p1: datetime
        :format p1: %Y-%m-%d %H:%M:%S

        :param  p2: p2 datetime
        :type   p2: datetime
        :format p2: %Y-%m-%d %H:%M:%S

        :param  p3: p3 datetime
        :type   p3: datetime

        '''
        return {
            'p1':p1,
            'p2':p2,
            'p3':p3,
            'argument': now_argument(),
            'attribute': self.now_attribute()
        }

if __name__ == '__main__':
    try:
        import console
        console.clear()
        console.set_font('Menlo',12)
    except:
        pass
    args.parse(['tick', 'tick', '17:54:00', '2017-09-15', '2017-09-15 17:54:00'])
    #args.parse(['tick', 'tock', '2017-09-15 17:54:00', '--p2', '2017-09-15 17:54:00', '--p3', '2017-09-15 17:54:00' ])
    #args.parse('tick tick -h'.split())
    results=args.execute()
    if results:
        prettyPrint(results, colour=True, yaml=True)

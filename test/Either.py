#!/usr/bin/env python2

import os,re,sys,json

from Tools.argue import Argue

args = Argue()

@args.command(single=True)
class Either(object):

    @args.attribute(
        name='a1', 
        oneof=['one','two','three'], 
        required=True,
        type=int
    )  
    def a1(self): return

    @args.attribute(
        name='a2', 
        oneof=['xml','json','yaml'], 
        flag=True, 
        required=True, 
        short=True
    )  
    def a2(self): return

    @args.operation
    def do(self, choice=None, either=None):
        '''
        only one of each
        
        :param    choice: exclusive choice
        :oneof    choice: ['aye','bee','cee']
        :flag     choice: True
        :short    choice: True
        :required choice: True

        :param    either: exclusive inputs
        :oneof    either: ['x','y','z']
        :required either: True
        :type     either: int

        '''
        return {
            'a1' : self.a1(),
            'a2' : self.a2(),
            'choice' : choice,
            'either' : either
        }
        
if __name__ == '__main__':
    import console
    console.set_font('Menlo', 11)
    json.dump(args.execute(),sys.stdout,indent=4)

    

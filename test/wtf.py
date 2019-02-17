#!/usr/bin/env python2

import os,re,sys

from Tools.argue import Argue

args = Argue()

@args.command(single=True)
class WhatTheFireTruck(object):
    
    @args.operation
    def l1(self, _format=None):
        '''
        list the KMS names

        @args.parameter(
            param='_format',
            name='format',
            help='what type format do you want',
            short=True,
            flag=True,
            oneof={
                'text':'output as text',
                'json':'output as json',
                'xml' :'output as xml',
            },
            default='text'
        )
        '''
        return _format
     
    @args.operation
    def l2(self,_format=None):
        '''
        mucken
        
        :param   _format: what type format do you want
        :name    _format: format
        :short   _format: True
        :flag    _format: True
        :oneof   _format: {'text':'text help','json':'json help','xml':'xml help'}
        :default _format: 'text'
        
        '''  
        return _format
       
if __name__ == '__main__': 
    print args.execute()
    

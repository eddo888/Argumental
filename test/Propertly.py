#!/usr/bin/env python2

import os,re,sys,json,yaml

from StringIO import StringIO

from Tools.pretty import prettyPrint
from Tools.argue import Argue

args = Argue()

@args.argument(short='v', flag=True)
def verbose():
    return False

#_______________________________________________________________
@args.command(name='valuable')
class Valuable(object):
    '''
    different file names for getter, setter and deleter
    postumous definition of value = property()
    '''
    
    _value = 'abc123'

    @args.attribute(short='v')
    def value(self):
        '''
        value getter
        '''
        return self._value

    def set_value(self,value):
        '''
        value setter
        '''
        self._value = value
      
    def del_value(self):
        '''
        value deleter
        '''
        self._value = None

    # define the property
    value = property(
        value,
        set_value,
        del_value
    )
    
    @args.operation
    @args.parameter(
        name='input', 
        help='just do it'
    )
    @args.returns(
        type=str,
        help='regex version of inout'
    )
    def do(self, input):
        '''
        class operation
        '''
        if self.value:
            return '^%s$'%self.value


#_______________________________________________________________
@args.command(name='just')
class Propertly(object):
    '''
    command class
    '''
    
    _value = 'abc123'

    @args.property(short='V')
    def value(self):
        '''
        value getter
        '''
        return self._value

    @value.setter
    def value(self,value):
        '''
        value setter
        '''
        self._value = value
      
    @value.deleter
    def value(self):
        '''
        value deleter
        '''
        self._value = None

    @args.operation
    @args.parameter(
        name='input', 
        help='just do it'
    )
    @args.returns(
        type=str,
        help='regex version of inout'
    )
    def do(self, input):
        '''
        class operation
        '''
        if self.value:
            return '^%s$'%self.value
            
#_______________________________________________________________
@args.command(name='duck')
class Duck(object):
    '''
    command class
    '''

    @args.property(short='V', default='abc123')
    def value(self):
        '''
        value getter
        '''
        return

    @args.operation
    @args.parameter(
        name='input', 
        help='just do it'
    )
    @args.returns(
        type=str,
        help='regex version of inout'
    )
    def do(self, input):
        '''
        class operation
        '''
        if self.value:
            return '^%s$'%self.value
            
#_______________________________________________________________
@args.command(name='test')
class TestMe(object):
    '''
    test the Propertly class as a normal class object
    '''

    @args.operation
    def run(self):
        '''
        create the object then interact with the object
        '''
        
        for c in [Valuable, Propertly, Duck]:
            if verbose():
                output = sys.stdout
            else:
                output = StringIO()
                
            output.write('%s\n'%c.__name__)
            
            p = c()

            # presume default value
            output.write('\tget\n\t\tp.value=%s\n'%p.value)
            assert('abc123' == p.value)
            output.write('\t\tp.do(\'da\')=%s\n'%p.do('da'))
            assert('^abc123$' == p.do('da'))

            p.value = '321cbs'
            output.write('\tset\n\t\tp.value=%s\n'%p.value)
            assert('321cbs' == p.value)
            output.write('\t\tp.do(\'da\')=%s\n'%p.do('da'))
            assert('^321cbs$' == p.do('da'))

            del p.value
            output.write('\tdelete\n\t\tp.value=%s\n'%p.value)
            assert(None == p.value)
            output.write('\t\tp.do(\'da\')=%s\n'%p.do('da'))
            assert(None == p.do('da'))

            del p
            #output.close()
            
        return
#_______________________________________________________________
if __name__ == '__main__':
    try:
        # pythonista on iOS
        import console
        console.clear()
        console.set_font('Menlo', 11)
    except:
        pass

    result = args.execute()
    if result:
        prettyPrint(yaml.load(result), yaml=True)
    

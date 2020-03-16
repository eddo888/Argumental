#!/usr/bin/env python3

import os,re,sys,json,gc,logging,unittest

if '..' not in sys.path:
	sys.path.append("..") # Adds higher directory to python modules path.
	
from datetime import datetime
from forTheSake import *
from HoldMe import HoldMe

holdme = HoldMe(verbose=False)

def patternCheck(fields,stdout):
	patterns = map(lambda x:re.compile('.*{.*%s.*}.*'%x), fields)
	for pattern in patterns:
		#print pattern.pattern
		assert pattern.match(stdout.replace('\n','\\n'))
		
#============================================================
class ForTheSakeTest(unittest.TestCase):

	def setUp(self):
		pass
		
	def tearDown(self):
		gc.collect()
		pass
		
	#________________________________________________________
	def test_00_argue(self):
		holdme.set()
		# get the default load out of the road
		args.parsed = args.parse('args'.split(' '))
		print(args.execute())
		stdout, stderr = holdme.get()
		holdme.unset()
		#print(stdout)
		assert len(stderr) == 0
		#print(type(stdout))
		assert 'arguments' in stdout
		
	#________________________________________________________
	def test_01_BaseHelp(self):
		line = '-h'
		
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			args.parsed = args.parser.parse_args(line.split(' '))
			args.execute()
			print(cm)
		stdout, stderr = holdme.get(output=False)
		holdme.unset()
		assert len(stderr) == 0
		patternCheck(['ForTheSake','mycommand','ShortCommand'],stdout)
		
	#________________________________________________________
	def test_02_CommandHelp(self):
		line = 'ForTheSake -h'
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			args.parsed = args.parser.parse_args(line.split(' '))
			args.execute()
			print(cm)
		stdout, stderr = holdme.get(output=False)
		holdme.unset()
		assert len(stderr) == 0
		patternCheck(['myMethod','mulched'],stdout)
		
	#________________________________________________________
	def test_03_OperationHelp(self):
		line = 'ForTheSake myMethod -h'
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			args.parsed = args.parser.parse_args(line.split(' '))
			args.execute()
			print(cm)
		stdout, stderr = holdme.get()
		holdme.unset()
		#print(stdout,stderr)
		assert len(stderr) == 0
		assert 'ForTheSake myMethod [-h] [--p3 P3] [--p4 P4]' in stdout
		assert 'p1 p2' in stdout
		#assert 'p1 should be expected' in stdout
		#assert 'p2 should be expected, default=3, type=int' in stdout
		
	#________________________________________________________
	def test_04_NoGlobals(self):
		line = 'ForTheSake --myRequired ok myMethod 1 2'
		holdme.set()
		args.parsed = args.parser.parse_args(line.split(' '))
		results = args.execute()
		stdout, stderr = holdme.get()
		holdme.unset()
		assert len(stderr) == 0
		logging.debug(json.dumps(results,indent=4))
		assert results['verbose'] == False
		assert results['level'] == 'INFO'
		
	#________________________________________________________
	def test_05_AllGlobals(self):
		line = '-v --level=DEBUG ForTheSake --myRequired ok myMethod 1 2'
		holdme.set()
		args.parsed = args.parser.parse_args(line.split(' '))
		results = args.execute()
		stdout, stderr = holdme.get()
		holdme.unset()
		assert len(stderr) == 0
		logging.debug(json.dumps(results,indent=4))
		assert results['verbose'] == True
		assert results['level'] == 'DEBUG'
		
	#________________________________________________________
	def test_06_NoAttributes(self):
		line = 'ForTheSake myMethod 1 2'
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			args.parsed = args.parser.parse_args(line.split(' '))
			args.execute()
			print(cm)
		stdout, stderr = holdme.get()
		holdme.unset()
		#print(stdout,stderr)
		assert 'error: the following arguments are required: --myRequired' in stderr
	#________________________________________________________
	def test_07_SomeAttributes(self):
		line = 'ForTheSake --myRequired ok myMethod 1 2'
		holdme.set()
		args.parsed = args.parser.parse_args(line.split(' '))
		results = args.execute()
		stdout, stderr = holdme.get()
		holdme.unset()
		assert len(stderr) == 0
		logging.debug(json.dumps(results,indent=4))
		assert results['attribute'] == 'isdefault'
		assert results['named'] == 'isnamed'
		assert results['short'] == 'isshort'
		assert results['required'] == 'ok'
		assert results['flag'] == False
		assert results['choice'] == None
		assert type(results['number']) == int
		assert results['number'] == 0
		assert results['settable'] == 'notset'
	#________________________________________________________
	def test_08_AllAttributes(self):
		line = 'ForTheSake --myAttribute=ma1 --named=mn1 -s sh1 --myRequired then --myFlag --myChoice b --myNumber 2 --settable isset myMethod 1 2'
		holdme.set()
		args.parsed = args.parser.parse_args(line.split(' '))
		results = args.execute()
		stdout, stderr = holdme.get()
		holdme.unset()
		assert len(stderr) == 0
		logging.debug(json.dumps(results,indent=4))
		assert results['attribute'] == 'ma1'
		assert results['named'] == 'mn1'
		assert results['short'] == 'sh1'
		assert results['required'] == 'then'
		assert results['flag'] == True
		assert results['choice'] == 'b'
		assert type(results['number']) == int
		assert results['number'] == 2
		assert results['settable'] == 'isset'
		
	#________________________________________________________
	def test_09_SomeParameters(self):
		line = 'ForTheSake --myRequired ok myMethod 1 2 --p3=3'
		print(line)
		holdme.set()
		args.parsed = args.parser.parse_args(line.split(' '))
		results = args.execute()
		stdout, stderr = holdme.get()
		holdme.unset()
		print(stdout, stderr)
		print(json.dumps(results, indent=4))
		assert len(stderr) == 0
		logging.debug(json.dumps(results,indent=4))
		assert results['choice'] == None
		assert results['flag'] == False
		assert results['attribute'] == 'isdefault'
		assert results['named'] == 'isnamed'
		assert type(results['number']) == int
		assert results['number'] == 0
		assert results['required'] == 'ok'
		assert results['settable'] == 'notset'
		assert results['short'] == 'isshort'
		assert results['verbose'] == False
		assert results['level'] == 'INFO'
		assert results['p1'] == '1'
		assert results['p2'] == 2
		assert results['p3'] == '3'
		assert results['p4'] == 'd4'
		
	#________________________________________________________
	def test_10_AllParameters(self):
		line = 'ForTheSake --myRequired ok myMethod 1 2 --p3=3 --p4=4'
		holdme.set()
		args.parsed = args.parser.parse_args(line.split(' '))
		results = args.execute()
		stdout, stderr = holdme.get()
		holdme.unset()
		assert len(stderr) == 0
		logging.debug(json.dumps(results,indent=4))
		assert results['choice'] == None
		assert results['flag'] == False
		assert results['attribute'] == 'isdefault'
		assert results['named'] == 'isnamed'
		assert type(results['number']) == int
		assert results['number'] == 0
		assert results['required'] == 'ok'
		assert results['settable'] == 'notset'
		assert results['short'] == 'isshort'
		assert results['verbose'] == False
		assert results['level'] == 'INFO'
		assert results['p1'] == '1'
		assert results['p2'] == 2
		assert results['p3'] == '3'
		assert results['p4'] == '4'
		
	#________________________________________________________
	def test_11_CommandHelp(self):
		line = 'mycommand -h'
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			args.parsed = args.parser.parse_args(line.split(' '))
			args.execute()
			print(cm)
		stdout, stderr = holdme.get()
		holdme.unset()
		assert len(stderr) == 0
		patternCheck(['myCombinations','myParameters','myRequirements'],stdout)
		
	#________________________________________________________
	def test_12_OperationHelp(self):
		line = 'mycommand myParameters -h'
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			args.parsed = args.parser.parse_args(line.split(' '))
			args.execute()
			print(cn)
		stdout, stderr = holdme.get()
		holdme.unset()
		assert len(stderr) == 0
		assert 'mycommand myParameters' in stdout
	#________________________________________________________
	def test_13_SomeParameters(self):
		line = 'mycommand myParameters'
		holdme.set()
		args.parsed = args.parser.parse_args(line.split(' '))
		results = args.execute()
		stdout, stderr = holdme.get()
		holdme.unset()
		assert len(stderr) == 0
		logging.debug(json.dumps(results,indent=4))
		assert results['shorted'] == 's1'
		assert results['named'] == 'n1'
		assert results['flagged'] == False
		assert results['chosen'] == 'a'
		assert results['nargue'] == ['1','2']
		
	#________________________________________________________
	def test_14_AllParameters(self):
		line = 'mycommand myParameters -s=ss --name=nn --flagged --chosen=b --nargue 3 4'
		holdme.set()
		args.parsed = args.parser.parse_args(line.split(' '))
		results = args.execute()
		stdout, stderr = holdme.get()
		holdme.unset()
		assert len(stderr) == 0
		logging.debug(json.dumps(results,indent=4))
		assert results['shorted'] == 'ss'
		assert results['named'] == 'nn'
		assert results['flagged'] == True
		assert results['chosen'] == 'b'
		assert results['nargue'] == ['3','4']
		
	#________________________________________________________
	def test_15_SomeChoices(self):
		line = 'mycommand myCombinations 2 --nv 2 3'
		holdme.set()
		args.parsed = args.parser.parse_args(line.split(' '))
		results = args.execute()
		stdout, stderr = holdme.get()
		holdme.unset()
		assert len(stderr) == 0
		logging.debug(json.dumps(results,indent=4))
		assert results['p1'] == [2]
		assert results['nv'] == [2,3]
		
	#________________________________________________________
	def test_16_WrongChoices(self):
		line = 'mycommand myCombinations 4 --nv 2 3'
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			args.parsed = args.parser.parse_args(line.split(' '))
			args.execute()
			print(cm)
		stdout, stderr = holdme.get()
		holdme.unset()
		assert 'error: argument p1: invalid choice: 4' in stderr
		
	#________________________________________________________
	def test_17_NoRequirements(self):
		line = 'mycommand myRequirements 1'
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			args.parsed = args.parser.parse_args(line.split(' '))
			args.execute()
			print(cm)
		stdout, stderr = holdme.get()
		holdme.unset()
		assert 'error: too few arguments' in stderr
	#________________________________________________________
	def test_18_SomeRequirements(self):
		line = 'mycommand myRequirements 1 2'
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			args.parsed = args.parser.parse_args(line.split(' '))
			args.execute()
			print(cm)
		stdout, stderr = holdme.get()
		holdme.unset()
		assert 'error: argument --r3 is required' in stderr
		
	#________________________________________________________
	def test_19_AllRequirements(self):
		line = 'mycommand myRequirements 1 2 --r3=3'
		holdme.set()
		args.parsed = args.parser.parse_args(line.split(' '))
		results = args.execute()
		stdout, stderr = holdme.get()
		holdme.unset()
		assert len(stderr) == 0
		logging.debug(json.dumps(results,indent=4))
		assert results['r1'] == '1'
		assert results['r2'] == '2'
		assert results['r3'] == '3'
	#________________________________________________________
	def test_20_UnDecorated(self):
		'''
		test the class outside of the Argue runtime
		'''
		from forTheSake import ForTheSake
		shouter = ForTheSake()
		notSet =  shouter.getSettable()
		assert notSet == 'notset'
		shouter.setSettable('preset')
		isSet = shouter.getSettable()
		assert isSet == 'preset'
		results = shouter.myMethod('1','2',p3='3')
		assert results['p1'] == '1'
		assert results['p2'] == '2'
		assert results['p3'] == '3'
		assert results['p4'] == 'd4'
		logging.debug(json.dumps(results,indent=4))
		del shouter
	#________________________________________________________
	def test_21_DodgySingle(self):
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			from dodgySingle import GoodBoy, BadBoy, args
			args.parse([])
			args.execute()
			print(cm)
		stdout, stderr = holdme.get()
		holdme.unset()
		assert 'single already defined, ignoring non single BadBoy' in stderr
		patternCheck(['gb1','args'],stderr)
		
	#________________________________________________________
	def test_22_WeirdSingle(self):
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			from weirdSingle import GoodBoy, BadBoy, args
			args.parse([])
			args.execute()
			print(cm)
		stdout, stderr = holdme.get()
		holdme.unset()
		assert 'single already defined, ignoring single BadBoy' in stderr
		patternCheck(['gb1','args'],stderr)
		
	#________________________________________________________
	def test_23_HappySingle(self):
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			from happySingle import GoodBoy, BadBoy, args
			args.parse([])
			args.execute()
			print(cm)
		stdout, stderr = holdme.get()
		holdme.unset()
		assert 'non single already defined, ignoring single BadBoy' in stderr
		assert '{GoodBoy,args}' in stderr
		
	#________________________________________________________
	def test_24_SimpleOne(self):
		holdme.set()
		from simple import args,g1,G2,g3,g4,g5,g6
		ns = args.parse('-g 3 --g2 2 --g1 1 -b --two=2'.split())
		stdout, stderr = holdme.get()
		holdme.unset()
		#print ns
		#for g in g1,G2,g3,g4,g5,g6:
			#print "%s=%s"%(g,g())
			
		assert len(stderr) == 0
		assert g1() == '1'
		assert G2() == '2'
		assert g3() == '3'
		assert g4() == 'g4'
		assert g5() == 'bee'
		assert g6() == 2
		
	#________________________________________________________
	def test_25_SimpleHelp(self):
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			from simple import args
			args.parser.parse_args('-h'.split())
			print(cm)
		stdout, stderr = holdme.get()
		holdme.unset()
		#print stdout
		#print stderr
		assert '(--one ONE | --three THREE | --two TWO)' in stdout
		assert '(-a | -b | -c)' in stdout
		assert '[--g4 G4]' in stdout
		assert '[-g G3]' in stdout
		assert '[--g2 G2]' in stdout
		assert '[--g1 G1]' in stdout
		
	#________________________________________________________
	def test_26_Neither(self):
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			from Either import args
			args.parse('do -h'.split())
			print(cm)
		stdout, stderr = holdme.get()
		holdme.unset()
		#print stdout
		#print stderr
		assert len(stderr) == 0
		assert '(--x X | --y Y | --z Z)' in stdout
		assert '(-a | -b | -c)' in stdout
		
	#________________________________________________________
	def test_27_One(self):
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			from Either import args
			args.parser.parse_args(['do'])
			print(cm)
		stdout, stderr = holdme.get()
		holdme.unset()
		#print stdout
		#print stderr
		assert "error: one of the arguments --x --y --z is required" in stderr
		
	#________________________________________________________
	def test_28_Other(self):
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			from Either import args
			args.parser.parse_args('do -b'.split())
			print(cm)
		stdout, stderr = holdme.get()
		holdme.unset()
		assert "error: one of the arguments --x --y --z is required" in stderr
		
	#________________________________________________________
	def test_29_MultiChoice(self):
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			from Either import args
			args.parser.parse_args('do -a -b --y=2'.split())
			print(cm)
		stdout, stderr = holdme.get()
		holdme.unset()
		
	#________________________________________________________
	def test_30_MultiEither(self):
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			from Either import args
			args.parser.parse_args('do -b --y=2 --z=3'.split())
			print(cm)
		stdout, stderr = holdme.get()
		holdme.unset()
		assert "error: argument --z: not allowed with argument --y" in stderr
	#________________________________________________________
	def test_31_MultiBoth(self):
		holdme.set()
		from Either import args
		args.parse('-x --one=1 do -a --y=2'.split())
		results = args.execute()
		stdout, stderr = holdme.get()
		holdme.unset()
		#print results
		#print stdout
		#print stderr
		assert len(stderr) == 0
		assert results['a1'] == 1
		assert results['a2'] == 'xml'
		assert results['choice'] == 'aye'
		assert results['either'] == 2
		
	#________________________________________________________
	def test_32_DocHelp(self):
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			from Procument import args
			args.parse('m2 -h'.split())
			print(cm)
		stdout, stderr = holdme.get()
		holdme.unset()
		#print stdout
		assert '[--p2 {a,b,c}]' in stdout
		assert '[-a | -b | -c]' in stdout
		assert '[-x X | -y Y | -z Z]' in stdout
		assert 'p1            arg 1, default=2' in stdout
		assert '-x X, --x X   help x' in stdout
		assert '-y Y, --y Y   help y' in stdout
		assert '-z Z, --z Z   help z' in stdout
		
	#________________________________________________________
	def test_33_PropHelp(self):
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			from Procument import args
			args.parser.parse_args('m1 -h'.split())
			print(cm)
		stdout, stderr = holdme.get(output=False)
		holdme.unset()
		#print stdout
		assert '[--p2 {a,b,c}]' in stdout
		assert '[-x X | -y Y | -z Z]' in stdout
		assert '[-a | -b | -c]' in stdout
		assert 'p1            arg 1, default=2' in stdout
		assert '-a, --aye' in stdout
		assert '-b, --bee' in stdout
		assert '-c, --cee' in stdout
		assert '-x X, --x X   help x' in stdout
		assert '-y Y, --y Y   help y' in stdout
		assert '-z Z, --z Z   help z' in stdout
		
	#________________________________________________________
	def test_34_PropHelp(self):
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			from Procument import args
			args.parser.parse_args('m2 -h'.split())
			print(cm)
		stdout, stderr = holdme.get(output=False)
		holdme.unset()
		#print stdout
		assert '[--p2 {a,b,c}]' in stdout
		assert '[-x X | -y Y | -z Z]' in stdout
		assert '[-a | -b | -c]' in stdout
		assert 'p1            arg 1, default=2' in stdout
		assert '-a, --aye' in stdout
		assert '-b, --bee' in stdout
		assert '-c, --cee' in stdout
		assert '-x X, --x X   help x' in stdout
		assert '-y Y, --y Y   help y' in stdout
		assert '-z Z, --z Z   help z' in stdout
		
	#________________________________________________________
	def test_35_PropHelp(self):
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			from Procument import args
			args.parser.parse_args('m3 -h'.split())
			print(cm)
		stdout, stderr = holdme.get(output=False)
		holdme.unset()
		#print stdout
		assert '[--p2 {a,b,c}]' in stdout
		assert '[-x X | -y Y | -z Z]' in stdout
		assert '[-a | -b | -c]' in stdout
		assert 'p1            arg 1, default=2' in stdout
		assert '-a, --aye' in stdout
		assert '-b, --bee' in stdout
		assert '-c, --cee' in stdout
		assert '-x X, --x X   help x' in stdout
		assert '-y Y, --y Y   help y' in stdout
		assert '-z Z, --z Z   help z' in stdout
		
	#________________________________________________________
	def test_36_TickTockValid(self):
		holdme.set()
		from TickTock import args
		args.parse([
		'--now_argument','2017-05-18 17:22:00',
		'tick',
		'--now_attribute','2017-05-18 17:22:00',
		'tock', '2017-05-18 17:22:00',
		'--p2','2017-05-18 17:22:00',
		'--p3','2017-05-18 17:22:00'
		])
		stdout, stderr = holdme.get()
		holdme.unset()
		#print stderr
		results = args.execute()
		#print results
		dts = datetime(2017, 5, 18, 17, 22)
		assert results['p1'] == dts
		assert results['p2'] == dts
		assert results['p3'] == dts
		assert results['argument'] == dts
		assert results['attribute'] == dts
		
	#________________________________________________________
	def test_37_TickTockHelp(self):
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			from TickTock import args
			args.parser.parse_args('tick tock -h'.split())
			print(cm)
		stdout, stderr = holdme.get()
		holdme.unset()
		#print stdout
		assert 'p1          p1 datetime' in stdout
		assert '--p2 P2     p2 datetime' in stdout
		assert '--p3 P3     p3 datetime' in stdout
		
	#________________________________________________________
	def test_38_TickTockInvalid(self):
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			from TickTock import args
			args.parser.parse_args(['tick','tock','2017-18-05 17:22:00'])
			print(cm)
		stdout, stderr = holdme.get()
		holdme.unset()
		#print stderr
		assert 'error: argument p1: invalid <lambda> value: \'2017-18-05 17:22:00\'' in stderr
		
	#________________________________________________________
	def test_39_TickTockInvalid(self):
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			from TickTock import args
			args.parser.parse_args(['tick','tock','2017-05-18 17:22:00','--p2','2017-18-05 17:22:00','--p3','2017-05-18 17:22:00'])
			print(cm)
		stdout, stderr = holdme.get()
		holdme.unset()
		#print stderr
		assert 'error: argument --p2: invalid <lambda> value: \'2017-18-05 17:22:00\'' in stderr
		
	#________________________________________________________
	def test_40_TickTockInvalid(self):
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			from TickTock import args
			args.parser.parse_args(['tick','tock','2017-05-18 17:22:00','--p2','2017-05-18 17:22:00','--p3','2017-18-05 17:22:00'])
			print(cm)
		stdout, stderr = holdme.get()
		holdme.unset()
		#print stderr
		assert 'error: argument --p3: invalid <lambda> value: \'2017-18-05 17:22:00\'' in stderr
		
	#________________________________________________________
	def test_41_BubbaArgueHelp(self):
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			from BubbaArgue import args
			args.parse('-h'.split(' '))
			print(args.execute())
		stdout, stderr = holdme.get(output=False)
		holdme.unset()
		#print stderr
		assert len(stderr) == 0
		patternCheck(['mum','bub','args'],stdout)
		assert '-v VERBOSE, --verbose VERBOSE' in stdout
		assert '-d DEBUG, --debug DEBUG' in stdout
		
	#________________________________________________________
	def test_42_PropertlyRaw(self):
		from Propertly import TestMe
		tm = TestMe()
		tm.run()
		
	#________________________________________________________
	def test_43_ValuableHelp(self):
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			from Propertly import args
			args.parse('valuable -h'.split(' '))
			print(args.execute())
		stdout, stderr = holdme.get(output=False)
		holdme.unset()
		#print stderr
		assert len(stderr) == 0
		assert '-v VALUE, --value VALUE' in stdout
		
	#________________________________________________________
	def test_44_PropertlyHelp(self):
		holdme.set()
		with self.assertRaises(SystemExit) as cm:
			from Propertly import args
			args.parse('just -h'.split(' '))
			print(args.execute())
		stdout, stderr = holdme.get(output=False)
		holdme.unset()
		#print stderr
		assert len(stderr) == 0
		assert '-V VALUE, --value VALUE' in stdout
		
	#________________________________________________________
	def _test_45_ValuableArgs(self):
		holdme.set()
		from Propertly import args
		args.parse('valuable -v bob do it'.split())
		stdout, stderr = holdme.get()
		holdme.unset()
		#print stderr
		results = args.execute()
		#print results
		assert results == '^bob$'
		
	#________________________________________________________
	def _test_46_PropertlyArgs(self):
		holdme.set()
		from Propertly import args
		args.parse('just -V bill do it'.split())
		stdout, stderr = holdme.get()
		holdme.unset()
		#print stderr
		results = args.execute()
		#print results
		assert results == '^bill$'
		
	#________________________________________________________
	def test_47_DuckArgs(self):
		holdme.set()
		from Propertly import args
		args.parse('duck -V quack do it'.split())
		stdout, stderr = holdme.get()
		holdme.unset()
		#print stderr
		results = args.execute()
		#print results
		assert results == '^quack$'
		
#============================================================
if __name__ == '__main__':
	level = logging.INFO
	#level = logging.DEBUG
	logging.basicConfig(level=level)
	unittest.main(exit=True)


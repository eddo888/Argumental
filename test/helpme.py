#!/usr/bin/env python3

import os,re,sys,argparse

from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(
	formatter_class=RawTextHelpFormatter,
	description='Process some integers\nand make it fast',
)

#parser.description = 'modified in post'

parser.add_argument(
	'integers', 
	metavar='N', 
	type=int, 
	nargs='+',
    help='an integer for the accumulator'
)

parser.add_argument(
	'--sum', 
	dest='accumulate', 
	action='store_const',
    const=sum, 
	default=max,
    help='sum the integers (default: find the max)'
)

args = parser.parse_args()

print(args.accumulate(args.integers))

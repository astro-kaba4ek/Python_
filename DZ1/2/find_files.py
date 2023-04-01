# coding: utf-8

import pathlib as pl
import argparse 

parser = argparse.ArgumentParser() 
parser.add_argument("-dir", dest="dir", default=pl.Path.cwd(), type=pl.Path)
parser.add_argument("-text", dest="text")

args = parser.parse_args()


for filename in args.dir.iterdir():
	
	file = open(filename, "r", encoding="utf-8")

	count = 0
	for line in file:
		str_start = line.find(args.text)
		str_end = str_start + len(args.text)

		count += 1
		if str_start != -1:
			print(filename.name, " " , count, " ", 
			line[:str_start], "\033[31m{}\033[0m".format(line[str_start:str_end]), line[str_end:].rstrip("\n"), sep="")

	file.close()
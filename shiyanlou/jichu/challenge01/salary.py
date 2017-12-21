#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import sys

# get config file

# get user data 

# path

class Path():
	def __init__(self, *args):
		self.__args = args
		self.__path = {}

		self.set_path()

	def set_path(self):
		if len(sys.argv) == 7:
			for arg in self.__args:
				self.__path[arg] = sys.argv[sys.argv.index(arg) + 1]
	
	@property
	def path(self):
		return self.__path

if __name__ == "__main__":
	paths = Path('-c','-d','-o').path
	cfg_path, user_path, result_path = paths['-c'], paths['-d'], path['-o']

	print(user_path)
	print(cfg_path)


#-*-  coding: utf-8 -*-

import re

path = input("Enter your file's path: ")

with open(path) as f:
	for line in f.readlines():
		email=re.findall(r'[0-9a-zA-Z._-]*@[0-9a-zA-Z._-]*\.[a-z]{3}',line)
		if(len(email) > 0 ):
			print(email)
		

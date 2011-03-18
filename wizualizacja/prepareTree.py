#!/usr/bin/env python

from couchquery import *
import json
import sys

tree = {}

server_url='http://sigma.inf.ug.edu.pl:14016/marketproduct'
db = Database(server_url)

for key, value in db.views.marketproduct.podaz(group_level=3).items():
	try:
		if len(tree[key[0]]) != 0:
			try:
				if len(tree[key[0]][key[1]]) != 0:
					tree[key[0]][key[1]][key[2]] = value
			except KeyError:
				tree[key[0]][key[1]] = {}
				tree[key[0]][key[1]][key[2]] = value
	except KeyError:
		tree[key[0]] = {}
		tree[key[0]][key[1]] = {}
		tree[key[0]][key[1]][key[2]] = value

f = open('tree.js', 'w')
f.write("var data = "+json.dumps(tree)+";")
	

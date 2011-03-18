#!/usr/bin/env python

from couchquery import *
import json
import sys

server_url='http://sigma.inf.ug.edu.pl:14016/marketproduct'
db = Database(server_url)

total = 0;
nodes = []
links = []
categories_id = {}
categories_val = {}
groups_val = {}
groups_id = {}

for doc in db.views.marketproduct.podaz():
  total =  doc

nodes.append({"nodeName":"Total:\n"+str(total),"group":0})


for key, value in db.views.marketproduct.podaz(group_level=1).items():
	id = len(nodes)
	nodes.append({"nodeName":key[0]+":\n"+str(value),"group":id})
	val = 0
	categories_id[key[0]]=id
	categories_val[key[0]]=value
	if value != 0:
		val = int((value*1000)/total)
	links.append({"source":0,"target":id,"value":val})

f = open('data.js', 'w')

f.write("var data = {nodes:"+json.dumps(nodes))
f.write(",\n")
f.write("links:"+json.dumps(links)+"};")
	
for key, value in db.views.marketproduct.podaz(group_level=3).items():
	pass	



#!/usr/bin/env python

from couchquery import *
import json
import sys

server_url='http://sigma.inf.ug.edu.pl:14016/marketproduct'
db = Database(server_url)

total = 0;
nodes = []
links = []

for doc in db.views.marketproduct.podaz():
  total =  doc

nodes.append({"nodeName":"total:\n"+str(total),"group":0})


for key, value in db.views.marketproduct.podaz(group_level=1).items():
	id = len(nodes)
	nodes.append({"nodeName":key[0]+":\n"+str(value),"group":id})
	links.append({"source":0,"target":id,"value":2})

#http://sigma.inf.ug.edu.pl:14016/marketproduct/_design/marketproduct/_view/podaz?group_level=0


#pobrac wszystkie jsony z coucha (do lvl 3 wlacznie)

#zbudowac tablice node-ow i linkow

f = open('data.js', 'w')

f.write("var nodes = {nodes:"+json.dumps(nodes)+"}")
f.write("\n,")
f.write("links = {links:"+json.dumps(links)+"}")



#!/usr/bin/env python

from couchquery import *
import sys

server_url='http://sigma.inf.ug.edu.pl:14016/marketproduct'
db = Database(server_url)

total = 0;

for doc in db.views.marketproduct.podaz():
  total =  doc

print total


for key, value in db.views.marketproduct.podaz(group_level=1).items():
  print key

#http://sigma.inf.ug.edu.pl:14016/marketproduct/_design/marketproduct/_view/podaz?group_level=0


#pobrac wszystkie jsony z coucha (do lvl 3 wlacznie)

#zbudowac tablice node-ow i linkow

#zrzucic do jsona

#zapisac w pliku data dane jsona

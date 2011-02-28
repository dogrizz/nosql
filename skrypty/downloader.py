#!/usr/bin/python

from couchdb import *
import sys
from xml.dom import minidom

nazwa = 'MarketProduct'
lista_json = []
db = None
cNodes = []
server_url='http://sigma.inf.ug.edu.pl:14016'


def upload(product):
  if product.get('Name') != None:
    product['_id']= product.get('MarketProductId')
    db.save(product)
    print('Zapisano '+product['Name'])

def wczytaj():
  DOMTree = minidom.parse(sys.argv[1])
  cNodes = DOMTree.childNodes

  for node in cNodes[1].getElementsByTagName(nazwa):
    product = {}
    for element in node.childNodes:
      try:
        product[element.nodeName]=element.childNodes[0].data
      except:
        try:
          product[element.nodeName]=element.data
        except:
          product[element.nodeName]=None
    del product["#text"]
    upload(product) 

if __name__ == "__main__":
  
  server = Server(url=server_url)
 
  if len(sys.argv) < 2:
    print "Nalezy podac nazwe pliku"
    sys.exit() 

  try:
    server.create(nazwa.lower())
  except:
    print "Baza juz istnieje"
    sys.exit()

  db = server[nazwa.lower()]
  
  wczytaj()


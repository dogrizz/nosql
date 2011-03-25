#!/usr/bin/env python
from couchdb import *
from couchdb.design import ViewDefinition

server = Server('http://sigma.inf.ug.edu.pl:14016')
nazwaBazy = "marketproduct"

db = server[nazwaBazy]

popyt = ViewDefinition(nazwaBazy, 'popyt',
'''function(doc) { 
    var val = parseInt(doc.BuyOrders); 
    emit([doc.CategoryName, doc.GroupName,doc.Name], val); 
  }''' ,"_sum")

podaz = ViewDefinition(nazwaBazy, 'podaz',
'''function(doc) { 
    var val = parseInt(doc.SellOrders); 
    emit([doc.CategoryName, doc.GroupName,doc.Name], val); 
  }''',"_sum")

ViewDefinition.sync_many(db, [popyt,podaz ])

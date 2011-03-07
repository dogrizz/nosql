// couchapp push wc.js http://Admin:Pass@localhost:4000/gutenberg

var couchapp = require('couchapp');

ddoc = {
    _id: '_design/app'
  , views: {}
  , lists: {}
  , shows: {}
}
module.exports = ddoc;

ddoc.views.popyt = {
  map: function(doc) {
    var val = parseInt(doc.BuyOrders);
    emit([doc.CategoryName, doc.GroupName,doc.Name], val);
  },
  reduce: "_sum"
}

ddoc.views.podaz = {
  map: function(doc) { 
    var val = parseInt(doc.SellOrders);
    emit([doc.CategoryName, doc.GroupName,doc.Name], val);
  },
  reduce: "_sum"
}


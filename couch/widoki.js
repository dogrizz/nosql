// couchapp push widoki.js http://localhost:14016/marketproduct

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


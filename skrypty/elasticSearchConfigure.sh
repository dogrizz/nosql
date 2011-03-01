#!/bin/bash

if [ $# != 1 ] 
then 
	echo "poprawne uzycie: $0 db_name"
	exit
fi

curl -XPUT 'localhost:9200/_river/$1_idx/_meta' -d '{
    "type" : "couchdb",
    "couchdb" : {
        "host" : "sigma.inf.ug.edu.pl",
        "port" : 14016,
        "db" : "$1",
        "filter" : null
    },
        "index" : "$1_idx",
        "type" : "$1",
        "bulk_size" : "100",
        "bulk_timeout" : "10ms"
    }
}'
if [ $? == 0  ]
then 
  echo "Powinno sie dac sie zadawac zapytania na http://localhost:9200/$1_idx/$1"
fi


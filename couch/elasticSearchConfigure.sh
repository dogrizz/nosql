#!/bin/bash

if [ $# != 1 ] 
then 
	echo "poprawne uzycie: $0 db_name"
	exit
fi

curl -XPUT 'localhost:9200/_river/'$1'/_meta' -d '{
    "type" : "couchdb",
    "couchdb" : {
        "host" : "localhost",
        "port" : 5984,
        "db" : "'$1'",
        "filter" : null
    },
    "index" : {
        "index" : "'$1'",
        "type" : "'$1'",
        "bulk_size" : "100",
        "bulk_timeout" : "10ms"
    }
}'
if [ $? == 0  ]
then 
  echo
  echo "Powinno sie dac sie zadawac zapytania na http://localhost:9200/$1/$1"
fi


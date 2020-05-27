#!/usr/bin/env bash 

echo "== Set variables =="
export node=172.26.133.229
export masternode=172.26.133.229
export size=3
export user=admin
export pass=admin
export VERSION='3.0.0'
export cookie='a192aeb9904e6590849337933b000c99'
export uuid='d4f7112a8d8ed58016aeac66cbe8ac22'

echo "== Get CouchDB =="
docker pull ibmcom/couchdb3:${VERSION}

echo "== Start container Master==="
if [ ! -z $(docker ps --all --filter "name=couchdb${node}" --quiet) ] 
    then
        docker stop $(docker ps --all --filter "name=couchdb${node}" --quiet) 
        docker rm $(docker ps --all --filter "name=couchdb${node}" --quiet)
fi

docker create --name couchdb${node} -p 5984:5984 -p 4369:4369 -p 9100-9200:9100-9200 --env COUCHDB_USER=${user} --env COUCHDB_PASSWORD=${pass} --env COUCHDB_SECRET=${cookie} --env ERL_FLAGS="-setcookie \"${cookie}\" -name \"couchdb@${node}\"" ibmcom/couchdb3:${VERSION}

declare -a conts=(`docker ps --all | grep couchdb | cut -f1 -d' ' | xargs -n3 -d'\n'`)
for cont in "${conts[@]}"; do docker start ${cont}; done
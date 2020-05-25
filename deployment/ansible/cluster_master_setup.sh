#!/usr/bin/env bash

echo "== Set variables =="
export nodes=172.26.133.229
export masternode=172.26.133.229
export size=3
export user=admin
export pass=admin
export VERSION='3.0.0'
export cookie='a192aeb9904e6590849337933b000c99'
export uuid='d4f7112a8d8ed58016aeac66cbe8ac22'

echo "== Setup cluster ==="
curl -X POST -H "Content-Type: application/json" http://${user}:${pass}@172.26.133.229:5984/_cluster_setup  -d '{"action":"enable_cluster", "bind_address":"0.0.0.0", "username":"admin", "password":"admin", "port":"5984", "remote_node":"172.26.133.229", "node_count":"3", "remote_current_user":"admin", "remote_current_password":"admin"}'
curl -X POST -H "Content-Type: application/json" http://${user}:${pass}@172.26.133.229:5984/_cluster_setup  -d '{"action":"enable_cluster", "bind_address":"0.0.0.0", "username":"admin", "password":"admin", "port":"5984", "remote_node":"172.26.133.240", "node_count":"3", "remote_current_user":"admin", "remote_current_password":"admin"}'
curl -X POST -H "Content-Type: application/json" http://${user}:${pass}@172.26.133.229:5984/_cluster_setup  -d '{"action":"enable_cluster", "bind_address":"0.0.0.0", "username":"admin", "password":"admin", "port":"5984", "remote_node":"172.26.134.32", "node_count":"3", "remote_current_user":"admin", "remote_current_password":"admin"}'


echo "== Add nodes ==="
curl -X POST -H "Content-Type: application/json" http://${user}:${pass}@172.26.133.229:5984/_cluster_setup  -d '{"action":"add_node", "host":"172.26.133.240", "username":"admin", "password":"admin", "port":"5984"}'
curl -X POST -H "Content-Type: application/json" http://${user}:${pass}@172.26.133.229:5984/_cluster_setup  -d '{"action":"add_node", "host":"172.26.134.32", "username":"admin", "password":"admin", "port":"5984"}'


# THis empty request is to avoid an error message when finishing the cluster setup 
curl -XGET "http://${user}:${pass}@172.26.133.229:5984/"


echo "== Finish cluster =="
curl -X POST -H "Content-Type: application/json" http://${user}:${pass}@172.26.133.229:5984/_cluster_setup -d '{"action": "finish_cluster"}'

# echo "== Check nodes =="
# # curl -X GET http://admin:admin@172.26.133.229:5984/_membership
# curl -X GET "http://${user}:${pass}@${masternode}:5984/_membership"

# echo "== Test create DB =="
# curl -X PUT "http://${user}:${pass}@${masternode}:5984/test1"
# curl -X GET "http://${user}:${pass}@172.26.133.240:5984/_all_dbs" 
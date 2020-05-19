#!/usr/bin/env bash

echo "== Set variables =="
export declare -a nodes=(172.26.132.216 172.26.128.114 172.26.134.61)
export declare -a ports=(5984 15984 25984)
export masternode=`echo ${nodes} | cut -f1 -d' '`
export declare -a othernodes=`echo ${nodes[@]} | sed s/${masternode}//`
export size=${#nodes[@]}
export user=admin
export pass=admin
export VERSION='3.0.0'
export cookie='a192aeb9904e6590849337933b000c99'
export uuid='d4f7112a8d8ed58016aeac66cbe8ac22'

echo "== Get CouchDB =="
docker pull ibmcom/couchdb3:${VERSION}

echo "== Start the containers =="
for node in "${nodes[@]}" 
  do
    if [ ! -z $(docker ps --all --filter "name=couchdb${node}" --quiet) ] 
       then
         docker stop $(docker ps --all --filter "name=couchdb${node}" --quiet) 
         docker rm $(docker ps --all --filter "name=couchdb${node}" --quiet)
    fi 
done

# for node in "${nodes[@]}" 
#   do
#     docker create\
#       --name couchdb${node}\
#       --publish 5984:5984\
#       --publish 4369:4369\
#       --publish 9100:9100\
#       --env COUCHDB_USER=${user}\
#       --env COUCHDB_PASSWORD=${pass}\
#       --env COUCHDB_SECRET=${cookie}\
#       --env ERL_FLAGS="-setcookie \"${cookie}\" -name \"couchdb@${node}\""\
#       ibmcom/couchdb3:${VERSION}
# done

for (( i=0; i<${size}; i++ )); 
  do
    docker create\
      --name couchdb${nodes[${i}]}\
      -p ${ports[${i}]}:5984\
      --env COUCHDB_USER=${user}\
      --env COUCHDB_PASSWORD=${pass}\
      --env COUCHDB_SECRET=${cookie}\
      --env ERL_FLAGS="-setcookie \"${cookie}\" -name \"couchdb@${nodes[${i}]}\""\
      ibmcom/couchdb3:${VERSION}
done

declare -a conts=(`docker ps --all | grep couchdb | cut -f1 -d' ' | xargs -n${size} -d'\n'`)

for cont in "${conts[@]}"; do docker start ${cont}; done

echo "== Setup cluster =="
curl -X POST -H "Content-Type: application/json" http://admin:admin@172.26.132.216:5984/_cluster_setup  -d '{"action":"enable_cluster", "bind_address":"0.0.0.0", "username":"admin", "password":"admin", "port":"25984", "remote_node":"172.26.134.61", "node_count":"3", "remote_current_user":"admin", "remote_current_password":"admin"}'
curl -X POST -H "Content-Type: application/json" http://admin:admin@172.26.132.216:5984/_cluster_setup  -d '{"action":"enable_cluster", "bind_address":"0.0.0.0", "username":"admin", "password":"admin", "port":"15984", "remote_node":"172.26.128.114", "node_count":"3", "remote_current_user":"admin", "remote_current_password":"admin"}'

# for node in ${othernodes} 
# do
#     curl -XPOST "http://${user}:${pass}@${masternode}:5984/_cluster_setup" \
#       --header "Content-Type: application/json"\
#       --data "{\"action\": \"enable_cluster\", \"bind_address\":\"0.0.0.0\",\
#              \"username\": \"${user}\", \"password\":\"${pass}\", \"port\": \"5984\",\
#              \"remote_node\": \"${node}\", \"node_count\": \"$(echo ${nodes[@]} | wc -w)\",\
#              \"remote_current_user\":\"${user}\", \"remote_current_password\":\"${pass}\"}"
# done

curl -X POST -H "Content-Type: application/json" http://admin:admin@172.26.132.216:5984/_cluster_setup  -d '{"action":"add_node", "host":"172.26.128.114", "username":"admin", "password":"admin", "port":"15984"}'
curl -X POST -H "Content-Type: application/json" http://admin:admin@172.26.132.216:5984/_cluster_setup  -d '{"action":"add_node", "host":"172.26.134.61", "port":"25984", "username":"admin", "password":"admin"}'

# for node in ${othernodes}
# do
#     curl -XPOST "http://${user}:${pass}@${masternode}:5984/_cluster_setup"\
#       --header "Content-Type: application/json"\
#       --data "{\"action\": \"add_node\", \"host\":\"${node}\",\
#              \"port\": \"5984\", \"username\": \"${user}\", \"password\":\"${pass}\"}"
# done

# THis empty request is to avoid an error message when finishing the cluster setup 
curl -XGET "http://${user}:${pass}@${masternode}:5984/"

echo "== Finish cluster =="
curl -XPOST "http://${user}:${pass}@${masternode}:5984/_cluster_setup"\
    --header "Content-Type: application/json" --data "{\"action\": \"finish_cluster\"}"

echo "== Check nodes =="
# curl -X GET http://admin:admin@172.26.132.216:5984/_membership
for node in "${nodes[@]}"; do  curl -X GET "http://${user}:${pass}@${node}:5984/_membership"; done

echo "== Test create DB =="
curl -XPUT "http://${user}:${pass}@${masternode}:5984/test"
for node in "${nodes[@]}"; do  curl -X GET "http://${user}:${pass}@${node}:5984/_all_dbs"; done

# echo "== Set variables =="
# declare -a nodes=(172.26.134.36 172.26.130.123 172.26.130.204)
# declare -a ports=(5984 15984 25984)
# export master_node=172.26.134.36
# export master_port=5984
# export size=${#nodes[@]}
# export user=admin
# export pass=admin

# echo "== Start the containers =="
# docker-compose up -d

# sleep 30

# echo "== Enable cluster setup =="
# for (( i=0; i<${size}; i++ )); do
#   curl -X POST "http://${user}:${pass}@localhost:${ports[${i}]}/_cluster_setup" -H 'Content-Type: application/json' \
#     -d "{\"action\": \"enable_cluster\", \"bind_address\":\"0.0.0.0\", \"username\": \"${user}\", \"password\":\"${pass}\", \"node_count\":\"${size}\"}"
# done

# sleep 10

# echo "== Add nodes to cluster =="
# for (( i=0; i<${size}; i++ )); do
#   if [ "${nodes[${i}]}" != "${master_node}" ]; then
#     curl -X POST -H 'Content-Type: application/json' http://${user}:${pass}@127.0.0.1:${master_port}/_cluster_setup \
#       -d "{\"action\": \"enable_cluster\", \"bind_address\":\"0.0.0.0\", \"username\": \"${user}\", \"password\":\"${pass}\", \"port\": 5984, \"node_count\": \"${size}\", \
#            \"remote_node\": \"${nodes[${i}]}\", \"remote_current_user\": \"${user}\", \"remote_current_password\": \"${pass}\"}"
#     curl -X POST -H 'Content-Type: application/json' http://${user}:${pass}@127.0.0.1:${master_port}/_cluster_setup \
#       -d "{\"action\": \"add_node\", \"host\":\"${nodes[${i}]}\", \"port\": 5984, \"username\": \"${user}\", \"password\":\"${pass}\"}"
#   fi
# done

# sleep 10

# echo "== Finish cluster =="
# curl -X POST "http://${user}:${pass}@localhost:${master_port}/_cluster_setup" -H 'Content-Type: application/json' -d '{"action": "finish_cluster"}'

# curl http://${user}:${pass}@localhost:${master_port}/_cluster_setup

# echo "== Check nodes =="
# for port in "${ports[@]}"; do  curl -X GET http://${user}:${pass}@localhost:${port}/_membership; done

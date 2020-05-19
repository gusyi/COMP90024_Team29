export node=172.26.128.114
export masternode=172.26.132.216
export size=${#nodes[@]}
export user=admin
export pass=admin
export VERSION='3.0.0'
export cookie='a192aeb9904e6590849337933b000c99'
export uuid='d4f7112a8d8ed58016aeac66cbe8ac22'

echo "== Get CouchDB =="
docker pull ibmcom/couchdb3:${VERSION}

echo "== Start the containers =="
if [ ! -z $(docker ps --all --filter "name=couchdb${node}" --quiet) ] 
    then
        docker stop $(docker ps --all --filter "name=couchdb${node}" --quiet) 
        docker rm $(docker ps --all --filter "name=couchdb${node}" --quiet)
fi

docker create --name couchdb${node} -p 5984:5984 -p 4369:4369 -p 9100:9100 --env COUCHDB_USER=${user} --env COUCHDB_PASSWORD=${pass} --env COUCHDB_SECRET=${cookie} --env ERL_FLAGS="-setcookie \"${cookie}\" -name \"couchdb@${node}\"" ibmcom/couchdb3:${VERSION}

declare -a conts=(`docker ps --all | grep couchdb | cut -f1 -d' ' | xargs -n3 -d'\n'`)

for cont in "${conts[@]}"; do docker start ${cont}; done

echo "== Setup cluster =="
curl -X POST -H "Content-Type: application/json" http://admin:admin@172.26.132.216:5984/_cluster_setup  -d '{"action":"enable_cluster", "bind_address":"0.0.0.0", "username":"admin", "password":"admin", "port":"5984", "remote_node":"172.26.128.114", "node_count":"3", "remote_current_user":"admin", "remote_current_password":"admin"}'

echo "== Add node =="
curl -X POST -H "Content-Type: application/json" http://admin:admin@172.26.132.216:5984/_cluster_setup  -d '{"action":"add_node", "host":"172.26.128.114", "username":"admin", "password":"admin", "port":"5984"}'

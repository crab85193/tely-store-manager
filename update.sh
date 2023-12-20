#!/bin/bash

CURRENT_DIR=`cd $(dirname $0) && pwd`

container_id=`docker ps -q -f status=running -f name=store-manager`

if [ -z "$container_id" ]; then
    echo "store-manager is not running"
    exit 0
fi

docker exec -it store-manager python src/main.py

docker-compose -f docker-compose.prod.yml down

docker-compose -f docker-compose.prod.yml up -d
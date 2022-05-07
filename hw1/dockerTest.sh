#!/bin/bash
docker build -t fileio -f Dockerfile.fileio .
docker build -t cpu -f Dockerfile.cpu .
for spec in "1024m 1" "2048m 2" "4096m 4";
do
    set -- $spec
    echo "test memory: $1 , cpus: $2"
    docker run -m $1 --cpus $2 --memory-swap 2048m fileio
    docker run -m $1 --cpus $2 --memory-swap 2048m cpu
done
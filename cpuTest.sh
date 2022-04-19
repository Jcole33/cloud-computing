#!/bin/bash
echo "CPU TEST"
for maxPrime in 100 100000
do
    for i in 1 2 3 4 5
    do 
        echo "run: $i"
        time sysbench cpu --cpu-max-prime=$maxPrime --threads=4 --time=30 run
    done
done
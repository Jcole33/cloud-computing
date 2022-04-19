#!/bin/bash
echo "FILE IO TEST"
for mode in seqwr rndwr
do 
    echo "file test mode: $mode"
    for i in 1 2 3 4 5
    do
        echo "run $i"
        sysbench fileio --file-num=64 --file-total-size=2G prepare > /dev/null
        sysbench fileio --file-num=64 --file-total-size=2G --time=30 --threads=4 --file-test-mode=$mode run
        sysbench fileio cleanup > /dev/null
    done
done

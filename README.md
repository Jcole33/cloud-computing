## Main files: ##
Markup: *dockerTest.sh - Description: Builds and runs the cpu and fileio docker containers - Dependencies: Dockerfile.cpu, Dockerfile.fileio
Markup: *Dockerfile.cpu - Description: Docker file for container cpu test - Dependencies: cpuTest.sh
Markup: *Dockerfile.fileio - Description: Docker file for container fileio test - Dependencies: fileTest.sh
Markup: *cpuTest.sh - Description: Runs the sysbench cpu test with max prime = 100 and max prime = 100000 5 times each
Markup: *fileTest.sh - Description: Runs the sysbench fileio test with test mode = seqwr and test mode = rndwr 5 times each
Markup: *Cloud_Assignment1.pdf - Description: Report pdf

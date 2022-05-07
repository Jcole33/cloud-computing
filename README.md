## HW 1 Main files: ##
- dockerTest.sh - Description: Builds and runs the cpu and fileio docker containers - Dependencies: Dockerfile.cpu, Dockerfile.fileio
- Dockerfile.cpu - Description: Docker file for container cpu test - Dependencies: cpuTest.sh
- Dockerfile.fileio - Description: Docker file for container fileio test - Dependencies: fileTest.sh
- cpuTest.sh - Description: Runs the sysbench cpu test with max prime = 100 and max prime = 100000 5 times each
- fileTest.sh - Description: Runs the sysbench fileio test with test mode = seqwr and test mode = rndwr 5 times each
- Cloud_Assignment1.pdf - Description: Report pdf

## HW 2 Main Files: ##
- Cloud_Assignment2.pdf - Description: Report pdf (includes screenshots and question answers)
- functions/ - Description: folder including all files from the faas-cli tests

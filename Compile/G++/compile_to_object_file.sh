 #!/bin/sh
#$1 - object file name
#$2 - source file name
if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - object file name"
        echo "2 arg - source file name"
  exit 1
fi

g++ -Wall -g -c $2 -o $1.o

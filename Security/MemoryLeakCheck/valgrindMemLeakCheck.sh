#!/bin/sh

#$1 - full path to the executable

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - full path to the executable"
  exit 1
fi


valgrind --leak-check=full \
         --show-leak-kinds=all \
         --track-origins=yes \
         --verbose \
         --log-file=valgrind-out.txt \
         $1

echo "valgrind-out.txt has been created. Check it for more information."

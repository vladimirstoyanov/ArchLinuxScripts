#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg  - your program (e.g. ./some_program)"
  exit 1
fi

perf stat -e context-switches,cpu-migrations,task-clock $1

#!/bin/sh
if [ $# -ne 1 ]
then
	echo "1 arg - PID"
  exit 1
fi

/proc/$1/syscall

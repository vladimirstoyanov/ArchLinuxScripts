#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - a kernel module name (e.g. snd_xen_front)"
  exit 1
fi
modinfo $1

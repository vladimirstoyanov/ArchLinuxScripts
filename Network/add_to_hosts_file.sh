#!/bin/sh
if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - IP address"
        echo "2 arg - Host name"
  exit 1
fi


echo '$1  $2' >> /etc/hosts

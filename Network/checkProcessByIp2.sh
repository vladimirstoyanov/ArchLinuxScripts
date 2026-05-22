#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - IP address"
  exit 1
fi

IP="$1"

while true; do
    clear
    echo "Searching for: $IP"
    echo "------------------------"

    ss -tunapH | awk -v ip="$IP" '$0 ~ ip'

    sleep 1
done

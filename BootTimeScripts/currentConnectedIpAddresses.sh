#!/bin/sh
while true
do
        netstat -tnp > /tmp/list_connected_ip_addr.txt
	sleep 60
done

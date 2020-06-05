  GNU nano 4.9.2                                         scan_all_ports.sh                                                    
#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg  - ip address"
  exit 1
fi


tcpdump -X host $1

#!/bin/sh

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - username"
        echo "2 arg - host IP"
  exit 1
fi

echo "AllowUsers $1@$2" >> /etc/ssh/sshd_config
sudo systemctl restart sshd

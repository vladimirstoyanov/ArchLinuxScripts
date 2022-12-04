#!/bin/sh

if [ $# -ne 4 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - username"
        echo "2 arg - password"
        echo "3 arg - path to .ovpn file (e.g. /home/user/example.ovpn)"
        echo "4 arg - name of the .ovpn file (e.g. example.ovpn)"
  exit 1
fi


touch /etc/openvpn/credentials
printf '%s\n' '$1' '$2' > /etc/openvpn/credentials
cp $3 /etc/openvpn/$4
sed -i 's/auth-user-pass/auth-user-pass \/etc\/openvpn\/credentials/g' /etc/openvpn/$4
nohup openvpn --config /etc/openvpn/$4 &

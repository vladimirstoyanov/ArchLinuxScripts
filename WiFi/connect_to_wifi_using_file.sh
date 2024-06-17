#!/bin/sh

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - wpa conf filename (e.g. /etc/wpasupplicant.conf)"
        echo "2 arg - network interface (e.g. wlan0)"
  exit 1
fi

wpa_supplicant -B -D wext -i $2 -c $1

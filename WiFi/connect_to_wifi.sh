#!/bin/sh

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - SSID (name of your wifi network)"
        echo "2 arg - WiFi interface (e.g. wlan0)"
  exit 1
fi

wpa_passphrase $1 >> /etc/wpasupplicant.conf
wpa_supplicant -B -D wext -i $1 -c /etc/wpasupplicant.conf

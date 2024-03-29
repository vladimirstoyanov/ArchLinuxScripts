#!/bin/sh

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - SSID (e.g. sda1)"
        echo "2 arg - WiFi interface (e.g. wlan0)"
  exit 1
fi

wpa_passphrase $1 >> /etc/wpa_supplicant.conf
wpa_supplicant -B -D wext -i $2 -c /etc/wpa_supplicant.conf

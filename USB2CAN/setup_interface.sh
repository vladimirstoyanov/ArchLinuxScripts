#!/bin/sh

modprobe can_raw
modprobe can_dev
insmod usb_8dev.ko
ip link set can0 up type can bitrate 1000000 sample-point 0.875

modprobe can_raw
modprobe can_dev
insmod usb_8dev


sudo ip link set can0 type can bitrate 500000
sudo ip link set up can0

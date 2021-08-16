#!/bin/sh
while true
do
	cd $ARCH_LINUX_SCRIPTS_PATH/Plasma/PlasmaWidgets/curriences_rates/
	python2.7 currencies_rates.py
	sleep 3600
done

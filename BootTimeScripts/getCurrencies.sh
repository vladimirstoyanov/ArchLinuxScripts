#!/bin/sh
while true
do
	cd $1/Plasma/PlasmaWidgets/curriences_rates/
	python2.7 currencies_rates.py >>log.txt
	sleep 3600
done

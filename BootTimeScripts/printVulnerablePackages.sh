#!/bin/sh
while true
do
	cd ../Security/
	python printVulnerablePackages.py
	sleep 60
done

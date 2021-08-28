#!/bin/sh
while true
do
	cd $1/Security/
	python printVulnerablePackages.py
	sleep 60
done

#!/bin/sh
while true
do
	cd /home/scitickart/gitHub/ArchLinuxScripts/Security/
	python printVulnerablePackages.py
	sleep 60
done

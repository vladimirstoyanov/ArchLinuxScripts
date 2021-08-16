#!/bin/sh
while true
do
	cd $ARCH_LINUX_SCRIPTS_PATH/Security/
	python printVulnerablePackages.py
	sleep 60
done

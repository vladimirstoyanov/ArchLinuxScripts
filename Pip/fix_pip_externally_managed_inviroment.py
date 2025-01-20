import os
import sys
import subprocess

version = sys.version.split()[0]
major_minor_version = '.'.join(version.split('.')[:2])


print(f"rm /usr/lib/python{major_minor_version}/EXTERNALLY-MANAGED")
os.system(f"sudo rm /usr/lib/python{major_minor_version}/EXTERNALLY-MANAGED ")#/EXTERNALLY-MANAGED")

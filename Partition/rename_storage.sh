
#!/bin/sh

if [ $# -ne 1 ]
then
	echo "1 arg - volume (e.g. /dev/sdb)"
  echo "2 arg - volume name (e.g. Some_hard_drive)"
	exit 1
fi

e2label $1 $2

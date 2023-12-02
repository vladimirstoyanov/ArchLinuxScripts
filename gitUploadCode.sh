#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - comment"
  exit 1
fi

sh removeLogs.sh

echo "git add --all"
git add --all

echo "git commit -m $1"
git commit -m "$1"

PASSWORD=$(cat /home/vladimir/gitHubToken.txt)
echo $PASSWORD
echo "git push origin"
git push origin << EOF
vladimirstoyanov
$PASSWORD
EOF

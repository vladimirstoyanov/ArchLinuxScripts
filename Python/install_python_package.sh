  GNU nano 4.4                                     static_internet_sharing.sh                                                
#!/bin/sh
#$1 - package name

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "arg1 - Package name" 
  exit 1
fi

pip install $1

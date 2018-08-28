if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg  - SVG file name (<>.svg)"
  exit 1
fi


systemd-analyze plot > $1

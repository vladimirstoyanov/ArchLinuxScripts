#$1 - Label (Flash_Drive)
#$2 - path to flash drive (/dev/sdb)

sudo mkfs.vfat -I -F 32 -n '$1' $2

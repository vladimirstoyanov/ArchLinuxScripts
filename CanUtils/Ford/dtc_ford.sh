# В един терминал слушай за отговор от PCM (0x7E8):
isotprecv -s 0x7E0 -d 0x7E8 can0

# Във втори терминал изпрати заявката:
echo "19 02 08" | isotpsend -s 0x7E0 -d 0x7E8 can0

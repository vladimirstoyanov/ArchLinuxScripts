import os 

for i in range (1024):
	print ("exporting " + str(i))
	os.system ("sh export_pin_gpio.sh " + str(i))


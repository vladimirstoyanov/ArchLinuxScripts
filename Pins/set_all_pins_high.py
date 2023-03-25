import os
import time

class OlimexPins:
	def __init__ (self):
		self.pins = [#"gpio12_pg9",
   			#"gpio1_pb3",
			#"gpio4_pe4",
			#"gpio7_pe7",
			#"gpio10_pe10",
			#"gpio13_pg10",
			#"gpio2_pb4",
			#"gpio5_pe5",
			#"gpio8_pe8",
			#"gpio11_pe11",
  			#"gpio14_pg11",
			"gpio3_pb10"
  			#"gpio6_pe6",
  			#"gpio9_pe9"
			]

	def changeModePins (self, mode): #mode is "in" or "out"
		for i in range (len(self.pins)):
			os.system("echo " + mode + " > /sys/class/gpio/" + self.pins[i] + "/direction")
	
	def enablePins (self):
		for i in range (len(self.pins)):
			os.system("echo 1 > /sys/class/gpio/" + self.pins[i] + "/value")
	
	def disablePins (self):
                for i in range (len(self.pins)):
                        os.system("echo 0 > /sys/class/gpio/" + self.pins[i] + "/value")
			
	def setPinOn50Hz (self):
		for i in range (len(self.pins)):
                        os.system("echo 1 > /sys/class/gpio/" + self.pins[i] + "/value")
			time.sleep(3/1000.0)
                        os.system("echo 0 > /sys/class/gpio/" + self.pins[i] + "/value")
			time.sleep(3/1000.0)
olimexPins = OlimexPins()
olimexPins.changeModePins("out")

while (1):
	#print ("Enabling all pins...")
	#olimexPins.enablePins()
	#time.sleep(3)
	#print ("Disabling all pins...")
	#olimexPins.disablePins()
	#time.sleep(3)
	olimexPins.setPinOn50Hz()

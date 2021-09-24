import os

class DisableInputDevice:
	def __init__ (self, deviceName):
		self.deviceName = deviceName

	def disable (self):
		dir_path = os.path.dirname(os.path.realpath(__file__))

		os.system("xinput list > " + dir_path + "/list.txt")
		f = open (dir_path + "/list.txt", "r")

		for line in f.readlines():
			if (-1 != line.find(self.deviceName)):
				l_split = line.split('\t')
				l_split_id = l_split[1].split('=')
				os.system ('xinput --disable ' + l_split_id[1] + ' > result.txt')
				os.system ('cat result.txt')
				os.system ('rm result.txt')
		f.close()

		os.system('rm ' + dir_path + '/list.txt')

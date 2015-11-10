#!/usr/bin/python
import os
import subprocess
import time
import ettercap

# ToDo:
#	add default interface eth0 if selected is empty or not existend
#	add default ip address and check given address for correct format
#	add filter to redirect from https to http
#	change filter catFilter to replace all images ==> regex
#	give the possibility to change the image source
#	start wireshark with activated filter	

# Shows the ARP Spoofing menu
def arpMenu():
	showMenu = True
	while(showMenu):
		print("ARP Spoofing Menu")
		print("1.\tStart Ettercap in sniffing mode")
		print("2.\tStart Ettercap in fun mode")
		print("0.\tBack to main menu")
		selection = input("Your selection: ")
		etter = ettercap.ArpSpoofing()
		if(selection == 1):
			etter.start(etter, 1)
			#ettercapMITM()
		elif(selection == 2):
			etter.start(etter, 2)
			#ettercapFun()
		elif(selection == 0):
			print("\nBack to main menu...\n")
			showMenu = False

##########################################
# Show Menu
#########################################
showMenu = True
#while(showMenu):
while(showMenu):
	#Main Menu
	print("Main Menu")
	print("1.\tARP Spoofing")
	print("2.\tDNS Spoofing")
	print("0.\tExit Programm")
	mainSelection = input("Your selection: ")
	if(mainSelection == 1):
		arpMenu()
	elif(mainSelection == 2):
		print("DNS Spoofing Menu")
	elif(mainSelection == 0):
		print("\nExiting\n")
		showMenu = False


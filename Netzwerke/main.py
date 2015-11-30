#!/usr/bin/python
import os
import subprocess
import time
#import ettercap
import colors
from ettercap import ettercap
from dnsspoofing import DNSSpoofing

# ToDo:
#	add default interface eth0 if selected is empty or not existend
#	add default ip address and check given address for correct format
#	add filter to redirect from https to http
#	change filter catFilter to replace all images ==> regex
#	give the possibility to change the image source
#	start wireshark with activated filter	

# Shows the ARP Spoofing menu
def arpMenu():
	shellCols = colors.ShellColors
	showMenu = True
	while(showMenu):
		subprocess.call(["clear"])
		print shellCols.UNDERLINE + shellCols.HEADER + "ARP Spoofing Menu" + shellCols.ENDC
		print shellCols.WARNING + "1.\tStart Ettercap in sniffing mode" + shellCols.ENDC
		print shellCols.WARNING + "2.\tStart Ettercap in fun mode" + shellCols.ENDC
		print shellCols.WARNING + "0.\tBack to main menu" + shellCols.ENDC
		selection = input(shellCols.BLUE + "\nYour selection: " + shellCols.ENDC)
		etter = ettercap.ArpSpoofing()
		if(selection == 1):
			etter.start(etter, 1)
			#ettercapMITM()
		elif(selection == 2):
			etter.start(etter, 2)
			#ettercapFun()
		elif(selection == 0):
			print "\nBack to main menu...\n"
			showMenu = False
		else:
			print "Not valid"

def dnsMenu():
	shellCols = colors.ShellColors
	showMenu = True
	while(showMenu):
		subprocess.call(["clear"])
		print shellCols.UNDERLINE + shellCols.HEADER + "DNS Spoofing Menu" + shellCols.ENDC
		print shellCols.WARNING + "1.\tStart DNS Spoofing Attack" + shellCols.ENDC
		print shellCols.WARNING + "2.\tShow Help" + shellCols.ENDC
		print shellCols.WARNING + "0.\tBack to main menu" + shellCols.ENDC
		selection = input(shellCols.BLUE + "\nYour selection: " + shellCols.ENDC)
		dnsSpoof = DNSSpoofing.DNSSpoofing()
		if(selection == 1):
			dnsSpoof.start()
		elif(selection == 2):
			dnsSpoof.help()
			raw_input(shellCols.BLUE + "\nPress Enter to continue " + shellCols.ENDC)
		elif(selection == 0):
			print "\nBack to main menu...\n"
			showMenu = False
		else:
			print "Not valid"

##########################################
# Show Menu
#########################################
showMenu = True
#while(showMenu):
while(showMenu):
	shellCols = colors.ShellColors
	#Main Menu
	subprocess.call(["clear"])
	print shellCols.UNDERLINE + shellCols.HEADER + "Main Menu" + shellCols.ENDC
	print shellCols.WARNING + "1.\tARP Spoofing" + shellCols.ENDC
	print shellCols.WARNING + "2.\tDNS Spoofing" + shellCols.ENDC
	print shellCols.WARNING + "0.\tExit Programm" + shellCols.ENDC
	mainSelection = input(shellCols.BLUE + "\nYour selection: " + shellCols.ENDC)
	if(mainSelection == 1):
		arpMenu()
	elif(mainSelection == 2):
		dnsMenu()
	elif(mainSelection == 0):
		print "\nExiting\n"
		showMenu = False


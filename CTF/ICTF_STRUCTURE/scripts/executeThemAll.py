# -*- coding: utf-8 -*-
import random
import string
import socket
import sys
import time
import os
import pexpect
import pexpect.fdpexpect
sys.path.append(os.getcwd())
import setflag
import getflag
import exploit
import benign


if __name__ == "__main__":
	ip = "127.0.0.1"
	port = 1337
	submit_flag = "FLG" + ''.join(random.choice(string.lowercase) for i in range(random.randint(6,15)))
	print "flag to submit: " + submit_flag
	print "----------------------SETFLAG----------------------"
	print "----------------------SETFLAG----------------------"
	print "----------------------SETFLAG----------------------"
	print "----------------------SETFLAG----------------------"
	print "----------------------SETFLAG----------------------"
#	setflag_ret = setflag.set_flag(ip, int(port), "FLGRQwiFiJD3SiBK")
	setflag_ret = setflag.set_flag(ip, int(port), submit_flag)
	print setflag_ret
	print "----------------------xx----------------------"
	print "----------------------xx----------------------"
	flag_id =  setflag_ret['FLAG_ID']
	print "flag_id: " + flag_id
	token = setflag_ret['TOKEN']
	print "token: " + token
	print "----------------------xx----------------------"


	time.sleep(2)
	print "----------------------GETFLAG----------------------"
	print "----------------------GETFLAG----------------------"
	print "----------------------GETFLAG----------------------"
	print "----------------------GETFLAG----------------------"
	print "----------------------GETFLAG----------------------"
	print getflag.get_flag(ip, int(port), flag_id, token)
	print "----------------------xx----------------------"
	print "----------------------xx----------------------"


	time.sleep(2)
	print "----------------------EXPLOIT----------------------"
	print "----------------------EXPLOIT----------------------"
	print "----------------------EXPLOIT----------------------"
	print "----------------------EXPLOIT----------------------"
	print "----------------------EXPLOIT----------------------"
	print exploit.exploit(ip, port, flag_id)

	print "----------------------xx----------------------"
	print "----------------------xx----------------------"


	time.sleep(2)
	
        print "----------------------BENIGN----------------------"
        print "----------------------BENIGN----------------------"
        print "----------------------BENIGN----------------------"
        print "----------------------BENIGN----------------------"
        print "----------------------BENIGN----------------------"
        print benign.benign(ip, port)

        print "----------------------xx----------------------"
        print "----------------------xx----------------------"


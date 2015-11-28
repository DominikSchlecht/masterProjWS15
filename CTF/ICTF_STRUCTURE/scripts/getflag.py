import subprocess
import socket
import sys
import time

def execute_shell(command, error=''):
    return subprocess.Popen(command, shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)

def get_flag(ip, port, flag_id, token):
    password = token
    

    password_splitted = password.split("-.-")
    fzn = password_splitted[0]
    bayWord = password_splitted[1]
	
    if (1==1):
	OKBLUE  = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL    = '\033[91m'
	ENDC    = '\033[0m'

	keys    = []
	encr    = []

	BUFFER_SIZE = 2048
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))

	data = ""
	loop = True
	while loop:
	    tmp = s.recv(BUFFER_SIZE)
	    if tmp.find("Fahrgsteinumma ei:") != -1: 
	        loop = False
	    data += tmp

	s.send(fzn+"\n")
	data = ""
	loop = True
	while loop:
	    tmp = s.recv(BUFFER_SIZE)
    	    if tmp.find("Dei Emissionwert der ist ned so guad schaust ma her:") != -1: 
	        loop = False
	data += tmp
	enc_flag = data.splitlines()[1]

	#------------------------------------------------------------------------------#

	s.send("I ko koa bayrisch\n")
	data = s.recv(BUFFER_SIZE)
	s.send(bayWord+"\n")
	data = ""
	loop = True
	while loop:
    	    tmp = s.recv(BUFFER_SIZE)
	    if tmp.find("deutsch.") != -1: 
                loop = False
        data += tmp
	aes_key = data[data.find('bedeutet')+9:data.find('in deutsch')-1] + '\n'

	#entries = data.splitlines()[1].split("ASDASD")[1].split("32343234")
	#entries.remove(entries[0])


	s.send("exit\n")
	data = s.recv(BUFFER_SIZE)
        s.send("decrypt\n")
        data = s.recv(BUFFER_SIZE)
        s.send(enc_flag + " " + aes_key + "\n")
        data = s.recv(BUFFER_SIZE)
	flag = data.splitlines()[0]

	
        return { 'FLAG': flag }
	s.close()
	sys.exit()


import subprocess
import socket
import sys
import time

def execute_shell(command, error=''):
    return subprocess.Popen(command, shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)

def get_flag(ip, port, flag_id, token):
    note_id = flag_id
    password = token
    print note_id
    print password

    password_splitted = password.split("-.-")
    print password_splitted
    fzn = password_splitted[0]
    print "hier is die fzn" + fzn
    bayWord = password_splitted[1]
    print bayWord
	
    if (1==1):
	OKBLUE  = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL    = '\033[91m'
	ENDC    = '\033[0m'

	ip      = sys.argv[1]
	port    = int(sys.argv[2])
	flagID  = sys.argv[3]
	flagID1 = flagID[:6]
	flagID2 = flagID[6:]

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
	        print "yyeah"
	    data += tmp

	print OKBLUE + "[*] Trying to get flag part 1" + ENDC
	s.send(fzn+"\n")
	print fzn
	data = ""
	loop = True
	while loop:
	    print "hey"
	    tmp = s.recv(BUFFER_SIZE)
	    print "tmp2222: " + tmp + "!!!!!!!!!"
	    print "hooo"
    	    if tmp.find("Dei Emissionwert der ist ned so guad schaust ma her:") != -1: 
	        loop = False
		print "bla"
	data += tmp
	print "blaaa"
	print "data: " + data
	print "data22: " + data.splitlines()[1]
	enc_flag = data.splitlines()[1]
	print "enc_flag: " + enc_flag	

#	for line in data.splitlines():
#		print "line: " + line
#   	    if line.startswith(flagID1):
#        	keys.append(line.split(";")[1])
#	print OKGREEN + "[+] Found " + str(len(keys)) + " possible parts" + ENDC
	#------------------------------------------------------------------------------#
	print OKBLUE + "[*] Trying to get flag part 2" + ENDC
	s.send("I ko koa bayrisch\n")
	print "aaa"
	data = s.recv(BUFFER_SIZE)
	print "bbb"
#	data += s.recv(BUFFER_SIZE)
	print "ccc"
	s.send(bayWord+"\n")
	print "xxx"	
	data = ""
	loop = True
	while loop:
	    print "yyy"
    	    tmp = s.recv(BUFFER_SIZE)
	    if tmp.find("deutsch.") != -1: 
                loop = False
        data += tmp
	print "rrrr"
	print "data: " + data
	aes_key = data[data.find('bedeutet')+9:data.find('in deutsch')-1] + '\n'

	#entries = data.splitlines()[1].split("ASDASD")[1].split("32343234")
	#entries.remove(entries[0])

#	chunks, chunk_size = len(entries[0]), 2#len(entries[0])//4
#	tmp = []
#
#	for ent in entries:
#	    tmp2 = [ ent[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
#	    tmp.append(tmp2)
#
#	lines = []
#	for elem in tmp:
 #   	tmp2 = ""
#	    for c in elem:
  #  	    try:
 #       	    tmp2 = chr(int(c, 16)) + tmp2
#	        except ValueError:
#	            pass
#	    lines.append(tmp2)
#	
#	for line in lines:
#	    if line.startswith(flagID2):
#    	    encr.append(line.split(";")[1][:-1])
#
#	print OKGREEN + "[+] Found " + str(len(encr)) + " possible parts" + ENDC
#
#	print(keys)
#	print(encr)

	s.send("exit\n")
	print "sss"
	data = s.recv(BUFFER_SIZE)
	print "s2"
#	for key in keys:
#	    for en in encr:
        s.send("decrypt\n")
	print "s3"
        data = s.recv(BUFFER_SIZE)
	print "s4"
#        data = s.recv(BUFFER_SIZE)
	print "s5"
	print "enc_flag to send: " + enc_flag
	print "aes_key to send: " + aes_key
        s.send(enc_flag + " " + aes_key + "\n")
        data = s.recv(BUFFER_SIZE)
	flag = data.splitlines()[0]
	print "flag: " + flag
#	for line in data.splitlines():
#		print "line: " + line

        if data.startswith("gcry_cipher_decrypt failed:"):
            print FAIL + "[-] Found false flag"+ data + ENDC
        else:
            print OKGREEN + "[+] Possible Flag: " + data + ENDC
	
        return { 'FLAG': flag }
	s.close()
	sys.exit()



if __name__ == "__main__":
    print get_flag(sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4])


import socket
import sys
import time
import pexpect
import pexpect.fdpexpect

def get_flag(ip, port, flag_id, token):
    # We read that note, knowing the password (in other words, we're benign traffic)
    # Whatever the patch, this must still work!
    note_id = flag_id
    password = token
    print note_id
    print password

    password_splitted = password.split("-.-")
    print password_splitted
    fzn = password_splitted[0]
    print fzn
    bayWord = password_splitted[1]
    print bayWord

    try:
#        s = socket.socket()
#        s.connect((ip,port))
        conn = socket.create_connection((ip,port))
        c = pexpect.fdpexpect.fdspawn(conn.fileno())


        # get encrypted flag
#        time.sleep(1)
 #       data = s.recv(4096)  # free
	print "1"
	print "2"
#	c.expect(".*")
	c.sendline(fzn)
#	c.expect(".*")
#	print c.after	
	print "3"
#        s.send(fzn)
        print "fzn sent"
	c.expect(".*")
	print "4"
#        data = s.recv(4096)
	data = c.readline()
	print data
	print "4"
	data = c.before
	print data
	print "4"
#        print "data: " + data
        print "---"
        encrypted_flag = data.splitlines()[1]
        print "encrypted_flag: " + encrypted_flag

        # get aes key
#        s.send("I ko koa bayrisch")
	c.sendline("I ko koa bayrisch")
#        data = s.recv(4096) # free
#        data = s.recv(4096) # free
        print "data: " + data
#        s.send(bayWord)
	c.sendline(bayWord)
#        data = s.recv(4096)
        print "data: " + data
#        aes_key = data.splitlines()[1]
        print "aes_key: " + aes_key
#        aes_key = aes_key[aes_key.find('bedeutet')+9:aes_key.find('in deutsch')-1] + '\n'
        print "aes_key: " + aes_key
        print "----"

#        data = s.recv(4096)
	data = c.readlines()
        # decrypt flag with aes key
#        s.send("exit")
	c.sendline("exit")
        print "normal mode"
#        s.send("decrypt")
	c.sendline("decrypt")
#        data = s.recv(4096)  # free
	data = c.readlines()
#        s.send(""{} '{}'".format(encrypted_flag, aes_key))
	c.sendline("{} '{}'".format(encrypted_flag, aes_key))
#        data = s.recv(4096)
#        data = s.recv(4096)
	data =	c.readlines()
        decrypted_flag = data
        print decrypted_flag

    except Exception as e:
      error = 42
      error_msg = str(e)
      print "exception!"
      print e

    print "b4 close"
    sys.stdin.flush()
    sys.stdout.flush()
    s.close()

    print "b4 ret"
    return { 'FLAG': decrypted_flag }


if __name__ == "__main__":
    print get_flag(sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4])

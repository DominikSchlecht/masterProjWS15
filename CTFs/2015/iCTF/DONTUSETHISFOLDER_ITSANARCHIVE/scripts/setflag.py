import random
import string
import socket
import sys
import pexpect
import pexpect.fdpexpect
import time

# To create random strings
POSSIBILITIES = string.ascii_uppercase + string.digits + string.ascii_lowercase

def set_flag(ip, port, flag):
    # We create a new note with the flag as content
#    note_id = random.randint(0,4294967295) # Well, hopefully should not collide
#    password = ''.join(random.choice(POSSIBILITIES) for x in range(20))
    note_id = "FZN1BAYW"    # TODO GENERATE FLAG
    password = "FZN12345-.-BAYWORD"
    content = flag

    try:
        s = socket.socket()
        s.connect((ip,port))

     #   c.expect("1")
    #    c.expect("Want to \(R\)ead or \(W\)rite a note?") # Note: these are RegExps!
        print "s.sendline(\"setflag\")"
        s.send("setflag")
        time.sleep(2)
    #    c.expect("2")
    #    c.expect("The note_id is an number. No extra whitespace!")
        print "client: " + note_id + " " + password + " " + content
        print "client: " + "{} {} {}".format(note_id, password, content)
        #c.send("a" + " b-.-c" + " d")
        a  = "{} {} {}".format(note_id, password, content)
        #c.sendline("{} {} {}".format(note_id, password, content))
        s.send(a)
        print "after send"

    except Exception as e:
      error = 42
      error_msg = str(e)
#    c.expect("Your note is safe with us! Bye!")
    #c.close()
    s.close()
    #if ip: conn.close()

    return {
            'FLAG_ID': note_id, # Unique id for each flag
            'TOKEN': password,  # benign (get_flag) will know this, exploits will not
            }


if __name__ == "__main__":
    print set_flag("127.0.0.1", 1337, "FLG_just_testing")

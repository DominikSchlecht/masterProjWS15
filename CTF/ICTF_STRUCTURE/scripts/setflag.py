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
import rstr.__init__ 


# To create random strings
POSSIBILITIES = string.ascii_uppercase + string.digits + string.ascii_lowercase

def set_flag(ip, port, flag):
    # We create a new note with the flag as content
#    note_id = random.randint(0,4294967295) # Well, hopefully should not collide
#    password = ''.join(random.choice(POSSIBILITIES) for x in range(20))

    fzn = generateRandomFZN()
    print "fzn: " + str(fzn)

    bayword = generateRandomBayWord()
    print "bayword: " + str(bayword)

    #note_id = "FZN1BAYW"
    note_id = fzn[:6] + bayword[:4]
    print "note_id: " + str(note_id)
    #password = "FZN12345-.-BAYWORD"
    password = fzn + "-.-" + bayword
    print "password: " + str(password)


    content = flag


    try:
#        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#        s.connect((ip,port))

	conn = socket.create_connection((ip,port))
	c = pexpect.fdpexpect.fdspawn(conn.fileno())
	
	print "000"
	print c.expect(".*")
	print "001"
	print c.expect(".*")
	print "1"
	print c.expect("Ey du Gradler gib a moi dei Fahrgsteinumma ei:")
	print "2"
#	while c.expect(".*") != "E":
#		xvh = 1
#	c.expect("dei Fahrgsteinumma ei:")
	print c.sendline("addfzn")
	print "00010" 
#	c.expect("Ey du Gradler gib a moi a naie Fahrgsteinumma ei ond an Abgaswert ei (Fahrgsteinumma Abgaswert):")
#	c.expect("Ey du Gradler gib a moi a naie Fahrgsteinumma ei ond an Abgaswert ei (Fahrgsteinumma Abgaswert):.*")
	c.expect(".*")
        a  = "{} {} {}".format(note_id, password, content)
	print "sending: " + str(a)
	print c.sendline(str(a)+"\n")
	print "00020"
	print c.expect(".*")
#	c.expect("Ey du Gradler gib a moi a naie Fahrgsteinumma ei ond an Abgaswert ei (Fahrgsteinumma Abgaswert):")
	print "bla"
	c.sendline("exit")
	print "blubb"
	print c.expect(".*")
#	c.expect("Ey du Gradler gib a moi dei Fahrgsteinumma ei:")
	print "bliblablubb"
	c.sendline("exit")

     #   c.expect("1")
    #    c.expect("Want to \(R\)ead or \(W\)rite a note?") # Note: these are RegExps!
 #       print "s.sendline(\"addfzn\")"
  #      s.send("addfzn")
   #     time.sleep(2)
    #    c.expect("2")
    #    c.expect("The note_id is an number. No extra whitespace!")
      #  print "client: " + note_id + " " + password + " " + content
    #    print "client: " + "{} {} {}".format(note_id, password, content)
     #   #c.send("a" + " b-.-c" + " d")
      #  a  = "{} {} {}".format(note_id, password, content)
      #  #c.sendline("{} {} {}".format(note_id, password, content))
     #   s.send(a)
     #   print "after send"
     #   data = s.recv(4096)
#	print data
 #       s.send("exit")

    except Exception as e:
        error = 42
        error_msg = str(e)
        print (error_msg)
#    c.expect("Your note is safe with us! Bye!")
    #c.close()
    sys.stdin.flush()
    sys.stdout.flush()
#    s.close()
    c.close()
    #if ip: conn.close()

    return {
            'FLAG_ID': note_id, # Unique id for each flag
            'TOKEN': password,  # benign (get_flag) will know this, exploits will not
            }

def generateRandomFZN():
    fahrzeugtypenstring_array = [ '111', '113', '115', '117', '135', '141', '143', '147', '148', '151', '152', '154', '155', '161', '163', '165', '167', '171', '173', '181', '183', '191', '192', '193', '194', '1AE', '1C1', '1E7', '1G1', '1G2', '1G4', '1H1', '1H2', '1H5', '1J1', '1J2', '1J5', '1J6', '1K1', '1T1', '1V7', '1Y7', '211', '215', '21A', '21B', '21C', '21D', '21E', '21F', '21G', '21H', '21K', '221', '225', '231', '235', '241', '245', '246', '247', '248', '251', '252', '253', '254', '255', '256', '261', '265', '271', '281', '282', '283', '284', '285', '286', '291', '292', '293', '294', '295', '2DA', '2DB', '2DC', '2DD', '2DE', '2DF', '2DG', '2DH', '2DK', '2DL', '2DM', '2KA', '2KB', '2VC', '2VF', '2VH', '3A2', '3A5', '3B2', '3B3', '3B5', '3B6', '3D2', '3G2', '3G5', '3D8', '311', '312', '313', '315', '317', '321', '321', '323', '323', '327', '331', '331', '343', '345', '361', '363', '365', '367', '411', '415', '421', '425', '461', '465', '481', '5Z5', '509', '531', '533', '6N1', '6N2', '6V2', '6V5', '6X1', '70A', '70B', '70C', '70E', '70H', '70J', '70K', '70L', '70M', '7AE', '7AG', '7AX', '7DA', '7DB', '7DC', '7DE', '7DH', '7DJ', '7DK', '7DL', '7DM', '7HA', '7HB', '7HC', '7HH', '7HJ', '7HM', '7JD', '7JE', '7JL', '7LA', '7M6', '7M8', '7M9', '801', '802', '803', '861', '863', '865', '867', '871', '873', '9C1', '9G1', '9K9' ]
    pattern =  "^(WVW|WV2|1VW|3VW|9BW|AAV)(ZZZ)?(" + random.choice(fahrzeugtypenstring_array) + ")([ABCDEFGHJKLMNPRSTVWXY]|[0-9])([ABCDEFGHJKLMNPRSTUVWXYZ]|[0-9])[0-9]{6}$"
    tmp = rstr.xeger(pattern)

    return tmp

def generateRandomBayWord():
    return ''.join(random.choice(string.lowercase) for i in range(random.randint(6,15)))


if __name__ == "__main__":
    print set_flag(sys.argv[1], int(sys.argv[2]), sys.argv[3])

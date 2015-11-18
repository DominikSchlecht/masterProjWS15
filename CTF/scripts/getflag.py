import socket
import sys
import pexpect
import pexpect.fdpexpect

def get_flag(ip, port, flag_id, token):
    # We read that note, knowing the password (in other words, we're benign traffic)
    # Whatever the patch, this must still work!
    note_id = flag_id
    password = token
    content = ""
    print note_id
    print password

    password_splitted = password.split("-.-")
    print password_splitted
    fzn = password_splitted[0]
    print fzn
    bayWord = password_splitted[1]
    print bayWord

    try:
        s = socket.socket()
        s.connect((ip,port))

        data = s.recv(4096)
        s.send(fzn)
        print "fzn sent"
        data = s.recv(4096)
        print data
        #c.expect("P  lease type: note_id password")
        s.send("{} {}".format(note_id, password))

        #c.expect("Note content: ")
        #content = s.readline().strip()
        data = s.recv(4096)
        print data

    except Exception as e:
      error = 42
      error_msg = str(e)
      print "exception!"
      print e

    print "b4 ret"
    s.send("b4 close")
    s.close()

    print "b4 ret"
    return { 'FLAG': content }


if __name__ == "__main__":
    print get_flag("127.0.0.1", 1337, sys.argv[3], sys.argv[4])

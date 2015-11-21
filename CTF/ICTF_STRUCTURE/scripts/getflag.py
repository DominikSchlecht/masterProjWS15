import socket
import sys
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
        s = socket.socket()
        s.connect((ip,port))

        # get encrypted flag
        data = s.recv(4096)  # free
        s.send(fzn)
        print "fzn sent"
        data = s.recv(4096)
        print data
        encrypted_flag = data

        # get aes key
        s.send("I ko koa Bayrisch")
        data = s.recv(4096) # free
        s.send(bayWord)
        data = s.recv(4096)
        aes_key = data

        # decrypt flag with aes key
        s.send("exit")
        s.send("getflag")
        data = s.recv(4096)  # free
        s.send("{} {}".format(fzn, bayWord))
        data = s.recv(4096)
        decrypted_flag = data
        print decrypted_flag

    except Exception as e:
      error = 42
      error_msg = str(e)
      print "exception!"
      print e

    print "b4 close"
    s.send("b4 close")
    s.close()

    print "b4 ret"
    return { 'FLAG': decrypted_flag }


if __name__ == "__main__":
    print get_flag("127.0.0.1", 1337, sys.argv[3], sys.argv[4])

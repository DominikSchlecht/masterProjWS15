import subprocess
import socket
import sys
import time

def execute_shell(command, error=''):
    return subprocess.Popen(command, shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)

def recv_until(s, text):
    BUFFER_SIZE = 2048
    data = ""
    loop = True
    while loop:
        tmp = s.recv(BUFFER_SIZE)
        if tmp.find(text) != -1: loop = False
        data += tmp
    return data


def get_flag(ip, port, flag_id, token):
    password = token

    password_splitted = password.split("-.-")
    fzn = password_splitted[0]
    bayWord = password_splitted[1]

#    return password + " " + fzn + " " + bayWord        # Internal error! Contact the admins!
#    retu = password + "_" + fzn + "_" + bayWord
#    return { 'FLAG': retu }    # ERROR , weil falsche Flag...Werte passen aber



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
    data = recv_until(s, "Fahrgsteinumma ei:\n")
    s.send(fzn+"\n")
    data = recv_until(s, "\n\n")
    enc_flag = data.splitlines()[1]
#       retu = data.splitlines()
#       return { 'FLAG': retu } # flag: [u\'Dei Emissionwert der ist ned so guad schaust ma her: \', u\'\'].'

    print OKGREEN + "[+] Found flag part 1: " + enc_flag + ENDC
    #------------------------------------------------------------------------------#

    s.send("I ko koa bayrisch\n")
    data = recv_until(s, "sie wissen?\n")
    s.send(bayWord+"\n")
    data = recv_until(s, "sie wissen?\n")
    aes_key = data[data.find('bedeutet')+9:data.find('in deutsch')-1] + '\n'
    print OKGREEN + "[+] Found flag part 2: " + aes_key + ENDC

        #entries = data.splitlines()[1].split("ASDASD")[1].split("32343234")
        #entries.remove(entries[0])


    s.send("exit\n")
    data = recv_until(s, "Fahrgsteinumma ei:\n")
    s.send("decrypt\n")
    data = recv_until(s, "entschluesseln?\n")
    s.send(enc_flag + " " + aes_key + "\n")
    data = recv_until(s, "entschluesseln?\n")
    flag = data.splitlines()[0]

    if data.startswith("gcry_cipher_decrypt failed:"):
        print FAIL + "[-] Found false flag"+ data.split("\n")[0] + ENDC
    else:
        print OKGREEN + "[+] Possible Flag: " + data.split("\n")[0] + ENDC

    s.close()
    return { 'FLAG': flag }

if __name__ == "__main__":
    print get_flag(sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4])

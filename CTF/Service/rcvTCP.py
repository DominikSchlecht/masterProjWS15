import sys, socket
import re
import csv
import subprocess

def execute_shell(command, error=''):
    return subprocess.Popen(command, shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
    #print 'verb: ' + str(arguments.verbose)
    #if arguments.verbose: print 'command: ' + command

Fahrzeugtypenstring = ""
f = open("info/Fahrzeugtypen.csv", 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        Fahrzeugtypenstring += str(row)[2:5] + "|"
finally:
    f.close()
Fahrzeugtypenstring = Fahrzeugtypenstring[:-1]

OKBLUE  = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL    = '\033[91m'
ENDC    = '\033[0m'

TCP_IP = '127.0.0.1'
#TCP_IP = '88.198.205.243'
TCP_PORT = 1337
BUFFER_SIZE = 512

pattern =  "^(WVW|WV2|1VW|3VW|9BW|AAV)(ZZZ)?(" + Fahrzeugtypenstring + ")([ABCDEFGHJKLMNPRSTVWXY]|[0-9])([ABCDEFGHJKLMNPRSTUVWXYZ]|[0-9])[0-9]{6}$"
counter = 1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(5)
clients = []

try:
    while 1:
        conn, addr = s.accept()
        if not str(addr[0]) in clients:
            clients.append(str(addr[0]))
            print(OKGREEN + "[+] Client %s connected" % (str(addr[0])) + ENDC)
        #print(OKBLUE    + "[*] Starting keydump..."                     + ENDC)
        tmp = ""

        conn.send("Ey du Gradler gib a moi dei Fahrgsteinumma ei: \n")

        while 1:
            try:
                data = conn.recv(BUFFER_SIZE) # This returns immediately with no data, when client connection is run from script and doesn't send() anything, just connects.
            except ConnectionResetError as e:
                print(FAIL + "\n[-] Client %s disconnected hard" % (str(addr[0])) + ENDC)
                break
            if not data:
                #print(WARNING + "\n[-] Client %s disconnected nicely" % (str(addr[0])) + ENDC)
                break
            data = str(data)
            sys.stdout.flush()

            if(re.match(pattern, data)):
                r = execute_shell("./commandInjection " + data)
                conn.send('Dei Emissionwert der ist ne so guad schaust ma her: \n' + r.stdout.read() + '\n')
            else:
                conn.send('Des is fei koa gscheide Numma du de** du damischer...\n')

        sys.stdout.flush()
        conn.close()
except KeyboardInterrupt as e:
    s.close()
    print(OKBLUE + "\n[-] Shutting down.." + ENDC)
except Exception as e:
    s.close()
    print(FAIL + "[X] Unhandelt Error:")
    print(e)

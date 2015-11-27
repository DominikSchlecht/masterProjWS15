import sys, socket
import csv
import subprocess
import thread

def execute_shell(command, error=''):
    return subprocess.Popen(command, shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)

Fahrzeugtypenstring = ""
f = open("../rw/info/Fahrzeugtypen.csv", 'rt')
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

BUFFER_SIZE = 4096

pattern =  "^(WVW|WV2|1VW|3VW|9BW|AAV)(ZZZ)?(" + Fahrzeugtypenstring + ")([ABCDEFGHJKLMNPRSTVWXY]|[0-9])([ABCDEFGHJKLMNPRSTUVWXYZ]|[0-9])[0-9]{6}$"
clients = []

def runService(conn, addr):
    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.bind((TCP_IP, TCP_PORT))
    #s.listen(5)

        try:
            #while 1:
                #conn, addr = s.accept()
                if not str(addr[0]) in clients:
                    clients.append(str(addr[0]))
                    print(OKGREEN + "[+] Client %s connected" % (str(addr[0])) + ENDC)
                #print(OKBLUE    + "[*] Starting keydump..."                     + ENDC)
                tmp = ""
                conn.send("\n********************************************************\n")
                conn.send("**************** Welcome to Folkswagen *****************\n")
                conn.send("********************************************************\n")
                conn.send("\n********************************************************\n")
                conn.send("*                                                      *\n")
                conn.send("* FFFFFFFFFFFFFFFFF  W               W               W *\n")
                conn.send("* FF                  W             W W             W  *\n")
                conn.send("* FF                   W           W   W           W   *\n")
                conn.send("* FF                    W         W     W         W    *\n")
                conn.send("* FFFFFFFFFFF            W       W       W       W     *\n")
                conn.send("* FF                      W     W         W     W      *\n")
                conn.send("* FF                       W   W           W   W       *\n")
                conn.send("* FF                        W W             W W        *\n")
                conn.send("* FF                         W               W         *\n")
                conn.send("*                                                      *\n")
                conn.send("********************************************************\n\n\n")


                translator = False
                addfzn = False
                decrypt = False

                numberplz = "Ey du Gradler gib a moi dei Fahrgsteinumma ei:\n"
                wordplz = "Welches bayrische Wort moechten sie wissen?\n"
                wrongnum = "\nDes is fei koa gscheide Numma du de** du dammischer...\n\nSollten sie aus dem Ausland kommen und kein Bayrisch\nsprechen koennen sie auch unseren Uebersetzer nutzen!\nGeben sie dafuer folgendes ein: \n\"I ko koa bayrisch\"\n"
                cake = "The cake is a lie!\n"
                quittrans = "Der Uebersetzer laesst sich mit exit oder quit beenden.\n"
                emission = "Dei Emissionwert der ist ned so guad schaust ma her: \n"
                newFZN = "Ey du Gradler gib a moi a naie Fahrgsteinumma ei ond an Abgaswert ei (Fahrgsteinumma Abgaswert):\n"
                decryptSth = "Mogst was entschluesseln?\n"

                conn.send(numberplz)

                while 1:
                    data = conn.recv(BUFFER_SIZE)
                    print "data: " + data
                    if not data:
                        print((WARNING + "\n[-] Client %s disconnected nicely" % (str(addr[0])) + ENDC))
                        break
                    else:
                        data = (str(data)).strip()
                        sys.stdout.flush()
                        if translator:
                            if(data == "quit" or data == "exit"):
                                translator = False
                                conn.send(numberplz)
                            else:
                                if not "\"" in data:
                                    r = execute_shell("../ro/uebersetzer \"" + data + "\"")
                                    tmp = r.stdout.read()
                                    conn.send("\nDas Wort "+ tmp + " in deutsch.\n");
                                conn.send(wordplz)
                        elif addfzn:
                            if(data == "quit" or data == "exit"):
                                addfzn = False
                                conn.send(numberplz)
                            else:
                                if not "\"" in data:
                                    r = execute_shell("../ro/setflag " + data)
                                    tmp = r.stdout.read()
                                    conn.send(tmp)
                                    print "after execute_shell()"
                                conn.send(newFZN)
                        elif decrypt:
                            if(data == "quit" or data == "exit"):
                                decrypt = False
                                conn.send(numberplz)
                            else:
                                if not "\"" in data:
                                    r = execute_shell("../ro/setflag -h " + data) # TODO
                                    tmp = r.stdout.read()
                                    conn.send(tmp)
                                    print "after execute_shell()"
                                conn.send("\n" + decryptSth);
                        elif(data == "quit" or data == "exit"):
                            print((WARNING + "\n[-] Client %s disconnected nicely" % (str(addr[0])) + ENDC))
                            break
                        elif(data == "help"):
                            conn.send(cake)
                        elif(data == "I ko koa bayrisch"):
                            translator = True
                            conn.send(quittrans)
                            conn.send(wordplz)
                        elif(data == "addfzn"):
                            conn.send(newFZN)
                            addfzn = True
                        elif(data == "decrypt"):
                            conn.send(decryptSth)
                            decrypt = True
                        else:
                        #elif(re.match(pattern, data)):
                            if not "\"" in data:
                                r = execute_shell("../ro/abgaswerte \"" + data + "\"")
                                tmp = r.stdout.read()
                            if tmp != "Na\n":
                                print(tmp)
                                conn.send(emission + tmp + "\n")
                            else:
                                conn.send(wrongnum)
                sys.stdout.flush()
                conn.close()
        except KeyboardInterrupt as e:
            conn.close()
            print(OKBLUE + "\n[-] Shutting down.." + ENDC)
        except Exception as e:
            conn.close()
            print(FAIL + "[X] Unhandelt Error:")
            print(str(e) + ENDC)

if __name__ == "__main__":

    if (len(sys.argv) < 2):
        port = 1337
    else:
        port = (int)(sys.argv[1])
    host = 'localhost'

    addr = (host, port)

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serversocket.bind(addr)

    serversocket.listen(2)

    while 1:
        print OKBLUE + "[*] Server is listening for connections\n" + ENDC

        clientsocket, clientaddr = serversocket.accept()
        thread.start_new_thread(runService, (clientsocket, clientaddr))
    serversocket.close()

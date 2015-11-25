import socket
import sys
import time
import random
import string

test = False


def benign(ip, port):
    if test:
        print("Hi!")

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        time.sleep(0.1)
        if test:
            print ("conection open")
        data = s.recv(4096)
        if test:
            print(data)

        output = "test"
        if test:
            print(output)
            raw_input()
        s.send(output)
        time.sleep(0.1)
        data = s.recv(4096)
        if test:
            print(data)

        output = "help"
        if test:
            print(output)
            raw_input()
        s.send(output)
        time.sleep(0.1)
        data = s.recv(4096)
        if test:
            print(data)
            #
        output = "I ko koa bayrisch"
        if test:
            print(output)
            raw_input()
        s.send(output)
        time.sleep(0.1)
        data = s.recv(4096)
        if test:
            print(data)

        output = "Gradler"
        if test:
            print(output)
            raw_input()
        s.send(output)
        time.sleep(0.1)
        data = s.recv(4096)
        if test:
            print(data)

        output = "quit"
        if test:
            print(output)
            raw_input()
        s.send(output)
        time.sleep(0.1)
        data = s.recv(4096)
        if test:
            print(data)

        output = "AAVZZZ48294857202"
        if test:
            print(output)
            raw_input()
        s.send(output)
        time.sleep(0.1)
        data = s.recv(4096)
        if test:
            print(data)

        flaggenr = random.randint(10000000, 99999999)
        output = "setflag=\"flg" + str(flaggenr) + "\""
        if test:
            print(output)
            raw_input()
        s.send(output)
        time.sleep(0.1)
        data = s.recv(4096)
        if test:
            print(data)

        output = "WVWZZZ161NZ331205"
        if test:
            print(output)
            raw_input()
        s.send(output)
        time.sleep(0.1)
        data = s.recv(4096)
        if test:
            print(data)

        output = "addfzn"
        if test:
            print(output)
            raw_input()
        s.send(output)
        time.sleep(0.1)
        data = s.recv(4096)
        if test:
            print(data)

        output = "quit"
        if test:
            print(output)
            raw_input()
        s.send(output)
        time.sleep(0.1)
        data = s.recv(4096)
        if test:
            print(data)

        output = "decrypt"
        if test:
            print(output)
            raw_input()
        s.send(output)
        time.sleep(0.1)
        data = s.recv(4096)
        if test:
            print(data)

        output = "quit"
        if test:
            print(output)
            raw_input()
        s.send(output)
        time.sleep(0.1)
        data = s.recv(4096)
        if test:
            print(data)

        flaggenID = str(random.randint(100000, 999999)) + ''.join(random.choice(string.uppercase) for i in range(4))
        output = "getflag=\"" + flaggenID + "\""
        if test:
            print(output)
            raw_input()
        s.send(output)
        time.sleep(0.1)
        data = s.recv(4096)
        if test:
            print(data)

        output = "WVWZZZ1675E166087"
        if test:
            print(output)
            raw_input()
        s.send(output)
        time.sleep(0.1)
        data = s.recv(4096)
        if test:
            print(data)

        output = "AAVZZZ86729856822"
        if test:
            print(output)
            raw_input()
        s.send(output)
        time.sleep(0.1)
        data = s.recv(4096)
        if test:
            print(data)

        output = "test"
        if test:
            print(output)
            raw_input()
        s.send(output)
        time.sleep(0.1)
        data = s.recv(4096)
        if test:
            print(data)
        sys.stdout.flush()
        s.close()
    except Exception as e:
        print ("Exception!")
        print (e)
        sys.stdin.flush()
        sys.stdout.flush()
        s.close()
if sys.argv[1].strip() == "test":
    test = True
    benign('127.0.0.1', 1337)
else:
    benign(sys.argv[1], int(sys.argv[2]))
print ("done")
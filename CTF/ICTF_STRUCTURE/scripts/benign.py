import socket
import sys
import time

test = True


def benign(ip, port):
    if test:
        print("Hi!")

    try:
        s = socket.socket()
        s.connect((ip, port))
        time.sleep(1)
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
        data = s.recv(4096)
        if test:
            print(data)
        output = "help"
        if test:
            print(output)
            raw_input()
        s.send(output)
        data = s.recv(4096)
        if test:
            print(data)
        output = "I ko koa Bayrisch"
        if test:
            print(output)
            raw_input()
        s.send(output)
        data = s.recv(4096)
        if test:
            print(data)
        output = "Gradler"
        if test:
            print(output)
            raw_input()
        s.send(output)
        data = s.recv(4096)
        if test:
            print(data)
        output = "quit"
        if test:
            print(output)
            raw_input()
        s.send(output)
        data = s.recv(4096)
        if test:
            print(data)
        output = "setflag"
        if test:
            print(output)
            raw_input()
        s.send(output)
        data = s.recv(4096)
        if test:
            print(data)
        output = "quit"
        if test:
            print(output)
            raw_input()
        s.send(output)
        data = s.recv(4096)
        if test:
            print(data)
        output = "WVWZZZ161NZ331205"
        if test:
            print(output)
            raw_input()
        s.send(output)
        data = s.recv(4096)
        if test:
            print(data)
        output = "WVWZZZ1675E166087"
        if test:
            print(output)
            raw_input()
        s.send(output)
        data = s.recv(4096)
        if test:
            print(data)
        output = "AAVZZZ86729856822"
        if test:
            print(output)
            raw_input()
        s.send(output)
        data = s.recv(4096)
        if test:
            print(data)
        output = "test"
        if test:
            print(output)
            raw_input()
        s.send(output)
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
if test:
    benign('127.0.0.1', 1337)
else:
    benign(sys.argv[1], int(sys.argv[2]))
print ("done")
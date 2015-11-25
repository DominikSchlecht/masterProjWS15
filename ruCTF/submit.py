import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("10.10.10.3", "31337"))

f = open("blubb", 'r')

for line in f:
    s.send(line)
f.close()

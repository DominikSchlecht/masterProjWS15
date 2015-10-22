#!/bin/env python
import argparse
from string import Template
from time import sleep
import subprocess
import threading
from datetime import datetime

# Init the parser
parser = argparse.ArgumentParser(description='''
Port recorder\n

..using tcpdump.

v. 1.0 2015-10-22 Dominik Schlecht (dominik.schlecht@hotmail.de)
''', formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-i', metavar='INTF',
                   help='Interface to capture on.', required=True)
parser.add_argument('-p', metavar='Port', type=int, nargs='+',
                   help='The ports to dump.', required=True)
parser.add_argument('-c', metavar='INT', type=int, default=1000,
                   help='Number of packets to capture before beginning a new file.')
parser.add_argument('-d', metavar='FOLDER',
                   help='Folder to write the dumps to.', default="/tmp/")
args = parser.parse_args()

OKBLUE  = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL    = '\033[91m'
ENDC    = '\033[0m'

# Fix folders
if args.d[-1] != "/":
    args.d = args.d + "/"
    print(WARNING + "[#] Don't you know that folders end in '/'? Correcting for you.." + ENDC)

TCPDumpCommand = Template("tcpdump -i $intf port $port -vv -c $count -w " + args.d + "$port/$name.pcap")

# Helper functions
def execute_shell(command, error=''):
    return subprocess.Popen(command, shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
def printDate():
    #return "[" + str(datetime.now().time().hour) + ":" + str(datetime.now().time().minute) + ":" + str(datetime.now().time().second) + "]"
    return "[%02d:%02d:%02d]" % (datetime.now().time().hour, datetime.now().time().minute, datetime.now().time().second)

def prepare_folders():
    # Prepare folders
    for port in args.p:
        r = execute_shell("mkdir " + args.d + str(port))
        print(OKBLUE + "[*]" + printDate() + " Created folder " + args.d + str(port) + ENDC)

# Dump Thread
def dump(portParam):
    print(OKBLUE + "[*]" + printDate() + " Started dump for port " + str(portParam) + ENDC)
    cnt = 0
    r = execute_shell(TCPDumpCommand.substitute(intf=args.i, port=portParam, count=args.c, name=cnt))
    while True:
        while True:
            try:
                r.communicate()[0]
            except ValueError:
                print(OKGREEN + "[*]" + printDate() + " Captured " + str(args.c) + " packets on port "
                    + str(portParam) + " to " + args.d + str(portParam) + "/" + str(cnt) + ".pcap" + "." + ENDC)
                break
            if flag == True:
                sleep(1)
                print(WARNING + "[*]" + printDate() + " Exiting Thread for port " + str(portParam) + ENDC)
                return 0
            sleep(1)
        cnt += 1
        r = execute_shell(TCPDumpCommand.substitute(intf=args.i, port=portParam, count=args.c, name=cnt))

try:
    flag = False
    prepare_folders()

    threads = []
    for port in args.p:
        t = threading.Thread(target=dump, args=(port,))
        threads.append(t)
        t.start()
    while True:
        sleep(10)
except (KeyboardInterrupt, SystemExit):
    flag = True
    print(WARNING + "\n[*]" + printDate() + " Shutting down.." + ENDC)

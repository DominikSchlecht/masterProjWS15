import subprocess
import argparse
from string import Template

# Init the parser
parser = argparse.ArgumentParser(description='''
Minimal WAF\n

..using iptables.

v. 1.0 2015-10-21 Dominik Schlecht (dominik.schlecht@hotmail.de)
''', formatter_class=argparse.RawDescriptionHelpFormatter)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-a', metavar='BadString',
                   help='String to block.')
group.add_argument('-d', metavar='BadString',
                   help='Delete a string.')
group.add_argument('-l', action='store_true', help='List strings.')
args = parser.parse_args()

OKBLUE  = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL    = '\033[91m'
ENDC    = '\033[0m'

# Define iptable strings as Templates for easy substitution
strInputAdd     = Template("iptables -A INPUT -m string --algo bm --string $text -j DROP")
strOutputAdd    = Template("iptables -A OUTPUT -m string --algo bm --string $text -j DROP")
strForwardAdd   = Template("iptables -A FORWARD -m string --algo bm --string $text -j DROP")
strInputDel     = Template("iptables -D INPUT -m string --string $text --algo bm --to 65535 -j DROP")
strOutputDel    = Template("iptables -D OUTPUT -m string --string $text --algo bm --to 65535 -j DROP")
strForwardDel   = Template("iptables -D FORWARD -m string --string $text --algo bm --to 65535 -j DROP")

# Little helper for command execution and interaction
def execute_shell(command, error=''):
    return subprocess.Popen(command, shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
    #print 'verb: ' + str(arguments.verbose)
    #if arguments.verbose: print 'command: ' + command

if args.l:
    r = execute_shell('iptables -L')
    print(r.communicate()[0])
elif args.a:
    r = execute_shell(strInputAdd.substitute(text=args.a))
    r = execute_shell(strOutputAdd.substitute(text=args.a))
    r = execute_shell(strForwardAdd.substitute(text=args.a))
    print(OKBLUE + "[+]" + ENDC + " Sucessfully added " + args.a + " to blocklist.")
elif args.d:
    r = execute_shell(strInputDel.substitute(text=args.d))
    r = execute_shell(strOutputDel.substitute(text=args.d))
    r = execute_shell(strForwardDel.substitute(text=args.d))
    print(OKBLUE + "[+]" + ENDC + " Sucessfully deleted " + args.d + " to blocklist.")

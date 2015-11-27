#!/usr/bin/env python
import os
import sys
import subprocess


OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'


def Folkswagen_emissions():
    tmp = ""
    sys.stdout.write("\n********************************************************\n")
    sys.stdout.write("**************** Welcome to Folkswagen *****************\n")
    sys.stdout.write("********************************************************\n")
    sys.stdout.write("\n********************************************************\n")
    sys.stdout.write("*                                                      *\n")
    sys.stdout.write("* FFFFFFFFFFFFFFFFF  W               W               W *\n")
    sys.stdout.write("* FF                  W             W W             W  *\n")
    sys.stdout.write("* FF                   W           W   W           W   *\n")
    sys.stdout.write("* FF                    W         W     W         W    *\n")
    sys.stdout.write("* FFFFFFFFFFF            W       W       W       W     *\n")
    sys.stdout.write("* FF                      W     W         W     W      *\n")
    sys.stdout.write("* FF                       W   W           W   W       *\n")
    sys.stdout.write("* FF                        W W             W W        *\n")
    sys.stdout.write("* FF                         W               W         *\n")
    sys.stdout.write("*                                                      *\n")
    sys.stdout.write("********************************************************\n\n")

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

    sys.stdout.write(numberplz)
    sys.stdout.flush()

    while 1:
        data = raw_input()
        #print "data: " + data
        if not data:
            #print((WARNING + "\n[-] Client %s disconnected nicely" % (str(addr[0])) + ENDC))
            break
        else:
            data = (str(data)).strip()
            if translator:
                if(data == "quit" or data == "exit"):
                    translator = False
                    sys.stdout.write(numberplz)
                    sys.stdout.flush()
                else:
                    if not "\"" in data:
                        r = execute_shell("../ro/uebersetzer \"" + data + "\"")
                        tmp = r.stdout.read()
                        sys.stdout.write("\nDas Wort "+ tmp + " in deutsch.\n");
                    sys.stdout.write(wordplz)
                    sys.stdout.flush()
            elif addfzn:
                if(data == "quit" or data == "exit"):
                    addfzn = False
                    sys.stdout.write(numberplz)
                    sys.stdout.flush()
                else:
                    if not "\"" in data:
                        r = execute_shell("../ro/setflag " + data)
                        tmp = r.stdout.read()
                        sys.stdout.write(tmp)
                        #print "after execute_shell()"
                    sys.stdout.write(newFZN)
                    sys.stdout.flush()
            elif decrypt:
                if(data == "quit" or data == "exit"):
                    decrypt = False
                    sys.stdout.write(numberplz)
                    sys.stdout.flush()
                else:
                    if not "\"" in data:
                        r = execute_shell("../ro/setflag -h " + data)  # TODO
                        tmp = r.stdout.read()
                        sys.stdout.write(tmp)
                        #print "after execute_shell()"
                    sys.stdout.write("\n" + decryptSth);
                    sys.stdout.flush()
            elif(data == "quit" or data == "exit"):
                #print((WARNING + "\n[-] Client %s disconnected nicely" % (str(addr[0])) + ENDC))
                break
            elif(data == "help"):
                sys.stdout.write(cake)
                sys.stdout.flush()
            elif(data == "I ko koa bayrisch"):
                translator = True
                sys.stdout.write(quittrans)
                sys.stdout.write(wordplz)
                sys.stdout.flush()
            elif(data == "addfzn"):
                sys.stdout.write(newFZN)
                sys.stdout.flush()
                addfzn = True
            elif(data == "decrypt"):
                sys.stdout.write(decryptSth)
                sys.stdout.flush()
                decrypt = True
            else:
            #elif(re.match(pattern, data)):
                if not "\"" in data:
                    r = execute_shell("../ro/abgaswerte \"" + data + "\"")
                    tmp = r.stdout.read()
                if tmp != "Na\n":
                    sys.stdout.write(emission + tmp + "\n")
                else:
                    sys.stdout.write(wrongnum)
                sys.stdout.flush()

def execute_shell(command, error=''):
    return subprocess.Popen(command, shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)

if __name__ == "__main__":
    Folkswagen_emissions()

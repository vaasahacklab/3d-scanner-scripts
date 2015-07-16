#!/usr/bin/python
#Pi3Dscan - listen script
#Written by: Richard Garsthagen - richard@3dmij.nl
#More info: www.pi3dscan.com
#Version 2.0 - November 22nd 2014

import socket
import struct
import fcntl
import subprocess
import sys

MCAST_GRP = '225.1.1.1'
MCAST_PORT = 3179

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

print " "
print "3D Scanner - Open Source listen script"

debug = 1  # Turn debug message on/off

while True:
   data = sock.recv(10240)
   rdata = data[1:]
   rcmd = ord(data[0])
   if debug == 1:
     print "Received cmd: "+ str(rcmd)
     print "Data: " + rdata
   if (rcmd == 1):
     print "shooting"
     cmd = "raspistill " + rdata
     pid = subprocess.call(cmd, shell=True)




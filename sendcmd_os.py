#!/usr/bin/python
#Pi3Dscan - send script
#Written by: Richard Garsthagen - richard@3dmij.nl
#More info: www.pi3dscan.com
#Version 2.0 - November 22nd 2014

import socket
import struct
import fcntl
import json
import subprocess
import sys
import IN


MCAST_GRP = '225.1.1.1'
MCAST_PORT = 3179
print sys.argv

if len(sys.argv) < 3 and sys.argv[1] != '-1':
  print "Please provide raspistill command options. See raspistill command for details"
else:
  options = [sys.argv[1]] # Command 1 = Shoot photo
  for a in range(2, len(sys.argv)):
   options.append(sys.argv[a])
  print "Sending shooting command..."
  SEND = json.dumps(options)
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
  sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
  sock.sendto(SEND, (MCAST_GRP, MCAST_PORT))
  sock.close()




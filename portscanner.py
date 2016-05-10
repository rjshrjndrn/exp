#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  portscanner.py
#  
#  Copyright 2016 rajesh rajendran <rajesh.rajendran@protonmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import socket
import subprocess
import sys
from datetime import datetime

#clear the screen
subprocess.call('clear',shell=True)

#ask for input
remote = raw_input("Enter a remote host to scan: ")
remoteIP = socket.gethostbyname(remote)

#printing some demo banner with info
print "-" * 60
print "please wait, scanning remote host", remoteIP
print "-" *60

#checking the time scanning started
t1=datetime.now()
#range of ports using range function
#and some error handling...incase ;)
try:
	for port in range(1,1025):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteIP, port))
		if result == 0:
			print "Port {} :	open".format(port)
		sock.close()
except KeyboardInterrupt:
	print "\noops.. you pressed Ctrl+C"
	sys.exit()
except socket.gaierror:
	print "hostname couldnot be resolved. Exiting"
	sys.exit()
#checking time again
t2=datetime.now()
#Calculate the difference in time
total=t2-t1
#printing info
print "scanning completed in: ",total



#!/usr/bin/python

import smtplib
fromaddr = 'rajesh@pinch.red'
toaddrs  = 'rajesh@pinch.red'
msg = 'Why,Oh why!'
username = 'rajesh@pinch.red'
password = 'Vitt@la122'
server = smtplib.SMTP('smtpout.asia.secureserver.net:465')

server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

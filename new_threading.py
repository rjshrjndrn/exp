#!/usr/bin/python

import threading
import time

exflag=0

class myThread(threading.thread):
	def _init_(self,threadID,name,counter):
		threading.Thread._init_(self)
		

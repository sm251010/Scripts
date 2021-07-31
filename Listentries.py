#Keepass Manager password expiry script
#Author : Shivam Malhotra
import os
import json
from pykeepass import PyKeePass
from datetime import date
import datetime as dt
import datetime

kp = PyKeePass('mynewncrdb.kdbx', password='qwerty@1234')
group = kp.find_groups(name='ACCOUNTS', first=True)
entrites = group.entries

#print('All entries :: ' + str(entrites))
for entry in entrites:
	print("\n")
	s = (str(entry))
	string = s[s.find("(")+1:s.find(")")]
	kp = PyKeePass('mynewncrdb.kdbx', password='qwerty@1234')
	entry = kp.find_entries(username=string, first=True)
	print(str(entry))

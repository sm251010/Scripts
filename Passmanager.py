#Keepass Manager password expiry script
#Author : Shivam Malhotra
import json
from pykeepass import PyKeePass
import csv
from datetime import date
import datetime as dt
import datetime

kp = PyKeePass('mynewncrdb.kdbx', password='qwerty@1234')
group = kp.find_groups(name='ACCOUNTS', first=True)
entrites = group.entries
#print(str(entrites))
#print('All entries :: ' + str(entrites))
for entry in entrites:
	if entry == 'None':
		continue
	else:
		print("\n")
		s = (str(entry))
		string = s[s.find("(")+1:s.find(")")]
		kp = PyKeePass('mynewncrdb.kdbx', password='qwerty@1234')
		entry = kp.find_entries(username=string, first=True)
		print(str(entry))
		expirtdate = entry.notes
		print('Entered date : ' + expirtdate)
		currentdate = datetime.date.today()
		print('Current date : ' + str(currentdate))
		datetime_obj = datetime.datetime.strptime(expirtdate, '%d/%m/%Y') # convert inputed date into date
		diff = datetime_obj.date() - currentdate # take .date because we only need date not time
		print('Difference :' +  str(diff))
		DAYS = str(diff)
		DAYSLEFT = DAYS.split()[0]
		Daysleft_integer = int(DAYSLEFT)
		Daysleft_integer = int(DAYSLEFT)

		if (Daysleft_integer < 15):
			print('create incident')
		else:
			print('Enough days left')


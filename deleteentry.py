from pykeepass import PyKeePass
import csv
from datetime import date
import datetime as dt
import datetime


#Username,Title,Password = input('Enter Username, Title, password : ').split()
Username = input('Enter Username : ')
#Title = input('Enter Title : ')
#Password = input ('Enter password : ')

kp = PyKeePass('mynewncrdb.kdbx', password='qwerty@1234')
group = kp.find_groups(name='ACCOUNTS', first=True)
#entries = kp.add_entry(group, 'SOUP2', 'fa230230', 'qwerty@123456', url='None', notes=Expirydate)
entries = kp.delete_entry(group, Username)
print('Entries :::' + str(entries))
#with open ('/home/oracle/Details.csv', "a") as file:
#	file.write(Title + ',' + Username + ',' + Password + ',' + formatted_date1 + '\n')

#save database
#kp.save()

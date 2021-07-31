from pykeepass import PyKeePass
import csv
from datetime import date
import datetime as dt
import datetime


#Username,Title,Password = input('Enter Username, Title, password : ').split()
Username = input('Enter Username : ')
Title = input('Enter Title : ')
Password = input ('Enter password : ')
date_str = input("Enter the expiry date in format dd/mm/yyy : ") #inputed date is in string need to conver ot into date
datetime_obj = datetime.datetime.strptime(date_str, '%d/%m/%Y') # convert inputed date into date

#original_date = datetime.datetime.strptime("2021-01-11", '%Y-%m-%d')
formatted_date = datetime_obj.strftime("%d/%m/%Y")
formatted_date1 = str(formatted_date)
##print("entered date ==",datetime_obj.date())
##DATE1 = str(datetime_obj.date())
##Expirydate = DATE1.replace('-','/')
##print('Last ::: ' + Expirydate)

kp = PyKeePass('mynewncrdb.kdbx', password='qwerty@1234')
group = kp.find_groups(name='ACCOUNTS', first=True)
#entries = kp.add_entry(group, 'SOUP2', 'fa230230', 'qwerty@123456', url='None', notes=Expirydate)
entries = kp.add_entry(group, Username, Title, Password, url='None', notes=formatted_date1)
print('Entries :::' + str(entries))
#with open ('/home/oracle/Details.csv', "a") as file:
#	file.write(Title + ',' + Username + ',' + Password + ',' + formatted_date1 + '\n')

#save database
kp.save()

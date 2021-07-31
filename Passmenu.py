#!/usr/bin/python3
import os
ans=True
while ans:
	print("""
		1.Add an entry
		2.Password expiry check
		3.List entries
		4.Delete an entry
		5.Exit/Quit
		""")
	ans = input("What would you like to do? ")
	if ans=="1":
		os.system ('python /home/oracle/KeepassManager/addentry.py')
	elif ans=="2":
		os.system ('python /home/oracle/KeepassManager/Passmanager.py')
	elif ans=="3":
		os.system ('python /home/oracle/KeepassManager/Listentries.py')
	elif ans=="4":
		os.system ('python /home/oracle/KeepassManager/Deletentry.py')
	elif ans=="5":
		print("\n Goodbye") 
		ans = None
	else:
		print("\n Not Valid Choice Try again")

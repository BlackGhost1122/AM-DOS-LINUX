from tkinter import *
from messagebox import *
from tkinter import messagebox
from colorama import *
import os
import time
import subprocess
import webbrowser
import pyfiglet as p

linux_shell = p.figlet_format("COMMAND PROMT", font="slant")
print(linux_shell)
print("\nList of commands - 'help'\n")

while True:
	try:
		shell = input("$ ")
		if shell == 'Help' or shell == 'help' or shell == 'HELP':
			print("""\n
+----------------+					
|    commands    |
|  1. dir        |
|  2. chk disk   |
|  4. diskpart	 |
|  5. clear      |
+----------------+\n""")

		elif shell == 'Dir' or shell == 'dir' or shell == 'DIR':
			print("\nDIR: chk disk\n")
			print("\nDIR: diskpart\n")
			print("\nDIR: clear\n")

		elif shell == 'chk disk':
			print("\nDISK CHECK PROCESS HAS BEEN STARTED...\n")
			time.sleep(3)
			for i in range(1, 10):
				print("Disk checked - Process - {}%".format(i * 10))
				time.sleep(0.10)
				time.sleep(0.10)
			print("\nDisk verified successfully! And there are no problems with it\n")
			time.sleep(3)
			os.system('cls')
			linux_shell = p.figlet_format("COMMAND PROMT", font="slant")
			print(linux_shell)
			print("\nList of commands - 'help'\n")

		elif shell == 'Clear' or shell == 'clear' or shell == 'CLEAR':
			os.system('cls')
			linux_shell = p.figlet_format("COMMAND PROMT", font="slant")
			print(linux_shell)
			print("\nList of commands - 'help'\n")

		elif shell == 'Diskpart' or shell == 'diskpart' or shell == 'DISKPART':
			print("""
   TOM  ###	     NAME    Label    File System     Type       Size
-------------- --------  -------  -------------  ---------  --------- 
  TOM 0           C       ???        NTFS        Chapter   ??? Gb/Mb
  TOM 1           D       ???        NTFS        Chapter   ??? Gb/Mb 

""")
		elif shell == 'Help diskpart' or shell == 'help diskpart':
			print("""\n
+-----------------------+					
|   commands diskpart   |
|  1. select  disk (num)|
|  2. clean (num)       |
|  3. format (num)      |
+-----------------------+\n""")

		elif shell == 'disk 0' or shell == 'disk 1':
			print(f"\nSelected {shell}\n")

		elif shell == 'clean 0':
			print("\nProcess...\n")
			time.sleep(2)
			print("\nCleared disk 0\n")

		elif shell == 'clean 1':
			print("\nProcess...\n")
			time.sleep(2)
			print("\nCleared disk 1\n")

		elif shell == 'format 0':
			print("\nProcess...\n")
			time.sleep(2)
			print("\nFormatted disk 0\n")

		elif shell == 'format 1':
			print("\nProcess...\n")
			time.sleep(2)
			print("\nFormatted disk 1\n")

		else:
			print("\nError! Unknown command please try again\n")
			os.sytem('cls')
			linux_shell = p.figlet_format("COMMAND PROMT", font="slant")
			print(linux_shell)
			print("\nList of commands - 'help'\n")
	except:
		print("\nError! Unknown command please try again\n")
		os.system('cls')
		linux_shell = p.figlet_format("COMMAND PROMT", font="slant")
		print(linux_shell)
		print("\nList of commands - 'help'\n")
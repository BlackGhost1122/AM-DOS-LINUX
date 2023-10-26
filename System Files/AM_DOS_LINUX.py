from termcolor import colored
from colorama import *
from messagebox import *
from tkinter import *
from tkinter import messagebox
import pyfiglet as p
import subprocess
import webbrowser
import pygame
import time
import sys
import os
		
class AM_DOS_LINUX():
	def __init__(self, shell):
		self.shell = shell
		init()
		
	def display_info(self):
		linux = p.figlet_format("AM DOS LINUX", font="slant")
		print(linux)
		print("\nList of commands - 'help'\n")
		showinfo("AM DOS LINUX", "Welcome to Am Dos Linux!")
		
	def os_script(self):
		pygame.mixer.init()
		pygame.mixer.music.load("Windows Longhorn.mp3")
		pygame.mixer.music.play()
		while True:
			try:
				self.shell = input("$ ")
				if self.shell == 'Help' or self.shell == 'help':
					print("""\n
+----------------+					
|    commands    |
|  1. dir        |
|  2. chk system |
|  3. ./(prog)   |
|  4. diskpart	 |
|  5. clear      |
| 6. /install.GUI|
+----------------+					
\n""")

				elif self.shell == 'Dir' or self.shell == 'dir' or self.shell == 'DIR':
					dir_programs = ['snake', 'chk system', 'chrome', 'calculator GUI', 'calculator_dos']
					for dir_program in dir_programs:
						print(f"\nDIR: {dir_program}\n")
					
				elif self.shell == './chk system':
					print("\nNo problem\n")

				elif self.shell == './install.GUI':
					print("\nProcess...\n")
					time.sleep(2)
					DETACHED_PROCESS = 0x00000008
					subprocess.Popen("start /b python AM_DOS_LINUX_GUI.py", creationflags=DETACHED_PROCESS, shell=True)

				elif self.shell == 'Exit' or self.shell == 'exit' or self.shell == 'EXIT':
					pygame.mixer.init()
					pygame.mixer.music.load("Exit.mp3")
					pygame.mixer.music.play()
					time.sleep(3)
					break
				
				elif self.shell == 'clear':
					os.system("cls")
					linux = p.figlet_format("AM DOS LINUX", font="slant")
					print(linux)
					print("\nList of commands - 'help'\n")
					
				elif self.shell == 'diskpart':
					print("""
   TOM  ###	     NAME    Label    File System     Type       Size
-------------- --------  -------  -------------  ---------  --------- 
  TOM 0           C       ???        NTFS        Chapter   ??? Gb/Mb
  TOM 1           D       ???        NTFS        Chapter   ??? Gb/Mb 

""")

				elif self.shell == 'Help diskpart' or self.shell == 'help diskpart':
					print("""\n
+-----------------------+					
|   commands diskpart   |
|  1. select  disk (num)|
|  2. clean (num)       |
|  3. format (num)      |
+-----------------------+
\n""")				
				elif self.shell == 'disk 0' or self.shell == 'disk 1':
					print(f"\nSelected {self.shell}\n")

				elif self.shell == 'clean 0':
					print("\nProcess...\n")
					time.sleep(2)
					print("\nCleared disk 0\n")

				elif self.shell == 'clean 1':
					print("\nProcess...\n")
					time.sleep(2)
					print("\nCleared disk 1\n")

				elif self.shell == 'format 0':
					print("\nProcess...\n")
					time.sleep(2)
					print("\nFormatted disk 0\n")

				elif self.shell == 'format 1':
					print("\nProcess...\n")
					time.sleep(2)
					print("\nFormatted disk 1\n")

				elif self.shell == './snake':
					print("\nProcess...\n")
					time.sleep(2)
					DETACHED_PROCESS = 0x00000008
					subprocess.Popen("start /b python snake.py", creationflags=DETACHED_PROCESS, shell=True)

				elif self.shell == './Calculator' or self.shell == './calculator' or self.shell == './Calc' or self.shell == './calc':
					print("\nProcess...\n")
					time.sleep(2)
					DETACHED_PROCESS = 0x00000008
					subprocess.Popen("start /b python calculator-gui.py", creationflags=DETACHED_PROCESS, shell=True)

				elif self.shell == './calculator_dos' or self.shell == './Calculator.dos' or self.shell == './Calculator_Dos':
					number1 = int(input('\nEnter the one number: '))
					number2 = int(input('\nEnter the two number: '))
					operation = input('\nEnter the operator:  ')
					if operation == '+':
						print(f"\n{number1 + number2}\n")
					elif operation == '-':
						print(f"\n{number1 - number2}\n")
					elif operation == '*':
						print(f"\n{number1 * number2}\n")
					elif operation == '/':
						print(f"\n{number1 / number2}\n")
					elif operation == '%':
						print(f"\n{number1 % number2}\n")
					else:
						print("\nError! Unknown command please try again\n")
				else:
					pygame.mixer.init()
					pygame.mixer.music.load("Error.mp3")
					pygame.mixer.music.play()
					print("\nError! Unknown command please try again\n")

			except:
				pygame.mixer.init()
				pygame.mixer.music.load("Error.mp3")
				pygame.mixer.music.play()
				print("\nError! Unknown command please try again\n")

"""AM DOS LINUX CLASS"""
linux = AM_DOS_LINUX('shell')
linux.display_info()
linux.os_script()

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
import os

os.system("cls")
class AM_DOS_LINUX_INSTALLER():
	def __init__(self, linux_shell):
		self.shell = linux_shell
		
	def display_installer_info(self):
		am_dos_linux_installer = p.figlet_format("AM DOS LINUX INSTALLER", font="slant")
		print(am_dos_linux_installer)
		init()

		print("""
+------------------------+
|  WELCOME TO AM DOS     |
|  LINUX INSTALLER!      |
|			 |
|  1. Install            |
|  2. Upgrade            |
|  3. Checking Update    |
|  4. Repair             |
|  5. Exit               |
+------------------------+
""")
		 
	def display_installer_script_info(self):
		while True:
			try:
				self.linux_shell = input("$ ")
				if self.linux_shell == 'clear':
					os.system("cls")
					am_dos_linux_installer = p.figlet_format("AM DOS LINUX INSTALLER", font="slant")
					print(am_dos_linux_installer)
					
					print("""
+------------------------+
|  WELCOME TO AM DOS     |
|  LINUX INSTALLER!	 |
|			 |
|  1. Install            |
|  2. Upgrade            |
|  3. Checking Update    |
|  4. Repair             |
|  5. Exit               |
+------------------------+
""")
					
				elif self.linux_shell == '1' or self.linux_shell == 'Install' or self.linux_shell == 'install':
					os.system("cls")
					am_dos_linux_installer = p.figlet_format("AM DOS LINUX INSTALL", font="slant")
					print(am_dos_linux_installer)
					time.sleep(2)
					print("\nProcess...\n")
					time.sleep(2)
					print("\nStarting Install file system Linux...\n")
					time.sleep(5)
					for i in range(1, 10):
						print("Installed. Process - {}%".format(i * 11))
						time.sleep(0.30)
					print("File System Installed!")

					time.sleep(5)
					os.system("cls")
					break
					
					
				elif self.linux_shell == '2' or self.linux_shell == 'Upgrade' or self.linux_shell == 'upgrade':
					os.system("cls")
					upgrade_linux = p.figlet_format("UPGRADE AM DOS LINUX", font="slant")
					print(upgrade_linux)
					print("\nProcess...\n")
					print("\nStarting Updating Linux...\n")
					time.sleep(5)
					for i in range(1, 10):
						print("Updated Linux. Process - {}%".format(i * 11))
						time.sleep(0.30)
					print("Am Dos Linux Updated!")
					os.system("cls")
					am_dos_linux_installer = p.figlet_format("AM DOS LINUX INSTALLER", font="slant")
					print(am_dos_linux_installer)
					print("""
+------------------------+
|  WELCOME TO AM DOS     |
|  LINUX INSTALLER!	 |
|			 |
|  1. Install            |
|  2. Upgrade            |
|  3. Checking Update    |
|  4. Repair             |
|  5. Exit               |
+------------------------+
""")
					showinfo("Success!", "The latest updates have been successfully downloaded!")	
					
				elif self.linux_shell == '3' or self.linux_shell == 'Checking Update' or self.linux_shell == 'checking update':
					os.system("cls")
					upgrade_linux = p.figlet_format("UPGRADE AM DOS LINUX", font="slant")
					print(upgrade_linux)
					print("\nChecking for updates...\n")
					time.sleep(4)
					print("\nThere is 1 update!\n")
					time.sleep(2)
					print("\nThe process of automatically downloading updates has started...\n")
					time.sleep(2)
					print("\nStarting Updating Linux...\n")
					time.sleep(5)
					for i in range(1, 10):
						print("Updated Linux. Process - {}%".format(i * 11))
						time.sleep(0.30)
					print("Am Dos Linux Updated!")
					os.system("cls")
					am_dos_linux_installer = p.figlet_format("AM DOS LINUX INSTALLER", font="slant")
					print(am_dos_linux_installer)
					
					print("""
+------------------------+
|  WELCOME TO AM DOS     |
|  LINUX INSTALLER!	 |
|			 |
|  1. Install            |
|  2. Upgrade            |
|  3. Checking Update    |
|  4. Repair             |
|  5. Exit               |
+------------------------+
""")
					showinfo("Success!", "The latest updates have been successfully downloaded!")
					
					
				elif self.linux_shell == '4' or self.linux_shell == 'Repair' or self.linux_shell == 'repair':
					os.system("cls")
					repair_computer = p.figlet_format("REPAIR COMPUTER", font="slant")
					print(repair_computer)
					time.sleep(2)
					print("\nProcess...\n")
					time.sleep(2)
					print("\nRepairing your computer...\n")
					time.sleep(5)
					for i in range(1, 10):
						print("Repaired Computer. Process - {}%".format(i * 11))
						time.sleep(0.10)
						time.sleep(2)
					print("Repeired Your Computer!")
					time.sleep(2)
					print("\nNo errors found in your system\n")
					time.sleep(2)
					print("\nPress any key to continue\n")
					
				elif self.linux_shell == '5' or self.linux_shell == 'Exit' or self.linux_shell == 'exit':
					exit()
					break
					
				else:
					print("\nError\n")
					os.system("cls")
					am_dos_linux_installer = p.figlet_format("AM DOS LINUX INSTALLER", font="slant")
					print(am_dos_linux_installer)
					print("""
+------------------------+
|  WELCOME TO AM DOS     |
|  LINUX INSTALLER!	 |
|			 |
|  1. Install            |
|  2. Upgrade            |
|  3. Checking Update    |
|  4. Repair             |
|  5. Exit               |
+------------------------+
""")
					
			except:
				print("\nError\n")
				os.system("cls")
				am_dos_linux_installer = p.figlet_format("AM DOS LINUX INSTALLER", font="slant")
				print(am_dos_linux_installer)
				print("""
+------------------------+
|  WELCOME TO AM DOS     |
|  LINUX INSTALLER!	 |
|			 |
|  1. Install            |
|  2. Upgrade            |
|  3. Checking Update    |
|  4. Repair             |
|  5. Exit               |
+------------------------+
""")
	
	
class Install_And_Registration(AM_DOS_LINUX_INSTALLER):
	def __init__(self, linux_shell, name_shell, password_shell, confirm_password_shell):
		self.linux_shell = linux_shell
		self.name_shell = name_shell
		self.password_shell = password_shell
		self.confirm_password_shell = confirm_password_shell
		
	def display_info(self):
		os.system("cls")
		linux_install = p.figlet_format("INSTALL LINUX", font="slant")
		print(linux_install)
		print("""
+------------------------+
| WHAT OS DO YOU WANT TO |
|       INSTALL?         |
|			 |
|  1. AM DOS LINUX HOME  |
|  2. AM DOS LINUX PRO   |
|  3. AM DOS LINUX MAX   |
+------------------------+
""")

	def install_linux_and_registration_script_info(self):
		while True:
			try:
				self.linux_shell = input("$ ")
				if self.linux_shell == '1':
					os.system("cls")
					linux_home = p.figlet_format("AM DOS LINUX HOME", font="slant")
					print(linux_home)
					time.sleep(2)
					print("\nProcess...\n")
					time.sleep(2)
					print("\nINSTALLING AM DOS LINUX HOME...\n")
					time.sleep(5)
					for i in range(1, 10):
						print("Installed Linux Home. Process - {}%".format(i * 11))
						time.sleep(0.10)
						time.sleep(2)
					print("\nLinux Home Installed!\n")
					time.sleep(2)
					os.system("cls")
					break
					
				elif self.linux_shell == '2':
					os.system("cls")
					linux_professional = p.figlet_format("AM DOS LINUX PROFESSIONAL", font="slant")
					print(linux_professional)
					time.sleep(2)
					print("\nProcess...\n")
					time.sleep(2)
					print("\nINSTALLING AM DOS LINUX PROFESSIONAL...\n")
					time.sleep(5)
					for i in range(1, 10):
						print("installed Linux Professional. Process - {}%".format(i * 11))
						time.sleep(0.10)
						time.sleep(2)
					print("\nLinux Profssional Installed!\n")
					time.sleep(2)
					os.system("cls")
					break
					
				elif self.linux_shell == '3':
					os.system("cls")
					linux_ultimate = p.figlet_format("AM DOS LINUX ULTIMATE", font="slant")
					print(linux_ultimate)
					time.sleep(2)
					print("\nProcess...\n")
					time.sleep(2)
					print("\nINSTALLING AM DOS LINUX ULTIMATE\n")
					time.sleep(5)
					for i in range(1, 10):
						print("Installed Linux Ultimate. Process - {}%".format(i * 11))
						time.sleep(0.10)
						time.sleep(2)
					print("\nLinux Ultimate Installed!\n")
					time.sleep(2)
					os.system("cls")
					break
					
				else:
					print("\nError! Unknown command please try again\n")
					os.system("cls")
					linux_install = p.figlet_format("INSTALL LINUX", font="slant")
					print(linux_install)
					print("""
+------------------------+
| WHAT OS DO YOU WANT TO |
|       INSTALL?         |
|			 |
|  1. AM DOS LINUX HOME  |
|  2. AM DOS LINUX PRO   |
|  3. AM DOS LINUX MAX   |
+------------------------+
""")
					
			except:
				print("\nError! Unknown command please try again\n")
				os.sytem("cls")
				linux_install = p.figlet_format("INSTALL LINUX", font="slant")
				print(linux_install)
				print("""
+------------------------+
| WHAT OS DO YOU WANT TO |
|       INSTALL?	 |
|			 |
|  1. AM DOS LINUX HOME  |
|  2. AM DOS LINUX PRO   |
|  3. AM DOS LINUX MAX   |
+------------------------+
""")

	def registration_linux_script(self):
		os.system("cls")
		registration_linux = p.figlet_format("REGISTRATION AM DOS LINUX", font="slant")
		print(registration_linux)
		time.sleep(2)
		self.name_shell = input("username: ")
		self.password_shell = input("password: ")
		self.confirm_password_shell = input("confirm password: ")
		time.sleep(3)
		print("\nCreating account...\n")
		time.sleep(2)
		print("\nAccount Created!\n")
		time.sleep(2)
		print(f"\n{self.name_shell}\n")
		print(f"\n{self.password_shell}\n")
		time.sleep(2)
		os.system("cls")
		time.sleep(2)
		DETACHED_PROCESS = 0x00000008
		subprocess.Popen("start /b python AM_DOS_LINUX.py", creationflags=DETACHED_PROCESS, shell=True)

"""AM DOS LINUX INSTALLER CLASS"""
linux_installer = AM_DOS_LINUX_INSTALLER('shell')
linux_installer.display_installer_info()
linux_installer.display_installer_script_info()

"""INSTALL AND REGISTRATION AM DOS LINUX CLASS"""
install_and_registration = Install_And_Registration('shell', 'name', 'password', 'confirm password')
install_and_registration.display_info()
install_and_registration.install_linux_and_registration_script_info()
install_and_registration.registration_linux_script()

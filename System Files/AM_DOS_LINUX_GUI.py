from tkinter import *
from tkinter import messagebox
from messagebox import *
import pygame
import subprocess
import webbrowser
import time
import sys
import os

class Setup(Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master1 = master
		self.master1.protocol("WM_DELETE_WINDOW", self.closing_setup)
		self.master1.geometry("600x400")
		self.master1.resizable(width=False, height=False)
		self.master1.title("Setup AM DOS LINUX GUI")
		self.master1['bg'] = 'black'
		self.setup_widgets()

	def setup_widgets(self):

		pygame.mixer.init()
		pygame.mixer.music.load("Windows Longhorn.mp3")
		pygame.mixer.music.play()

		setup_linux_lbl = Label(self.master1, text='AM DOS LINUX GUI', bg='black', fg='white', font='Arial 20 bold', padx=10, pady=8)
		setup_linux_lbl.pack()

		self.setup_linux_btn = Button(self.master1, text='Install', bg='black', fg='white', font='Arial 20 bold', padx=10, pady=8, command=self.next_am_dos_linux_gui_installer)
		self.setup_linux_btn.place(relx=0.39, rely=0.4)

		self.command_promt_btn = Button(self.master1, text='Running the command promt', bg='black', fg='white', padx=10, pady=8, font='Arial 7 bold', command=self.runing_shell)
		self.command_promt_btn.place(relx=0.00, rely=0.93)

	def closing_setup(self):
		if messagebox.askokcancel("Closing setup", "Do you want to exit the setup AM DOS LINUX GUI?"):
			self.master1.destroy()

	def next_am_dos_linux_gui_installer(self):
		self.master1.withdraw()
		self.next_installer = Toplevel(self.master1)
		self.installer_gui_version = Installer(self.next_installer)

	def runing_shell(self):
		DETACHED_PROCESS = 0x00000008
		subprocess.Popen("start /b python command-promt.py", creationflags=DETACHED_PROCESS, shell=True)


class Installer(Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master2 = master
		self.master2.protocol("WM_DELETE_WINDOW", self.closing_installer)
		self.master2.geometry("400x400")
		self.master2.attributes('-fullscreen', True)
		self.master2.resizable(width=False, height=False)
		self.master2['bg'] = 'black'
		self.master2.title("AM DOS LINUX GUI INSTALLER")
		self.installer_widgets()

	def installer_widgets(self):
		am_dos_linux_gui_lbl = Label(self.master2, text='AM DOS LINUX GUI', bg='black', fg='white', font='Arial 50 bold', padx=10, pady=8)
		am_dos_linux_gui_lbl.place(relx=0.25, rely=0.2)

		self.command_promt_installer_btn = Button(self.master2, text='Running the command promt', bg='black', fg='white', font='Arial 7 bold', padx=10, pady=8, command=self.runing_shell)
		self.command_promt_installer_btn.place(relx=0.0, rely=0.95)

		self.language_list_lbl = Label(self.master2, text='language and region:', bg='black', fg='white', font='Arial 20 bold')
		self.language_list_lbl.place(relx=0.27, rely=0.4)

		self.english_list_lbl = Label(self.master2, text='England: English', bg='black', fg='white', font='Arial 20 bold')
		self.english_list_lbl.place(relx=0.53, rely=0.4)

		self.continue_btn = Button(self.master2, text='continue', bg='black', fg='white', font='Arial 20 bold', padx=10, pady=8, command=self.continue_install)
		self.continue_btn.place(relx=0.42, rely=0.6)

	def closing_installer(self):
		if messagebox.askokcancel("Closing installer", "Do you want to exit the installer AM DOS LINUX GUI?"):
			self.master2.destroy()

	def runing_shell(self):
		DETACHED_PROCESS = 0x00000008
		subprocess.Popen("start /b python command-promt.py", creationflags=DETACHED_PROCESS, shell=True)

	def continue_install(self):
		self.master2.withdraw()
		self.next_installer = Toplevel(self.master2)
		self.installer_gui_version = Activation(self.next_installer)

class Activation(Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master3 = master
		self.master3.geometry("400x400")
		self.master3.attributes('-fullscreen', True)
		self.master3.resizable(width=False, height=False)
		self.master3['bg'] = 'black'
		self.master3.title('Activation AM DOS LINUX GUI')
		self.activation_widgets()

	def activation_widgets(self):
		activation_lbl = Label(self.master3, text='Activation AM DOS', bg='black', fg='white', font='Arial 50 bold', padx=10, pady=8)
		activation_lbl.place(relx=0.25, rely=0.2)

		self.activation_entry = Entry(self.master3, font='Arial 45 bold', fg='black')
		self.activation_entry.place(relx=0.24, rely=0.4)

		self.activation_btn = Button(self.master3, text='Check', bg='black', fg='white', font='Arial 40 bold', padx=60, command=self.activation_script)
		self.activation_btn.place(relx=0.24, rely=0.5)

		self.skip_activation_btn = Button(self.master3, text='Skip act', bg='black', fg='white', font='Arial 40 bold', padx=50, command=self.skip_activation)
		self.skip_activation_btn.place(relx=0.47, rely=0.5)

	def activation_script(self):
		self.activation_key = self.activation_entry.get()
		if self.activation_key == 'AMDOS-AMDOS-LINUX':
			time.sleep(2)
			showinfo('Sucess!', 'The product key has arrived!')
			self.master3.withdraw()
			self.check_key = Toplevel(self.master3)
			self.master3.installer_gui_version = Installing_Linux(self.check_key)
		else:
			pygame.mixer.init()
			pygame.mixer.music.load("Error.mp3")
			pygame.mixer.music.play()
			showerror('Error', 'The product key did not match')

	def skip_activation(self):
		self.skip_activation = self.activation_entry.get()
		time.sleep(2)
		self.master3.withdraw()
		self.check_key = Toplevel(self.master3)
		self.master3.installer_gui_version = Installing_Linux(self.check_key)

class Installing_Linux(Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master4 = master
		self.master4.geometry('400x400')
		self.master4.resizable(width=False, height=False)
		self.master4.attributes('-fullscreen', True)
		self.master4.title("Installing AM DOS LINUX GUI")
		self.master4.protocol('WM_DELETE_WINDOW', self.closing_installing)
		self.master4['bg'] = 'black'
		self.installing_widgets()

	def installing_widgets(self):
		pass

	def closing_installing(self):
		if messagebox.askokcancel('Closing', 'Do you want to exit the installer AM DOS LINUX GUI?'):
			self.master4.destroy()

if __name__ == '__main__':
	root = Tk()
	linux_setup = Setup(root)
	linux_setup.mainloop()


"""
pygame.mixer.init()
pygame.mixer.music.load("file.mp3")
pygame.mixer.music.play()

"""
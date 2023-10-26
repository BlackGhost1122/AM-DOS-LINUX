import time
import random
import pygame

for i in range(1, 40):
	time.sleep(1)
	random_number = random.randint(1, 999)
	print(f"\nStarting script...{random_number}\n")
	time.sleep(0.10)


for i in range(1, 10):
	time.sleep(1)
	time.sleep(0.40)
	print("\nInstalling system files - {}%\n".format(i * 10))
	time.sleep(3)
	time.sleep(0)
	

for i in range(1, 10):
	time.sleep(1)
	print("\nExtracting system files - {}%\n".format(i * 10))
	time.sleep(0)
	time.sleep(3)

for i in range(1, 10):
	time.sleep(1)
	print("\nCompletion - {}%\n".format(i * 10))
	time.sleep(0)

time.sleep(2020202)
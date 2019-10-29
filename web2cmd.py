import requests
import termcolor
import colorama
import os
import json
import platform

print(open("README.txt").read())

def user_agreement():
	resp = input('\n\nDo you agree to the terms listed above? (Y/n)')
	if(resp == "Y" or resp == "y"):
	 	init()
	else:
	 	print("Exiting now...")
	 	exit(0)

def init():
	print(open("logo.txt").read())

	print(platform.system())

if __name__ == "__main__":
	user_agreement()
import requests
import os
import json
import platform
from termcolor import colored
import colorama
import datetime

colorama.init()
info = "[" + colored("*", "cyan") + "]"
positive = "[" + colored("+", "green") + "]"
negative = "[" + colored("-", "red") + "]"
warning = "[" + colored("!", "yellow") + "]"

print(open("README.txt").read())

def user_agreement():
	resp = input(f'\n[!] Do you agree to the terms listed above? (Y/n)')
	if resp == "Y":
	 	init()
	else:
	 	print("Exiting now...")
	 	exit(0)

def init():

	print(open("logo.txt").read())

	print(f"{info} Loading web2cmd for {platform.system()}")

	print(f"{positive} Loaded web2cmd for {platform.system()}")

	d = datetime.datetime.today()

	print(f"{info} Started web2cmd at {d.strftime('%H:%M:%S')} {d.strftime('%b-%d-%Y')}")

if __name__ == "__main__":
	user_agreement()

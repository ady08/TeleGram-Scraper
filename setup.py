#!/bin/env python3
# code by : youtube.com/adysitorus ady

"""

you can re run setup.py 
if you have added some wrong value

"""
import os, sys
import configparser
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
def banner():
	os.system('clear')
	print(f"""
	{re}╔═╗{cy}┌─┐┌┬┐┬ ┬┌─┐ |
	{re}╚═╗{cy}├┤  │ │ │├─┘ |
	{re}╚═╝{cy}└─┘ ┴ └─┘┴   |
        {gr}_____________________________________________________________|_                                       
        {gr}++++++++++++++++===={cy}++++++++++++++++++++++{re}++++++     |
        {re}|Author    : {cy} Nicoleus Sitorus        ++++{re}++++++     |
        {re}|Thanks TO : {cy} Nicoleus Sitorus        ++++{gr}++++++     |
        {re}|Thanks TO :  {cy} SAMOSIR CYBER TEAM     ++++{gr}++++++     |
        {re}|HOARS..... HORAS {cy}HORAS SAMOSIR CYBER TEAM ++{re}++++    |
        {gr}++++++++++++++++===={cy}++++++++++++++++++++++{re}++++++     |
        {gr}_____________________________________________________________|_
	 """)
banner()
print(gr+"[+] Installing requierments ...")
os.system('python3 -m pip install telethon')
os.system('pip3 install telethon')
banner()
os.system("touch config.data")
cpass = configparser.RawConfigParser()
cpass.add_section('cred')
xid = input(cy+"[+] HORAS....!!!!!  "+re)
xhash =input(gr+"[=]+++++++++++++++++++ "+cy)
xid = input(gr+"[+] enter api ID : "+re)
cpass.set('cred', 'id', xid)
xhash = input(gr+"[+] enter hash ID : "+re)
cpass.set('cred', 'hash', xhash)
xphone = input(gr+"[+] enter phone number : "+re)
cpass.set('cred', 'phone', xphone)
setup = open('config.data', 'w')
cpass.write(setup)
setup.close()
print(gr+"[+] setup complete !")
print(gr+"[+] now you can run any tool !")
print(gr+"[+] make sure to read docs 4 installation & api setup")
print(gr+"[+] https://github.com/ady08/TeleGram-Scraper/blob/master/README.md")

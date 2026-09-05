#HDB = (Human Debug Bridge)
#This Code Created By HDB Team 
#HDB Boss Is Mehrdad King
#Cleaner
import os
os.system('cls')
os.system('clear')

#DownLoader
import os
import sys
import time

DL = input ('Hey Boss DownLoad Starter Pip ? [y/n] ')

if DL == 'y':
  os.system('cls')
  os.system('clear')
  print ("DownLoad Started By HDB os Don't Close Page")
  os.system('pip install colorama')
  #DownLoad Not Com....
  print ('Finding DownLoad Pip ')
  print ('Searching...')
  time.sleep(5)

elif DL == 'n':
  os.system('cls')
  os.system('clear')
  print ('Not Down Pip = Not Work Script')
  time.sleep(3)

else:
  print ('ERORR 404')
  sys.exit()

#Cleaner
os.system('cls')
os.system('clear')

#Importer And Frommer
import os
import sys
import json
import time
import math
import random
import subprocess
import platform
import pathlib
import shutil
import re
from colorama import Fore, Back, Style, init

#colorama
from colorama import Fore, Back, Style, init

#Slowed Printer And Inputer
def sp(text, delay=0.02):
    for char in str(text):
        print(char, end="", flush=True)
        time.sleep(delay)
    print()
  
def si(text, delay=0.02):
    for char in str(text):
        print(char, end="", flush=True)
        time.sleep(delay)
    return input()

#Random Info
A = random.randint(100, 999)
B = random.randint(100, 999)
C = random.randint(1, 9)
D = random.randint(1, 999)
E = random.randint(1024, 9999)
F = random.randint(1, 999)
G = random.randint(1, 99)
w = shutil.get_terminal_size().columns

#Start HDB Mine Menu
sp ('======> HDB <======')
sp ('Human Debug Bridge ')

time.sleep(3)

os.system('cls')
os.system('clear')

sp(f'Lobby Ip : [{A}.{B}.{C}.{D}]')
sp(f'Lobby Port : [{E}]')
sp(f'Lobby Number : [{F}]')
sp(f'Lobby FireWall Mode : [{G}]')
sp('Loading...')

time.sleep(3)

os.system('cls')
os.system('clear')

PlayMusic = si('Hey Boss Play Hacker Music? [y/n] ')

if PlayMusic.lower() == "y":
    music = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "Music.mp3"
    )

    if os.path.isfile(music):
        os.system(f'mpv --no-video --no-terminal --loop=inf "{music}" >/dev/null 2>&1 &')
        sp('Hacker Music Started!')
    else:
        sp('ERROR: Music.mp3 Not Found')

elif PlayMusic.lower() == "n":
    sp('Ok')

else:
    sp("Hey What Don't Play Music")

#Cleaner
os.system('cls')
os.system('clear')

#Runner
sp(Fore.RED + r"""
██╗  ██╗██████╗ ██████╗
██║  ██║██╔══██╗██╔══██╗
███████║██║  ██║██████╔╝
██╔══██║██║  ██║██╔══██╗
██║  ██║██████╔╝██████╔╝
╚═╝  ╚═╝╚═════╝ ╚═════╝
""")
sp("╔" + "═" * (w - 2) + "╗")
sp("╚" + "═" * (w - 2) + "╝")

sp(Fore.GREEN + '1.DDoS')
sp('2.SMS Bomber [For Iran]')
sp('3.RAT Android')
sp('4.Virus Crafter')
sp('5.CCTV Hack')
sp('6.Ip Tracker')
sp('7.Birds [Better Dirb]')
sp('8.User Phishing')
sp('9.Word Gen Pro')
sp('10.Ultra Fast Intrnet Speed')
sp('11.Op Comperssor')
sp('12.NFC Drop')
sp('13.Flask Chat')
sp('14.Nano Gen AI')
sp('15.Thor Browser')
sp('16.HDB  [High Dynamic Booster] Mega Ram Boost')
sp('17.Net Scanner')
sp('18.GitHub')
sp('19.Settings')
sp(Fore.RED + '20.Exit')

sp("╔" + "═" * (w - 2) + "╗")
sp("╚" + "═" * (w - 2) + "╝")

User = si(Fore.YELLOW + 'ẞelect Ñumbers : ')

os.system('cls')
os.system('clear')


if User == '1':
  os.system('python Tools/ddos/ddos.py')

if User == '2':
  os.system('python Tools/Sms/SmsBomber.py')

if User == '3':
  os.system('termux-open-url "https://cdn.appteka.store/fb032686bff7b5f25c554e8d867fd4f4041b6538/com.xhunter_1.6_6.apk?e=1788614420&s=40XzJlgSoS5Bjz7gl18u6A"')

if User == '4':
  os.system('bash TigerVirus.sh')

if User == '5':
  sp('Hey Boss Not Created This Script')

if User == '6':
  os.system('python Tools/GhostTrack/GhostTR.py')

if User == '7':
  os.system('python Tools/Birds/main.py')

if User == '8':
  os.system('python Tools/UserCollector/User.py')

if User == '9':
  os.system('python Tools/WordGenPro/Ban.py')

if User == '10':
  os.system('python Tools/UFIS/main.py')

if User == '11':
  os.system('python Tools/OP-Compressor/iop.py')

if User == '12':
  os.system('bash Tools/NFD/NFD.sh')

if User == '13':
  os.system('python Tools/FlaskChat/app.py')

if User == '14':
  os.system('python Tools/NanoGen/main.py')

if User == '15':
  os.system('python Tools/ThorBrowser/main.py')

if User == '16':
  os.system('bash Tools/HDB/HDB.sh')

if User == '17':
  os.system('python Tools/NetScanner/app.py')

if User == '18':
  os.system('termux-open-url "https://github.com/banban965"')

if User == '19':
  os.system('python Settings/S.py')

if User == '20':
  os.system('cls')
  os.system('clear')
  sp('Bye')
  sys.exit()
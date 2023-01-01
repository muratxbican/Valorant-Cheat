import os
import colorama
import time
from colorama import Fore
from os import system
from colorama import Fore, Back, Style, init
init(autoreset=True)
import random


os.system('cls')
logo = f"""     

    ____  _                ____           __                        
   / __ \(_)___  ____ _   / __ \___  ____/ /_  __________  _____    
  / /_/ / / __ \/ __ `/  / /_/ / _ \/ __  / / / / ___/ _ \/ ___/    
 / ____/ / / / / /_/ /  / _, _/  __/ /_/ / /_/ / /__/  __/ /        
/_/   /_/_/ /_/\__, /  /_/ |_|\___/\__,_/\__,_/\___/\___/_/         
              /____/                                                

 {Fore.WHITE}(Coded by #Mb ){Fore.RESET}
"""
print(Fore.CYAN+logo)
system("title " + str(hash))
os.system("TASKKILL /F /IM discord.exe")
os.system("TASKKILL /F /IM chrome.exe")
os.system("TASKKILL /F /IM spotify.exe")
os.system("TASKKILL /F /IM steam.exe")
os.system("TASKKILL /F /IM skype.exe")
time.sleep(2)
print(f"[{Fore.GREEN}+{Fore.RESET}] The process is OK. You can return to the game.") 
time.sleep(5)
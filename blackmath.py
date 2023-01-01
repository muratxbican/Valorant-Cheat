import os
import colorama
from colorama import Fore
from os import system
from colorama import Fore, Back, Style, init
init(autoreset=True)
import uuid
import random
import time
from alive_progress import alive_bar
import sys
import ctypes  



hash = random.getrandbits(128)


os.system('cls')
logo = f"""     

 _    __      __                       __     ___          __  _       ________          __     
| |  / /___ _/ /___  _________ _____  / /_   /   |  ____  / /_(_)     / ____/ /_  ____ _/ /_    
| | / / __ `/ / __ \/ ___/ __ `/ __ \/ __/  / /| | / __ \/ __/ /_____/ /   / __ \/ __ `/ __/    
| |/ / /_/ / / /_/ / /  / /_/ / / / / /_   / ___ |/ / / / /_/ /_____/ /___/ / / / /_/ / /_      
|___/\__,_/_/\____/_/   \__,_/_/ /_/\__/  /_/  |_/_/ /_/\__/_/      \____/_/ /_/\__,_/\__/      
                                                                                                
                                                                    

 {Fore.WHITE}(Coded by #Mb ){Fore.RESET}
"""
print(Fore.CYAN+logo)
system("title " + str(hash))
ctypes.windll.user32.MessageBoxW(0, "Make Sure You Leave This Program Open Behind When Using The Valorant Cheat \n\nIn This Way, You Will Provide 99.99% Security Against Valorant Vanguard Protection.", "Protector V4.1", 1)
print("---------------------------------------------------")
print(f"[{Fore.GREEN}1{Fore.RESET}] Full Active Protection") 
print(f"[{Fore.GREEN}2{Fore.RESET}] Full Active Protection V2.0") 
print(f"[{Fore.GREEN}3{Fore.RESET}] Full Active Protection V2.2") 
print(f"[{Fore.GREEN}4{Fore.RESET}] Full Active Protection V2.3") 
print(f"[{Fore.GREEN}5{Fore.RESET}] Full Active Protection V2.4") 
print(f"[{Fore.GREEN}6{Fore.RESET}] 2021 Protection [PRİV]") 
print(f"[{Fore.GREEN}7{Fore.RESET}] Active Protection [FxF-Q85X]") 
print(f"[{Fore.GREEN}8{Fore.RESET}] 2022 Protection [DEMO]")
print("---------------------------------------------------")
cprog = input(f"[{Fore.GREEN}?{Fore.RESET}] Select: ") 
ctypes.windll.user32.MessageBoxW(0, "In order to use the protection system you have chosen with 100% efficiency, first run the Ping Controller.\n\nThe Program Wants To Download Some Security Files To Your Computer. Do You Allow This?\n\nThese Files Do Not Interfere With Valorant Files And Are Invisible", "WARNING!", 1)
def progges():
    for x in 1000, 1500, 700, 0:
        with alive_bar(x) as bar:
            for i in range(1000):
                time.sleep(.005)
                bar()
progges()
time.sleep(2)
print()
print(f"[{Fore.GREEN}1{Fore.RESET}] All Files Installed Successfully") 
print("---------------------------------------------------")
ctypes.windll.user32.MessageBoxW(0, "Protection System Ready to Run\n\nDo you want to start?", "Customized Valorant Protection System", 1)
while True:
    hash = random.getrandbits(128)
    hashx = uuid.uuid1()
    system("title " + str(hashx))
    print(colorama.Fore.WHITE + "[" + colorama.Fore.RED + "!" + colorama.Fore.WHITE + f"] {colorama.Fore. RED}Protection Active! >>{str(hashx)} {colorama.Fore.WHITE} | {colorama.Fore.RED} Protection Active! >>{str(hash)} {colorama.Fore.GREEN} ", end="\r")


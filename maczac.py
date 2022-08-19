# MACCHANGER CODED BY X-byt3
import subprocess
import re
import optparse
import colorama
import playsound
from colorama import Fore
from playsound import playsound


banner = '''
███████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
█░░▄▀░░░░░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░░░░░░░░░░░▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████████████░░░░▄▀░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████
█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░███████████████░░░░▄▀░░░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████
█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████████░░░░▄▀░░░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████
█░░▄▀░░██░░░░░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░███████████░░░░▄▀░░░░███████░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████
█░░▄▀░░██████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░░░▄▀░░░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████
█░░▄▀░░██████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀▄▀░░░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░██████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░░░██████████░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█
███████████████████████████████████████████████████████████████████████████████████████████████████████'''


print(Fore.CYAN + banner)
print(Fore.RED + "\n\n                        💉 coded by X-Byt3")
print(Fore.RED + "                        💉 made with love")
print(Fore.RED + "                        💉 Version = " + Fore.GREEN + "1.0\n\n")
print(Fore.YELLOW)
playsound('welcome.mp3')
            #getting arguments from user function
def get_arg():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest = "interface" , help  = "Select the interface")
    parser.add_option("-m", "--mac", dest = "new_mac" , help  = "Specify the mac address")
    (option, arg) = parser.parse_args()
    if not option.interface:
        playsound('int.mp3')
        parser.error(Fore.RED + "[+]" + Fore.YELLOW + " please specify --interface.")
    elif not option.new_mac:
        playsound('mac.mp3')
        parser.error(Fore.RED + "[+]" + Fore.YELLOW + " please specify --mac")
    return option



            #change_mac function
def change_mac(interface, new_mac):
    print(Fore.RED + "[+]", Fore.BLUE + " CHANGING " +  Fore.BLUE + interface + " " +  Fore.BLUE + "MAC to " + new_mac)
    playsound('chmac.mp3')
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


            #current_mac function
def current_mac(interface):
    curr_mac = subprocess.check_output(["ifconfig", interface])
    curr_mac1 = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", curr_mac.decode("utf-8"))
    if curr_mac1:
        return curr_mac1.group(0)
    else:
        print(Fore.RED + "[+]" + Fore.YELLOW +" ERROR WHILE READING MAC")
        playsound('error.mp3')
        exit()
    







option = get_arg()
change_mac(option.interface, option.new_mac)
currentmac = current_mac(option.interface)
if currentmac == option.new_mac:
    print(Fore.RED + "[+]" + Fore.BLUE +" BOOM! MAC CHANGED SUCCESSFULLY TO ", currentmac)
    playsound('success.mp3')
else:
    print(Fore.RED + "[+]" + Fore.YELLOW + " Wh00PS! SOMETHING WENT WRONG")
    playsound('wrong.mp3')

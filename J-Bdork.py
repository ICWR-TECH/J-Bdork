print("""
    /$$$$$         /$$$$$$$        /$$                     /$$      
   |__  $$        | $$__  $$      | $$                    | $$      
      | $$        | $$  \ $$  /$$$$$$$  /$$$$$$   /$$$$$$ | $$   /$$
      | $$ /$$$$$$| $$$$$$$  /$$__  $$ /$$__  $$ /$$__  $$| $$  /$$/
 /$$  | $$|______/| $$__  $$| $$  | $$| $$  \ $$| $$  \__/| $$$$$$/ 
| $$  | $$        | $$  \ $$| $$  | $$| $$  | $$| $$      | $$_  $$ 
|  $$$$$$/        | $$$$$$$/|  $$$$$$$|  $$$$$$/| $$      | $$ \  $$
 \______/         |_______/  \_______/ \______/ |__/      |__/  \__/
====================================================================
[*] Jancok Bing Dorker - R&D ICWR
====================================================================
""")

import socket
from requests import get
from re import findall
from time import sleep as delay
from threading import Thread
from datetime import datetime
from os.path import isfile
from os.path import isdir
from os import mkdir
from fake_useragent import UserAgent

class jancok_dorker:

    def check_site(self, site):

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((site.split("/")[2], 80))
            s.send("GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(site.split("/")[2]).encode())
            s.close()
            print("[+] {}".format(site))
            open("result-site/result-" + str(datetime.now().strftime("%Y-%m-%d")) + ".txt", "a").write("{}\n".format(site))

        except:

            print("[-] {}".format(site))

    def extract_link(self, dork, page):

        try:

            resp = get(url="https://www.bing.com/search?q={}&first={}".format(dork, str(page)), headers={ "User-Agent": UserAgent().random }, timeout=5)
            link = findall("href=\"(.+?)\"", resp.text)

            for x in link:

                xurl = x.split("/")

                if xurl[0] == "http:" or xurl[0] == "https:":

                    if all(not xxx in xurl[2] for xxx in [".bing.", ".google.", ".microsoft."]):

                        Thread(target=self.check_site, args=(x, )).start()
                        delay(0.1)

        except:

            pass

    def __init__(self):

        if not isdir("result-site"):

            mkdir("result-site")

        input_dork = input("[*] Dork / List Dork : ")
        page = input("[*] Page : ")
        print("\n")

        if input_dork != '' and page != '':

            if isfile(input_dork):

                for dork in open(input_dork, errors='ignore').read().split("\n"):

                    for i in range(0, int(page)):

                        if dork != '':

                            Thread(target=self.extract_link, args=(dork, "{}0".format(str(i)))).start()
                            delay(0.1)

            else:

                for i in range(0, int(page)):
                    
                    Thread(target=self.extract_link, args=(input_dork, "{}0".format(str(i)))).start()
                    delay(0.1)

        else:

            print("[-] Invalid Option")

if __name__ == "__main__":
    
    jancok_dorker()

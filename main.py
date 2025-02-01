import os
import requests
import telebot
from concurrent.futures import ThreadPoolExecutor
from json import dumps
from ssl import CERT_NONE
from gzip import decompress
from random import choice, choices
from websocket import create_connection
from colorama import Fore, Style, init
import time


init(autoreset=True)


ascii_art = '''
  _________  ____ 
 /   _____/ /_   |
 \_____  \   |   |
 /        \  |   |
/_______  /  |___|
'''


for char in ascii_art:
    time.sleep(0.1)
    print(char, end='')

print(f'''
{Fore.BLUE}--------------------------------------------------
      {Fore.GREEN}Welcome to the {Fore.YELLOW}S1{Fore.GREEN} Tool    
            {Fore.CYAN}Tool Safuem
       {Fore.MAGENTA}Developer  :  @jokerpython3
{Fore.BLUE}--------------------------------------------------
''')


token = "7915967893:AAERfb3HxG0GHDGC4I36mNY9VMC6YZTrWXA"
try:
    bot = telebot.TeleBot(token)
except Exception:
    token = input(f'{Fore.WHITE}{Style.BRIGHT} TOKEN INVALID, TRY AGAIN: ')
    bot = telebot.TeleBot(token)

print(f'{Fore.BLUE}--------------------------------------------------')
chat_id = "5583353259"
os.system('clear')


class S1:
    def __init__(self):
        self.success = 0
        self.retry = 0
        self.failed = 0
        self.accounts = []
#لاتصير قحبون وتخمط
    def create_account(self):

        username = choice("qwertyuioasdfghjklzxcvbnpm1234567890") + "".join(
            choices(list("qwertyuioasdfghjklzxcvbnpm1234567890"), k=17)
        )

        try:

            con = create_connection(
                "wss://51.79.208.190:8080/Reg",
                header=[
                    "app: com.safeum.android",
                    "host: None",
                    "remoteIp: 51.79.208.190",
                    "remotePort: 8080",
                    "sessionId: None",
                    "time: 2024-04-11 11:00:00",
                    "url: wss://51.79.208.190:8080/Reg",
                ],
                sslopt={"cert_reqs": CERT_NONE},
            )


            con.send(dumps({"action":"Register","subaction":"Desktop","locale":"ar_IQ","gmt":"+03","password":{"m1x":"a8853033eb579da7c476af0cd969703191346572df52f77469cded4b68e00fbf","m1y":"510324aa56626d65db05b26c6f8427e00c826db193af7ffebefc3ce0806f7185","m2":"83997dd64fb1871c880be11533df8d339c22c5d2f3601e20254d73cdf12e7d89","iv":"7a221afb04b1f89f8b1c78a9de701dff","message":"6764adee6b95aeef9f5b8972cb64d9d6d054ac10cbbc89b134d2f9674f28b86331116d6861d048917e551fe21554be63d214248f836ab7a421bf95847dc9746451b7529a334d74062de4073048356a3e"},"magicword":{"m1x":"d6e1614068a4b1194e95968470f8e54fcc0185f8ba456ab16647736dd1549ec4","m1y":"6b7300b694759f721cfd9304a8327dd80029a62f716f99943aeee71133ca64ff","m2":"357e1e609811702fe313319a023b1266992da682e4cbf6955d204db0a9d7905d","iv":"8f124da0cdee56983277038c65e2e446","message":"9030781e842d41ae8226a8c1c14a215f"},"magicwordhint":"0000","login":str(username),"devicename":"Realme RMX3269","softwareversion":"1.1.0.1640","nickname":"hrhejjeghrbjrrbtjej","os":"AND","deviceuid":"f7a88f3e39abf27a","devicepushuid":"*cME2FmjeSj6-869LtFwnwI:APA91bGyMZ_7-tmCzlep7Fz_mWJ9AnTimC83urrBkFMXxTpZhD7Q2xBpUc4DFJIUcKzfzI9H5SqZ0_sY36rc1QJd61kprv7iHSyHtELbuPVTPBbdE75qqs6eTaCoBpmRL_i6RTZEYbFF","osversion":"and_11.0.0","id":"2142419123"}))

            response = decompress(con.recv()).decode("utf-8")


            if '"status":"Success"' in response:
                self.success += 1
                self.accounts.append(username)
                with open('users.txt', 'a') as file:
                    file.write(username + "\n")
                bot.send_message(chat_id, f"<strong> <code>{username}</code> </strong>", parse_mode="html")
            else:
                self.failed += 1

        except Exception:
            self.retry += 1



s1_tool = S1()


executor = ThreadPoolExecutor(max_workers=1000)

while True:
    executor.submit(s1_tool.create_account)


    os.system('clear')
    print(f'''
{Fore.BLUE}--------------------------------------------------
      {Fore.GREEN}Welcome to the {Fore.YELLOW}S1{Fore.GREEN} Tool    
            {Fore.CYAN}Tool RUNNING
       {Fore.MAGENTA}Developer  :  @jokerpython3
{Fore.BLUE}--------------------------------------------------
    ''')

    print(f"""
    {Fore.GREEN}{Style.BRIGHT}Successful accounts: {s1_tool.success}\n
    {Fore.RED}{Style.BRIGHT}Failed attempts: {s1_tool.failed}\n
    """)
#خمطك اكبر دليل على فشلك
    if s1_tool.success > 0:
    	print("\n", "\n".join([Fore.BLUE + account for account in s1_tool.accounts]))


bot.polling()

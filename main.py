import requests
import json
from colorama import Fore
import os

# User data

pseudo = 'Hisoka'
rank = 'admin'
id = '1'
ban = False

# Token AND Chat ID

bot1 = {
    'token':'2134902146:AAHgCC3vkOatqQaMQuDo5l0h3NxCITHDUl4',
    'chat_id':'-1001648468501'
}

bot2 = {
    'token':'2106470373:AAGDKSr7fD02dI17NqMyjSAdvPAeJljns44',
    'chat_id':'-1001648468501'
}

def get_message():
    url_get = 'https://api.telegram.org/bot' + bot1['token'] + '/getUpdates'
    req = requests.get(url_get).json()
    if req['ok'] == True:
        data_message = req['result']
        for message in data_message:
            try:
                message = json.loads(message['message']['text'])
                rank = message['rank']
                pseudo = message['pseudo']
                msg = message['content']
                id = message['id']
                if rank == "admin":
                    prefix = f'{Fore.LIGHTRED_EX}[ADMIN] {Fore.GREEN} {pseudo} [{id}] : {Fore.WHITE}' + msg
                elif rank == "visitor":
                    prefix = f'{Fore.LIGHTCYAN_EX}[VISITOR] {Fore.GREEN} {pseudo} [{id}] : {Fore.WHITE}' + msg
                else:
                    prefix = f'{Fore.LIGHTYELLOW_EX}[UNKNOW] {Fore.GREEN} {pseudo} [{id}] : {Fore.WHITE}' + msg
                print(prefix)
            except:
                pass

def send_message(message):
    msg = {'id':id,'pseudo':pseudo,'rank':rank,'content':message}
    url_post = f"https://api.telegram.org/bot{bot2['token']}/sendMessage?chat_id={bot1['chat_id']}&text={msg}"
    req = requests.get(url_post).json()
    print(req)

# Check rank

    
if ban != True:
    os.system('cls')
    print('Start chatting with username : ' + pseudo + ' and rank : ' + rank + '\n')
    send_message(input())
    get_message()
    
    
    
    
import requests
import json
from colorama import Fore
import os

# User data (pas de constant parceque c'est dynamique)
user_data = {
    'username': 'Hisokaleskid', # variable name are in english :)
    'rank': 'admin',
    'id': 1,
    'banned': False
}

# Token AND Chat ID (contant :D)
BOTS = [
    {
        'token':'2134902146:AAHgCC3vkOatqQaMQuDo5l0h3NxCITHDUl4',
        'chat_id':'-1001648468501'
    },
    {
        'token':'2106470373:AAGDKSr7fD02dI17NqMyjSAdvPAeJljns44',
        'chat_id':'-1001648468501'
    }
]

def get_message():
    url_get = 'https://api.telegram.org/bot' + BOTS[0]['token'] + '/getUpdates'
    req = requests.get(url_get).json()
    if req['ok'] == True:
        data_message = req['result']
        for message in data_message:
            try:
                message = json.loads(message['message']['text'])
                user_data['rank'] = message['rank']
                user_data['username'] = message['pseudo']
                user_data['id'] = message['id']
                msg = message['content']
                
                if rank == "admin":
                    prefix = f'{Fore.LIGHTRED_EX}[ADMIN] {Fore.GREEN} {user_data['username']} [{user_data['id']}] : {Fore.WHITE}' + msg
                elif rank == "visitor":
                    prefix = f'{Fore.LIGHTCYAN_EX}[VISITOR] {Fore.GREEN} {user_data['username']} [{user_data['id']}] : {Fore.WHITE}' + msg
                else:
                    prefix = f'{Fore.LIGHTYELLOW_EX}[UNKNOW] {Fore.GREEN} {user_data['username']} [{user_data['id']}] : {Fore.WHITE}' + msg
                print(prefix)
            except:
                pass

def send_message(message):
    msg = {'id':id,'pseudo':user_data['username'],'rank':user_data['rank'],'content':message}
    url_post = f"https://api.telegram.org/bot{BOTS[1]['token']}/sendMessage?chat_id={BOTS[0]['chat_id']}&text={msg}"
    req = requests.get(url_post).json()
    print(req)

# Check rank

if __name__ == '__main__':
    if user_data['banned'] != True:
        os.system('cls')
        print('Start chatting with username : ' + user_data['username'] + ' and rank : ' + user_data['rank'] + '\n')
        send_message(input())
        get_message()
    
    
    
    

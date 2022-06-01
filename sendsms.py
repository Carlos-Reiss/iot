import telebot 
from telethon.sync import TelegramClient 
from telethon.tl.types import InputPeerUser, InputPeerChannel 
from telethon import TelegramClient, sync, events 
  
def sendSMS(message, usuario):
    api_id = '18949729'
    api_hash = '9ccc0a5a83b3538d00bfa70a5bc67032'
    bot_token = '5507411579:AAFMC1ShEo7Ii2Akir1xcvruR3Ey32nZSs8'
    phone = '5581992614885'
    client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
    
    if not client.is_user_authorized(): 
        client.send_code_request(phone) 
        client.sign_in(phone, input('Enter the code: ')) 
    
    try: 
        receiver = client.get_entity(usuario)
        client.send_message(receiver, message, parse_mode='html') 
    except Exception as e: 
        print(e); 
    client.disconnect() 
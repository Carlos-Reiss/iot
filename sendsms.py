import requests
import os
from dotenv import load_dotenv

def send_telegram_message(message):

    # Carrega as variáveis de ambiente
    load_dotenv()

    # Pega o token do bot e o id do chat a partir das variáveis de ambiente
    bot_token = os.getenv('bot_token')
    chat_id = os.getenv('chat_id')

    try:

        # Monta e envia um POST request à uma API do telegram
        data = {"chat_id": chat_id, "text":message}
        url = "https://api.telegram.org/bot{}/sendMessage".format(bot_token)
        requests.post(url,data)

    except Exception as e:
        print("[!] Erro ao enviar a mensagem: ", e)
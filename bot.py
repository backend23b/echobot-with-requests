import requests
import time
from settings import TOKEN

URL = f'https://api.telegram.org/bot{TOKEN}'

def get_last_update():
    url = f'{URL}/getUpdates'

    response = requests.get(url=url)
    if response.status_code == 200:
        data = response.json()

        updates = data['result']

        if len(updates) != 0: return updates[-1]


def get_data_from_last_update(update: dict) -> tuple:
    update_id = update['update_id']
    chat_id = update['message']['chat']['id']
    text = update['message']['text']

    return update_id, chat_id, text


def send_message(chat_id, text):
    url = f'{URL}/sendMessage'

    payload = {"chat_id": chat_id, "text": text}
    response = requests.get(url=url, params=payload)

    return response.status_code

last_update = get_last_update()

last_update_id = get_data_from_last_update(last_update)[0]

while True:
    
    current_update = get_last_update()

    current_update_id, chat_id, text = get_data_from_last_update(current_update)

    if last_update_id != current_update_id:
        sc = send_message(chat_id, text)
        print(sc)

        last_update_id = current_update_id

    time.sleep(1)
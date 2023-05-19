import requests 
from settings import TOKEN


URL = f'https://api.telegram.org/bot{TOKEN}'


def send_contact(chat_id, phone_number, first_name, last_name=''):
    url = f'{URL}/sendContact'

    payload = {
        "chat_id": chat_id,
        "phone_number": phone_number,
        "first_name": first_name,
        "last_name": last_name,
    }
    requests.get(url=url, params=payload)

def send_dice(chat_id, emoji):
    url = f'{URL}/sendDice'

    payload = {
        "chat_id": chat_id,
        "emoji": emoji,
    }
    requests.get(url=url, params=payload)

# send_contact(chat_id='1258594598', phone_number='+998883277733', first_name='Diyorbek', last_name='Jumanov')
# send_dice('1258594598', '🎲')
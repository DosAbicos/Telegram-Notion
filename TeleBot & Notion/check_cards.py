from utils import DATABASE_ID, NOTION_TOKEN, url, headers
import requests
from send_message import send_telegram_message, send_telegram_message_with_url

sent_cards = {}

def get_all_cards():
    response = requests.post(url, headers=headers)
    data = response.json()
    return data.get('results', [])

def check_and_send_new_cards():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2021-05-13"
    }

    response = requests.post(url, headers=headers)
    data = response.json()

    if 'results' in data:
        for item in data['results']:
            card_id = item['id']
            props = item["properties"]
            if 'Status' in props and 'select' in props['Status']:
                status = props['Status']['select']['name']
                card_title = props['URL']['title'][0]['text']['content']
                print(f"Card '{card_title}' has status: '{status}'")  # Debug print
                if status == "To do" or status == "Done":
                    if card_id in sent_cards:
                        # Если карточка уже отправлена, обновляем ее статус в словаре
                        if sent_cards[card_id] != status:
                            send_telegram_message(f"📌Статус карточки '{card_title}' изменен на '{status}'!")
                            sent_cards[card_id] = status
                    else:
                        send_telegram_message(f"📌Карточка '{card_title}' перемещена в статус '{status}'!")
                        sent_cards[card_id] = status
                else:
                    # Если статус карточки не "New", отправляем уведомление
                    if card_id not in sent_cards:
                        send_telegram_message_with_url(card_title, item['url'])
                        sent_cards[card_id] = status
                    else:
                        # Если карточка была отправлена и возвращена обратно в статус "New", также отправляем уведомление
                        if sent_cards[card_id] != status:
                            send_telegram_message_with_url(card_title, item['url'])
                            sent_cards[card_id] = status
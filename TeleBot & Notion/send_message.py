from utils import bot, bot_chat_id
import datetime
import check_cards


def send_telegram_message(message):
    bot.send_message(bot_chat_id, message, parse_mode="HTML") 

def send_telegram_message_with_url(title, url):
    message = f"📢<b>Новая карточка в Notion: <a href='{url}'>{title}</a></b>"
    bot.send_message(bot_chat_id, message, parse_mode="HTML")

def send_all_cards_daily():
    now = datetime.datetime.now()
    # Укажите желаемое время для отправки карточек
    target_time = datetime.time(hour=20, minute=00)  # Например, 9:10 утра
    if now.time().hour == target_time.hour and now.time().minute == target_time.minute:
        all_cards = check_cards.get_all_cards()
        if all_cards:
            # Сортируем карточки по статусу
            sorted_cards = {"New": [], "To do": [], "Done": []}
            for item in all_cards:
                card_title = item["properties"]["URL"]["title"][0]["text"]["content"]
                card_status = item["properties"]["Status"]["select"]["name"]
                card_url = item["url"]
                # Добавляем карточку в соответствующий список в зависимости от статуса
                sorted_cards[card_status].append((card_title, card_url))

            message = "<b>📋Подытожим сегоднешний день:</b>\n\n"
            # Добавляем карточки каждого статуса в сообщение
            for status, cards in sorted_cards.items():
                # Определение смайлика для статуса
                emoji = ""
                if status == "New":
                    emoji = "🟥"
                elif status == "To do":
                    emoji = "🟧"
                elif status == "Done":
                    emoji = "🟩"

                if cards:
                    message += f"<b>{emoji} {status}:</b>\n"
                    for card_title, card_url in cards:
                        message += f"<a href='{card_url}'>{card_title}</a>\n"
                    message += "\n"

            send_telegram_message(message)

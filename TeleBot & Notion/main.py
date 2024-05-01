from check_cards import check_and_send_new_cards
from send_message import send_all_cards_daily

import time

# Основной цикл программы
while True:
    # Проверяем и отправляем новые карточки
    check_and_send_new_cards()
    # Отправляем все карточки в определенное время каждый день
    send_all_cards_daily()
    # Проверяем каждую минуту
    time.sleep(60)

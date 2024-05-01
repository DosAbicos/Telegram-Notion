import telebot

bot_token = "6888109357:AAGjhio4OBZ3_YoEOSVOfl0UGiMn1t6T20A"
bot = telebot.TeleBot(bot_token)
bot_chat_id = "-4147844552"

NOTION_TOKEN = "secret_XSt8ap2cMAJdzPTN8q0keJTgTruaUGr6UMlKV9gp4zk"
DATABASE_ID = "7d56f5a628dd452882666b62f19da6c7"

url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}
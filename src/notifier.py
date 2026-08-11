import os
import requests
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]

def send_notification(message):
    payload = {"content": message}
    response = requests.post(WEBHOOK_URL, json=payload)
    response.raise_for_status()

if __name__ == "__main__":
    send_notification("テスト通知です。Botの設定は正常に動いています。")
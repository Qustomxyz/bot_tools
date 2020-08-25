#!/usr/bin/env python

import os
from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv()

link_hook = f"https://api.telegram.org/bot{os.getenv('TOKEN')}/getWebhookInfo"
webhook_info = requests.get(link_hook)
print(webhook_info.json())

print(datetime.fromtimestamp(webhook_info.json()['result']['last_error_date']))

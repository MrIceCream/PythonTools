#!/usr/bin/env python3
# encoding=utf-8
import json
import hashlib
import base64
import hmac
import time
import requests
from urllib.parse import quote_plus
import schedule
import datetime
import random_ball

# 测试用
url = 'https://oapi.dingtalk.com/robot/send?access_token=6763e8f08215f682912d9304a5961b56ea4e55d5697080923c7cde1011ce01e2'
secret = 'SEC56cb7cac3351c466a343ed17ac167eb420b0aa36764dd3edf9386991b0abbfd9'
# 程序一组
# url = 'https://oapi.dingtalk.com/robot/send?access_token=7b2ea9abb6fc36b45996bff584da55f4546d604fdaab3855c289d66aab8a9d63'
# secret = 'SEC4dc2296e76dc988f0a795623624ac148b05e58d41533420fb9c373762b8b5fc7'

secret_enc = secret.encode('utf-8')
timestamp = str(round(time.time() * 1000))
string_to_sign = f'{timestamp}\n{secret}'
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = quote_plus(base64.b64encode(hmac_code))


def send_message(text):
    headers = {'Content-Type': 'application/json'}
    webhook = f'{url}&timestamp={timestamp}&sign={sign}'
    data = {
        "msgtype": "text",
        "at": {
            "isAtAll": True
        },
        "text": {
            "content": text
        }
    }
    value = json.dumps(data)
    with requests.post(webhook, value, headers=headers) as r:
        return r.text


def send_notification():
    # 获取当前时间
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text = f"https://docs.qq.com/sheet/DYnRrcmFNQlp0R3d6\n人员进度表更新。\n通知时间:{current_time}\n"
    response = send_message(text)
    print(response)

send_notification()

# # 定义定时任务
# schedule.every().day.at("11:32").do(send_notification)
# schedule.every().day.at("17:55").do(send_notification)

# while True:
#     # 运行待定的定时任务
#     schedule.run_pending()
#     time.sleep(1)
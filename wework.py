import os
import requests
import json

def send_wework_message(content, msg_type="markdown"):
    webhook = os.getenv("WEWORK_WEBHOOK")
    msg_type = os.getenv("WEWORK_MSG_TYPE", msg_type)

    if not webhook:
        raise ValueError("WEWORK_WEBHOOK is not set")

    if msg_type == "markdown":
        payload = {
            "msgtype": "markdown",
            "markdown": {
                "content": content
            }
        }

    elif msg_type == "text":
        payload = {
            "msgtype": "text",
            "text": {
                "content": content
            }
        }

    elif msg_type == "news":
        payload = {
            "msgtype": "news",
            "news": {
                "articles": [
                    {
                        "title": "GitHub Trending 更新",
                        "description": content,
                        "url": "https://github.com/trending",
                        "picurl": ""
                    }
                ]
            }
        }

    elif msg_type == "template_card":
        payload = {
            "msgtype": "template_card",
            "template_card": {
                "card_type": "text_notice",
                "source": {
                    "desc": "GitHub Trending 推送"
                },
                "main_title": {
                    "title": "📌 Trending 更新",
                    "desc": content
                },
                "emphasis_content": {
                    "title": "查看详情",
                    "desc": "GitHub Trending"
                },
                "horizontal_content_list": [],
                "jump_list": [
                    {
                        "type": 1,
                        "url": "https://github.com/trending",
                        "title": "打开 Trending"
                    }
                ]
            }
        }

    else:
        raise ValueError("Unsupported message type")

    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook, data=json.dumps(payload), headers=headers)
    return response.text

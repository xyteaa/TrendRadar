def send_wework_news(webhook, title, description, url, image_url):
    payload = {
        "msgtype": "news",
        "news": {
            "articles": [
                {
                    "title": title,
                    "description": description,
                    "url": url,
                    "picurl": image_url
                }
            ]
        }
    }
    requests.post(webhook, json=payload)

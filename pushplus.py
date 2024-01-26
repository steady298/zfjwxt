import requests
import json
import os


def send_message(title, content):
    token = os.environ.get("TOKEN")
    url = "http://www.pushplus.plus/send"
    data = {"token": token, "title": title, "content": content}
    body = json.dumps(data).encode(encoding="utf-8")
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=body, headers=headers)
    url2 = "https://api2.pushdeer.com/message/push?pushkey=PDU17847TVfsWnjMpHXpdNzagjSoDuFfFIQH4SePm&text=教务成绩有更新&desp=" + "body" + "&type=markdown"
    requests.get(url2)
    return response.text

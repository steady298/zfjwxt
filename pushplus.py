import requests
import json
import os
import urllib.parse
import urllib.request

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



def pushdeer_send(text='教务系统有更新', desp='教务系统有更新', type='markdown', key='PDU17847TVfsWnjMpHXpdNzagjSoDuFfFIQH4SePm'):
    data = urllib.parse.urlencode({'text': text, 'desp': desp, 'type': type, 'pushkey': key})
    data = data.encode('utf-8')
    
    url = 'https://api2.pushdeer.com/message/push'
    req = urllib.request.Request(url, data)
    
    with urllib.request.urlopen(req) as response:
        result = response.read()
        return result.decode('utf-8')

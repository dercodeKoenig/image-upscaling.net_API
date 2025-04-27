import requests
import json

API_ROOT = "https://image-upscaling.net/online_tts/"
client_id = "57dbf311771d385c7ee7ca3bc8ac4c66"


def submit(client_id, text, voice, speed=1.0):
    url = API_ROOT + 'submit.php'
    cookies = {'client_id': client_id}
    payload = {'text': text, 'voice': voice, 'speed': speed}
    headers = {'Content-Type': 'application/json', 'Origin': API_ROOT}
    r = requests.post(url, json=payload, cookies=cookies, headers=headers)
    r.raise_for_status()
    return r.json()

def get_status(client_id):
    cookies = {'client_id': client_id}
    url = API_ROOT + 'get_texts.php'
    r = requests.get(url, cookies=cookies)
    r.raise_for_status()
    response = []
    for request in r.json()["requests"]:
        output = request["output_path"]
        if output != "":
            output = API_ROOT+"data/"+output
        response.append(([request["req_id"], output]))
    return response

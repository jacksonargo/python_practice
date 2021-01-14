import json  # https://docs.python.org/3/library/json.html

import requests  # https://requests.readthedocs.io/en/latest/user/quickstart/


def translate(text):
    # https://libretranslate.com/docs/
    r = requests.post("https://libretranslate.com/translate", params={"q": text, "source": "en", "target": "es"})
    r.raise_for_status()
    return json.loads(r.text)["translatedText"]


def foaas():
    r = requests.get("https://foaas.com/cup/jackson", headers={"Accept": "application/json"})
    r.raise_for_status()
    payload = json.loads(r.text)
    return translate(payload["message"]) + "\n" + payload["subtitle"]


print(foaas())

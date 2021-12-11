import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)

news = []
for elem in root.iter():
    if elem.tag == 'item':
        news.append({'author': elem.find('author').text,
                    'category': elem.find('category').text,
                    'description': elem.find('description').text,
                    'enclosure': elem.find('enclosure').text,
                    'guid': elem.find('guid').text,
                    'link': elem.find('link').text,
                    'pubDate': elem.find('pubDate').text,
                    'title': elem.find('title').text})

with open('news.json', 'w', encoding="utf-8") as fp:
    json.dump(news, fp, ensure_ascii=False)
from urllib.request import urlopen
from json import loads
from itertools import groupby
from urllib.parse import quote

url = "https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=" + quote('Бельмондо,_Жан-Поль')
data = loads(urlopen(url).read().decode('utf8'))
revisions = data['query']['pages']['192203']['revisions']
revisions_counter = {}
for key, group in groupby(revisions, lambda x: x['timestamp'][0:10]):
    revisions_count = 0
    for thing in group:
        revisions_count += 1
    revisions_counter[key] = revisions_count
print(max(revisions_counter, key=revisions_counter.get))
import requests
from bs4 import BeautifulSoup
user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
headers = {'User-Agent' : user_agent}

r = requests.get('http://www.baidu.com/', headers = headers)
# with open('requests.html', 'w', encoding='utf8') as f:
#     f.write(r.text)
soup = BeautifulSoup(r.text, features="html.parser")
print(soup.title.get_text())
# print(soup.p.string)
texts = soup.find_all('a')
for text in texts:
    hotsearch = text.find_all('span')
    if len(hotsearch) == 2:
      print(hotsearch[0].string + '：' + hotsearch[1].string)
      print(text.get('href'))
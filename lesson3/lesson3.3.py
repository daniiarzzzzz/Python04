import bs4
import requests

html = requests.get("https://24.kg/")

# print(html.content)

bs = bs4.BeautifulSoup(str(html.content, encoding='utf-8'), 'html.parser')

news_list = bs.find_all('div', class_='one')

for i in news_list:
    print(i.text)


print(news_list)

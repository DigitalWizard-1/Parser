import requests
import bs4

def get_hubs(pie):
    hubs = pie.find_all('a', class_="tm-article-snippet__hubs-item-link")
    hubs = [hub.find('span').text for hub in hubs]
    return hubs

def habr_text(text):
    soup = bs4.BeautifulSoup(text, features='html.parser')
    articles = soup.find_all('article')

    for article in articles:
        hubs = get_hubs(article)
        title = article.find('h2')
        tag = title.find('a')
        href = tag.attrs['href']
        url = 'https://habr.com' + href
        article_date = article.find('time').attrs['title']

        tmp = str(article.find_all('div', class_="article-formatted-body"))

        flag = 0
        for id in KEYWORDS:
            if tmp.find(id) > 0:
                flag += 1

        if flag > 0:
            print(article_date)
            print(title.text)
            # print(hubs)
            print(url)
            print()


HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'DNT': '1',
           'Host': 'habr.com',
           'Sec-Fetch-Dest': 'document',
           'Sec-Fetch-Mode': 'navigate',
           'Sec-Fetch-Site': 'none',
           'Sec-Fetch-User': '?1',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'
}

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'MobX', 'Хабр', 'NFT']

if __name__ == '__main__':
  response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
  response.raise_for_status()
  text = response.text
  habr_text(text)


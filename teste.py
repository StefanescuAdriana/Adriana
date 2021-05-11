from bs4 import BeautifulSoup
import requests
import re

def get_html(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify())

    for article in soup.find_all('article'):
        headline = article.h3.a.text
        print(headline)

        try: summary = article.find('div', class_='col-md-8 post-content').p.text
        except Exception as e:
            summary = None
        print(summary)

        links = []
        for news in article.findAll('h3', {'class': 'post-title'}):
            links.append(news.a['href'])
        print("Link-ul este: ", links)

        try: date = article.find('div', class_='col-lg-10 col-md-9 col-sm-8').text
        except Exception as e:
            date = None
        print(date)


get_html("https://www.calitateaer.ro/public/alerts-and-news/?__locale=ro")

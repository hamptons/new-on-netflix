import email_handler
from app_url_opener import AppURLopener
from custom_date_builder import CustomDateBuilder
from bs4 import BeautifulSoup

opener = AppURLopener()
page = opener.open('https://uk.newonnetflix.info/')
soup = BeautifulSoup(page, 'lxml')
wrapper = soup.find('div', attrs={'class': 'wrapper'})

elements = wrapper.findAll('article', limit=None)

date_builder = CustomDateBuilder()
date_text = 'Added to UK Netflix: ' + date_builder.build_date()
films = []
tv_shows = []
for element in elements:
    website_date_text = element.findAll('p')[4].get_text()
    if website_date_text == date_text:
        title = element.header.h1.a.get_text()
        duration = element.findAll('p')[7].get_text()
        if 'season' not in duration.lower():
            films.append(title)
        else:
            tv_shows.append(title)

email_handler.send_email(
    date_text,
    films,
    tv_shows)

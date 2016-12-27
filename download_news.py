from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import time
import sqlite3 
import re
from datetime import datetime

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
#c.execute('''CREATE TABLE IF NOT EXISTS news
#		(company_id text, dtime datetime, news text, news_url text UNIQUE)''')

def scraping_data():
    news_list= []
    news_adress_list = []
    company_link_list = []

    base_domain = r'http://www.e-disclosure.ru/'
    r = urlopen(base_domain)
    soup = bs(r, 'html.parser')

    for a in soup.select('[class*=live] a[href*="www.e-disclosure.ru/portal/event.aspx?"]'):
        news_list.append(a.get_text())
    for a in soup.select('[class*=live] a[href*="www.e-disclosure.ru/portal/event.aspx?"]'):
        news_adress_list.append(a.get('href'))
    for a in soup.select('[class*=live] a[href*="www.e-disclosure.ru/portal/company.aspx?"]'):
        company_link_list.append(re.sub("[^0-9]","", a.get('href')[-6:]))

    for i in range(len(company_link_list)):
    	c.execute("INSERT OR IGNORE INTO news_newsfeed (company_id, added_at, news_short, news_url) VALUES (?,?,?,?)",(company_link_list[i],datetime.now(),news_list[i],news_adress_list[i]))
    conn.commit()
    time.sleep(30)

def inf_scraping():
    while True:
        scraping_data()

inf_scraping()
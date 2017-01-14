from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import time
import sqlite3 
import re
from datetime import datetime

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS news
		(company_id text, dtime datetime, news text, news_url text UNIQUE)''')

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

# companies = []
# companies2 = []
#
#
# with open('emitents.csv', 'r') as file:
#     for row in file:
#         companies.append([row])
#
# for i in companies:
#     for b in i:
#         companies2.append(b.split(';'))
#
# companies_final = companies2[1:]
#
# c.execute('''CREATE TABLE IF NOT EXISTS companies_companies
#     (company_id INTEGER UNIQUE, ticker TEXT, company_full_name TEXT, company_short_name TEXT, official_site TEXT, ceo TEXT, industry TEXT, company_description TEXT)''')
#
# for i in companies_final:
#     data = (i[0], i[1], i[2] ,i[4] ,i[5] ,i[6] ,i[7] ,i[8])
#     c.execute("INSERT INTO companies_companies (company_id,ticker,company_full_name,company_short_name,official_site,ceo,industry,company_description) VALUES (?,?,?,?,?,?,?,?)", data)
#     conn.commit()
#
# c.close()

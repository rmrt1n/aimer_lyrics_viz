# import packages
import requests
from bs4 import BeautifulSoup
import re
import csv
import time


# functions
def regex(lyrics):
    ''' regex to clean scraped lyrics '''
    lyrics = ''.join(lyrics) 
    lyrics = re.sub('\[.*?\]', '', lyrics)
    lyrics = re.sub(r'[^\w\s]', '', lyrics)
    lyrics = re.sub('([a-z])([A-Z])', r'\1 \2', lyrics)

    res = {}
    for i in lyrics.lower().split():
        if i not in res:
            res[i] = 1
        else:
            res[i] += 1
    return res

def parse(url):
    ''' takes url as an argument and returns a dictionary of words and their count '''
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    # page structure in genius.com pages are inconsistent. the lyrics are in different tags.
    if soup.find('div', class_='Lyrics__Container-sc-1ynbvzw-2 jgQsqn') is not None: 
        lyrics = [i.text for i in soup.find_all('div', class_='Lyrics__Container-sc-1ynbvzw-2 jgQsqn')]
        result = regex(lyrics)
        return result
    elif soup.find('div', class_='Lyrics__Container-sc-1ynbvzw-2 jgQsqn') is None: 
        if soup.find('p') is not None:
            lyrics = soup.find('p').text
            result = regex(lyrics)
            return result
        else:
            print('unable to scrape ' + url)

def append_rows():
    ''' appends words and their count from dict along with song title to a list  '''
    for i in resp['songs']:
        url = i['url']
        title = i['title']

        words = parse(url)
        # only append scraped data
        if words is not None:
            rows = [[key, value] for key, value in words.items()]
            for row in rows:
                row.insert(0, title)
                l.append(row)


# fake ajax request
l = [] 
n_page = 1
api_url = 'https://genius.com/api/artists/1044826/songs?page='

while True:
    print('sending get request to ' + api_url + str(n_page))
    resp = requests.get(api_url + str(n_page)).json()['response']

    if resp['next_page'] is not None:
        append_rows()
        print('scraping lyrics...')
        n_page += 1
        time.sleep(2)
    else:
        append_rows()
        break


# write to csv
with open('data/scraped_data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Song_title', 'Word', 'Count'])
    writer.writerows(l)


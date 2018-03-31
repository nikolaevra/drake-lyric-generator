import urllib.request as urllib2
from bs4 import BeautifulSoup
import pandas as pd

quote_page = 'http://metrolyrics.com/{}-lyrics-drake.html'
filename = 'drake-songs.csv'
songs = pd.read_csv(filename)

for index, row in songs.iterrows():
    page = urllib2.urlopen(quote_page.format(row['song']))
    soup = BeautifulSoup(page, 'html.parser')
    verses = soup.find_all('p', attrs={'class': 'verse'})

    lyrics = ''

    for verse in verses:
        lyrics = lyrics + verse.text.strip().replace('\n', ' ')

    songs.at[index, 'lyrics'] = lyrics

    print('saving {}'.format(row['song']))
    songs.head()

print('writing to csv')
songs.to_csv(filename, sep=',', encoding='utf-8')

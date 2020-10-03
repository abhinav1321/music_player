from bs4 import BeautifulSoup as bs
import requests
from fuzzywuzzy import fuzz

url ='http://www.radiomirchi.com/more/mirchi-top-20/'

response = requests.get(url)
soup = bs(response.text, 'html.parser')

pagewrap = soup.findAll('div', {'class': 'pagewrap'})

top01 = pagewrap[0].findAll('article', {'class': 'top01'})

panel_list = []

for t in top01:
    panel = t.findAll('div', {'class': 'pannel02'})
    panel_list.append(panel)

song_list = []
for panel in panel_list:
    song_name = panel[0].findAll('h2')
    description = panel[0].findAll('h3')[0].text.strip()
    song_list.append((song_name[0].text.strip(), description))


def top_songs():
    return song_list[0:10]


def download():
    for s in song_list:
        try:
            print(s, ' : search for')
            site_url = 'https://mp3pk.com/search?q='
            song_to_search = s[0].replace(' ', '+')
            new_url = site_url+song_to_search
            print(new_url, 'as new url')
            search_response = requests.get(new_url)
            search_soup = bs(search_response.text, 'html.parser')
            content = search_soup.findAll('section', {'class', 'container site-wrapper'})
            body_wrapper = content[0].findAll('main', {'class', 'body-wrapper'})
            archive_body = body_wrapper[0].findAll('div', {'class', 'archive-body'})
            figure = archive_body[0].findAll('figure', {'class', 'col-md-12 thumb-vertical'})
            link = figure[0].findAll('a', href=True)[0]['href']
            new_url = site_url+link
            search_resp = requests.get(new_url)
            search_soup = bs(search_resp.text, 'html.parser')
            # content = search_soup.findAll('main', {'class', 'body-wrapper'})
            # content_wrapper = content[0].findAll('content')
            # page_zip_wrap = content_wrapper[0].findAll('div', {'class', 'page-zip-wrap'})
            cat_wrap = search_soup.findAll('div', {'class', 'single-songs list-group page-cat-wrap'})
            # print('cat_wrap',cat_wrap)
            fig_caption = cat_wrap[0].findAll('figcaption')
            maximum = 0, ''
            href = ''
            for fig in fig_caption:
                to_fuzz = fig.find('h3').text.split(',')[0].strip()
                ratio = fuzz.ratio(to_fuzz, s[0])
                href = fig.find('h3').find('a')['href']
                # print('href as',href)
                if ratio > maximum[0]:
                    maximum = ratio, href
            download_href = 'https://mp3pk.com' + str(href)
            print(download_href)
            try:
                song_req = requests.get(download_href)
                soup = bs(song_req.text, 'html.parser')
                song = requests.get(soup.findAll('div', {'class', 'page-zip-wrap'})[0].findAll('a')[1]['href'])
                with open(str(s[0])+'.mp3', 'wb') as file:
                    print('writing ', str(s[0]))
                    file.write(song.content)
            except:
                pass
        except:
            pass



from bs4 import BeautifulSoup as bs
import requests

print('1')

url ='http://www.radiomirchi.com/more/mirchi-top-20/'

response = requests.get(url)
soup = bs(response.text,'html.parser')

pagewrap=soup.findAll('div',{'class':'pagewrap'})

top01=pagewrap[0].findAll('article',{'class':'top01'})

panel_list=[]
for t in top01:
    panel=t.findAll('div',{'class':'pannel02'})
    panel_list.append(panel)

song_list=[]
for panel in panel_list:
    song_name=panel[0].findAll('h2')
    description=panel[0].findAll('h3')[0].text.strip()
    song_list.append((song_name[0].text.strip(),description))


def top_songs():
    return song_list


def download(song_to_search):
    print(song_to_search)
    site_url = 'https://mp3pk.com/search?q='
    song_to_search = song_to_search.replace(' ', '+')
    new_url = site_url+song_to_search
    print(new_url)
    search_response = requests.get(new_url)
    search_soup = bs(search_response.text, 'html.parser')
    content = search_soup.findAll('section', {'class', 'container site-wrapper'})
    body_wrapper = content[0].findAll('main', {'class', 'body-wrapper'})
    archive_body = body_wrapper[0].findAll('div', {'class','archive-body'})
    figure = archive_body[0].findAll('figure', {'class', 'col-md-12 thumb-vertical'})
    link=figure[0].findAll('a',href=True)[0]['href']
    new_url=site_url+link
    search_resp = requests.get(new_url)
    search_soup= bs(search_resp.text, 'html.parser')
    content = search_soup.findAll('main', {'class', 'body-wrapper'})
    content_wrapper = content[0].findAll('content')
    # print(content_wrapper[0].findAll('div',{'class', 'page-zip-wrap'}))
    # print(content[0])

from bs4 import BeautifulSoup
import requests
import csv

# with open('simple.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')

# print(soup.find('div', class_='footer'))
# for article in soup.find_all('div', class_='article'):
#     print(article.h2.a.text)
csv_file = open('scarpe.csv','w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video_link'])

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')
articles = soup.find_all('article')
# print(article.prettify())
for article in articles:
    headline = article.h2.a.text
    print(headline)
    summary = article.find('div', class_='entry-content').p.text
    print(summary)
    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4].split('?')[0]
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except TypeError:
        yt_link = None
    print(yt_link)
    print()
    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
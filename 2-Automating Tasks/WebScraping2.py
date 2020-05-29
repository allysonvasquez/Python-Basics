# author: Allyson Vasquez
# version: May.28.2020
# Practice: web scraping on actual website, creates cms_scrape.csv
# https://coreyms.com
# https://youtu.be/ng2o98k983k

# Scrapes page of header, descriptions & youtube videos, saves to csv file

from bs4 import BeautifulSoup
import requests
import csv

# Get source code using requests library
source = requests.get('http://coreyms.com').text
# Pass source code into beautiful soup
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

# create CSV file to write information to
csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Summary', 'Video Link'])  # creates top row of excel table

# looping through all video information
for article in soup.find_all('article'):
    try:
        # get title
        headline = article.header.h2.a.text
        print(headline)
        # get video description
        summary = article.find('div', class_='entry-content').p.text
        print(summary)


        # Parse down article to find youtube link
        vid_src = article.find('iframe', class_='youtube-player')['src']
        # print(vid_src)
        vid_id = vid_src.split('/')[4]  # parsing down to find video ID
        vid_id = vid_id.split('?')[0]  # will return the video ID
        # print(vid_id)

        # creating our own yt link using the parsed video ID
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except:
        yt_link = None  # if there is no video for a specific post

    print(yt_link)
    print()

    csv_writer.writerow([headline, summary, yt_link])  # write information to csv file

csv_file.close()
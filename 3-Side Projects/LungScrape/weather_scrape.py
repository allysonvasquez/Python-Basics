"""
author: Allyson Vasquez
version: July.3.2020
"""

from bs4 import BeautifulSoup
import requests, csv

csv_header = []
weather_info = []

# Retrieve page
url = 'https://weather.com/weather/today/l/34.9191,-80.7283'
source = requests.get(url)
soup = BeautifulSoup(source.content, 'lxml')


# Get header titles for CSV file
for title in soup.find_all("div", {"data-testid": "WeatherDetailsLabel"}):
    item = str(title.text)
    csv_header.append(item)
csv_header.pop()
csv_header[0] = 'High'
csv_header.append('Air Quality Index')


# Create csv to write information
csv_file = open('weather_info.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(csv_header)


# Scrape & write information 
i = 1
for info in soup.find_all("div", {"class":"_-_-components-src-molecule-WeatherDetailsListItem-WeatherDetailsListItem--wxData--kK35q"}):
    if i < 8: # Exludes the moon-phase info
        weather_info.append(info.span.text.encode('utf-8'))
    i+=1
weather_info.append(soup.find('text', {"data-testid": "DonutChartValue"}).text)
csv_writer.writerow(weather_info)
csv_file.close()
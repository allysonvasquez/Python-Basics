# author: Allyson Vasquez
# Date: May.29.2020
# Scrapes easy breakfast recipe article and saves data to csv file
# Website used: https://www.allrecipes.com

# import the stuffs
from bs4 import BeautifulSoup
import requests
import csv

# retrieve page using requests library
url = 'https://www.allrecipes.com/gallery/easy-egg-breakfast/'
source = requests.get(url)

# get html of page
soup = BeautifulSoup(source.content, 'lxml')
# print(soup.prettify())  # outputs parsed html

# create csv file to hold recipes
csv_file = open('recipe_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Recipe', 'Summary', 'Recipe Link'])  # creates titles on top row of file

# Scrape data and write into csv file
for recipe in soup.find_all(class_='glide-slide recipe-slide'):
    recipe_title = recipe.h3.text.strip()
    print(recipe_title)

    recipe_summary = recipe.p.text.strip()
    print(recipe_summary)

    recipe_link = recipe.find('a', title="View Recipe").attrs['href']
    print(recipe_link)
    print()

    csv_writer.writerow([recipe_title, recipe_summary, recipe_link])  # write data to csv

csv_file.close()
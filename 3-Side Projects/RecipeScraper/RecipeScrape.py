# author: Allyson Vasquez
# version: May.29.2020
# Scrapes easy breakfast recipe article and saves data to csv file
# Website used: https://www.allrecipes.com

"""
Steps
    -retrieve and get html code of page
    -analyze html to figure out what tags contain the data (hard part!)
    -write data to csv file
"""

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
csv_writer.writerows(['Dish', 'Summary'])


# figure out where all the information is
'''
# Finding first title in page
print('Analyzing First Recipe Title:')
recipe_title = soup.find('h3', class_='glide-slide-title')
recipe_title = recipe_title.text.strip()  # remove whitespaces
print(recipe_title)

# Finding first summary in page
print('Analyzing First Summary:')
recipe_summary = soup.find('div', class_='glide-slide-desc')
print(recipe_summary.p.text)

print()
'''

# TODO: FIX CSV FILE FORMAT!!! (super broken) - put everything in 1 loop
# Loop to collect data
# Now that we know where it is...Scrape all titles
for title in soup.find_all('h3', class_='glide-slide-title'):
    recipe_title = title.text.strip()  # remove whitespaces
    print(recipe_title)
    csv_writer.writerow([recipe_title])  # Write data to csv file

# Scrape all summaries
for summary in soup.find_all('div', class_='glide-slide-desc'):
    recipe_summary = summary.p.text
    print(recipe_summary, '\n')
    csv_writer.writerow([recipe_summary])  # Write data to csv file

csv_file.close()


# TODO: Add recipe link to csv file

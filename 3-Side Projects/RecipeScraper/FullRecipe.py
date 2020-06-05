# author: Allyson Vasquez
# Start Date: May.29.2020
# Scrapes easy breakfast recipe article and saves data to csv file
# Website used: https://www.allrecipes.com

# import the stuffs
from bs4 import BeautifulSoup
import requests
import csv

# retrieve page using requests library
url = 'https://www.allrecipes.com/recipe/187850/egg-in-a-hole/'  # test using eggInaHole
source = requests.get(url)
soup = BeautifulSoup(source.content, 'lxml')  # get html of page

for recipe in soup.find_all('li', class_='checkList__line'):
    print(recipe.prettify())

    #ingredients = recipe.find('span', class_='recipe-ingred_txt added').text
    #ingredients = recipe.find('li', class_='checkList__line').text
    #print(ingredients)

'''
# TODO: ADD FULL RECIPE TO CSV
    # get html of recipe
    source = requests.get(recipe_link)
    linkSoup = BeautifulSoup(source.content, 'lxml')
    for article in linkSoup.find_all('section', class_='ar_recipe_index full-page'):
        print(article)
        # find tags to parse and scrape
        # for ingredients
        #recipe_ingredients = article.find('span', {'class':"recipe-ingred_txt added"}).text
        #print(recipe_ingredients)




    # for instructions

    # csv writerow (replace third element in csv_writer)
'''
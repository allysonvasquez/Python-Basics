# author: Allyson Vasquez
# version: May.15.2020
# Practice: Web Scraping Syntax, uses simple.html
# https://youtu.be/ng2o98k983k

from bs4 import BeautifulSoup
import requests
import lxml

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# prints entire html
print(soup, '\n')

# indents nested tags
print(soup.prettify(), '\n')

# Grab title of web page
match = soup.title
print(match, '\n')

# Grab text only of title tag
match = soup.title.text
print(match, '\n')

# Grab first div
match = soup.div
print(match, '\n')

# Grab div with the class of footer
match = soup.find('div', class_='footer')
print(match, '\n')

# Grab headline
article = soup.find('div', class_='article')
print(article, '\n')

# Grabbing headline & summary of web site
headline = article.h2.a.text
print(headline, '\n')
summary = article.p.text
print(summary, '\n')


# Prints all text in web site
for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)
    summary = article.p.text
    print(summary)

    print()


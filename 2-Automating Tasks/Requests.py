# author: Allyson Vasquez
# version: May.29.2020
# Practice: requests

import requests

# request the url
r = requests.get('http://xkcd.com/353')

# output all accessible attributes & methods
print(dir(r))

# more detail about r object
print(help(r))

# content of response in unicode (html)
print(r.text)


# downloading image from the web site
r = requests.get('https://imgs.xkcd.com/comics/python.png')
print(r.content)  # prints bytes of image

with open('comic.png','wb') as f:  # wb = write bytes
    f.write(r.content)  # writes content of response to file

print(r.status_code)  # 200 = success, 300 = redirect, 400 = client error
print(r.ok)  # prints true for anything under 400
print(r.headers)  # headers that come back with response


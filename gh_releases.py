#!/usr/bin/env python3

import sys
import requests

repo = sys.argv[1] # ie. auth0/auth0-spa-js

url = 'https://api.github.com/repos/' + repo + '/releases'

releases = requests.get(url)

release_list = releases.json()

count = 0

for release in release_list:
    count += 1
    url = release['url']
    name = release['name']
    tag_name = release['tag_name']

    print(tag_name)

    if count >= 3:
        break






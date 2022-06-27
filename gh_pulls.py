#!/usr/bin/env python3

import sys
import requests

repo = sys.argv[1] # ie. octocat/Hello-World

url = 'https://api.github.com/repos/' + repo + '/pulls'


headers = {'Accept': 'application/vnd.github.v3+json'}

pulls = requests.get(url, headers=headers)

pull_list = pulls.json()

count = 0

for pull in pull_list:
    count += 1

    title = pull['title']
    number = pull['number']

    print(title + ' ' + str(number))

    if count >= 3:
        break



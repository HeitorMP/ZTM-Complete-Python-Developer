import requests
from bs4 import BeautifulSoup
import pprint

pages = int(input("Number of pages"))
page_list = []
combined = ""
for index in range(1, pages + 1):
    res = requests.get(f'https://news.ycombinator.com/?p={index}')
    combined += res.text

soup = BeautifulSoup(combined, 'html.parser')

# heads up! .storylink changed to .titleline
links = soup.select('.titleline > a')
subtext = soup.select('.subtext')


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        # href = links[idx].find('a')['href']
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})

    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(links, subtext))

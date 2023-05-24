"""six degrees of kevin bacon"""
import datetime
import logging
import random
import re
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup  # pylint: disable=import-error


class KevinBacon:
    """Six Degrees of Kevin Bacon Class"""

    urlLinks = []

    def make_wikipedia_url(self, article_url: str) -> str:  # noqa: 501 pylint: disable=line-too-long

        """Create Wikipedia compatible string"""
        return f'http://en.wikipedia.org{article_url}'

    def __init__(self, url: str):
        """Initialise class with starting url"""
        self.urlLinks.clear()
        self.url = url
        random.seed(int(round(datetime.datetime.now().timestamp())))

    def get_links(self, article_url):
        """Get links from the wikipedia page"""
        wikiurl = self.make_wikipedia_url(article_url)
        with urlopen(wikiurl) as html:
            logging.debug(wikiurl)
            self.urlLinks.append(wikiurl)
            b_soup = BeautifulSoup(html, 'html.parser')
            return b_soup.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))  # noqa: 501 pylint: disable=line-too-long

    def six_degrees(self) -> int:
        """six degrees mechanism"""
        links = self.get_links(self.url)

        while len(links) > 0 and len(self.urlLinks) < 7:
            new_article = links[random.randint(0, len(links)-1)].attrs['href']
            links = self.get_links(new_article)

        return len(self.urlLinks)

    def as_list(self):
        """Return Python List"""
        return self.urlLinks

    def as_json(self):
        """Return JSON List"""
        return json.dumps(self.urlLinks)

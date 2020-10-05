import json
from bs4 import BeautifulSoup
from pubsub.pub import sendMessage
from requests import get
from requests.exceptions import RequestException, HTTPError, InvalidSchema, MissingSchema
from novelcores.novelclass.Func import ExFunc
get_soup = ExFunc.get_soup
get_title = ExFunc.get_title


class FastNovel:
    slash = 3
    url = "https://fastnovel.net/"
    title_tag = "h1"
    title_tag_class = "name"

    @staticmethod
    def get_soup(url: str):
        return get_soup(url)

    @staticmethod
    def get_title(soup: BeautifulSoup) -> str:
        return get_title(soup, FastNovel.title_tag, FastNovel.title_tag_class)

    @staticmethod
    def get_author(soup: BeautifulSoup) -> str:
        meta_data = soup.find("ul", class_="meta-data")
        author_item = BeautifulSoup(str(meta_data), 'html.parser').find("li")
        author = BeautifulSoup(str(author_item), 'html.parser').find("a").text
        return str(author)

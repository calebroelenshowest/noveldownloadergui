import json
from bs4 import BeautifulSoup
from pubsub.pub import sendMessage
from requests import get
from requests.exceptions import RequestException, HTTPError, InvalidSchema, MissingSchema
from novelcores.novelclass.Func import ExFunc
get_soup = ExFunc.get_soup
get_title = ExFunc.get_title


class Novel27:
    slash = 4
    url = "https://novel27.com/novel/"
    title_tag = "title"
    title_tag_class = ""

    @staticmethod
    def get_soup(url: str):
        return get_soup(url)

    @staticmethod
    def get_title(soup: BeautifulSoup):
        return get_title(soup, Novel27.title_tag, Novel27.title_tag_class, ["online free - Novel27", "Read"], False)

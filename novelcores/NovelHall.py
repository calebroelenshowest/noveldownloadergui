import json
from bs4 import BeautifulSoup
from pubsub.pub import sendMessage
from requests import get
from requests.exceptions import RequestException, HTTPError, InvalidSchema, MissingSchema
from novelcores.novelclass.Func import ExFunc
get_soup = ExFunc.get_soup
get_title = ExFunc.get_title


class NovelHall:
    slash = 3
    url = "https://novelhall.com/"
    title_tag = "h1"
    title_tag_class = ""

    @staticmethod
    def get_soup(url: str):
        return get_soup(url)

    @staticmethod
    def get_title(soup: BeautifulSoup):
        return get_title(soup, NovelHall.title_tag, NovelHall.title_tag_class, class_req=False)

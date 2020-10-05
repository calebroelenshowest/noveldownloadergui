import json
from bs4 import BeautifulSoup
from pubsub.pub import sendMessage
from requests import get
from requests.exceptions import RequestException, HTTPError, InvalidSchema, MissingSchema
from novelcores.novelclass.Func import ExFunc
get_soup = ExFunc.get_soup
get_title = ExFunc.get_title


class LightNovelWorld:
    slash = 4
    url = "https://www.lightnovelworld.com/novel/"
    title_tag = "h1"
    title_tag_class = "novel-title"

    @staticmethod
    def get_soup(url: str):
        return get_soup(url)

    @staticmethod
    def get_title(soup: BeautifulSoup) -> str:
        return get_title(soup, LightNovelWorld.title_tag, LightNovelWorld.title_tag_class)

import json
from bs4 import BeautifulSoup
from pubsub.pub import sendMessage
from requests import get
from requests.exceptions import RequestException, HTTPError, InvalidSchema, MissingSchema
from novelcores.novelclass.Func import ExFunc
get_soup = ExFunc.get_soup
get_title = ExFunc.get_title


class NovelFull:
    slash = 3
    url = "https://novelfull.com/"
    title_tag = "h3"
    title_tag_class = "title"

    @staticmethod
    def get_soup(url: str):
        return get_soup(url)

    @staticmethod
    def get_title(soup: BeautifulSoup) -> str:
        return get_title(soup, NovelFull.title_tag, NovelFull.title_tag_class)

    @staticmethod
    def get_author(soup: BeautifulSoup) -> str:
        try:
            div_info = soup.find("div", class_="info")
            div_div = BeautifulSoup(str(div_info), 'html.parser').find("div")
            author = BeautifulSoup(str(div_div), "html.parser").find("a").text
            return author
        except Exception:
            return "Unknown"


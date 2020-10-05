import json
from bs4 import BeautifulSoup
from pubsub.pub import sendMessage
from requests import get
from requests.exceptions import RequestException, HTTPError, InvalidSchema, MissingSchema
from novelcores.novelclass.Func import ExFunc
get_soup = ExFunc.get_soup
get_title = ExFunc.get_title


class NovelOnlineFull:
    slash = 4
    url = "https://novelonlinefull.com/novel/"
    title_tag = "h1"
    title_tag_class = ""

    @staticmethod
    def get_soup(url: str):
        return get_soup(url)

    @staticmethod
    def get_title(soup: BeautifulSoup) -> str:
        return get_title(soup, NovelOnlineFull.title_tag, NovelOnlineFull.title_tag_class, class_req=False)

    @staticmethod
    def get_author(soup: BeautifulSoup) -> str:
        author_soup = soup.find("ul", class_="truyen_info_right")
        author_item = BeautifulSoup(str(author_soup), "html.parser").findAll("li")[1]
        author = BeautifulSoup(str(author_item), "html.parser").find("a").text
        return str(author)
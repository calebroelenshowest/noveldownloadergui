import json
from bs4 import BeautifulSoup
from pubsub.pub import sendMessage
from requests import get
from requests.exceptions import RequestException, HTTPError, InvalidSchema, MissingSchema
from novelcores.novelclass.Func import ExFunc
get_soup = ExFunc.get_soup
get_title = ExFunc.get_title


class ReadNovelFull:
    slash = 3
    url = "https://readnovelfull.com/"
    title_tag = "h3"
    title_tag_class = "title"

    @staticmethod
    def get_soup(url: str):
        return get_soup(url)

    @staticmethod
    def get_title(soup: BeautifulSoup) -> str:
        return get_title(soup, ReadNovelFull.title_tag, ReadNovelFull.title_tag_class)

    @staticmethod
    def get_author(soup: BeautifulSoup) -> str:
        author_sp = soup.find("span", itemprop="author")
        author = BeautifulSoup(str(author_sp), "html.parser").find("meta", itemprop="name")["content"]
        return str(author)

    @staticmethod
    def get_url_chapters(soup: BeautifulSoup) -> list:
        pass

    @staticmethod
    def get_url_image(soup: BeautifulSoup) -> str:
        pass
import json
from bs4 import BeautifulSoup
from pubsub.pub import sendMessage
from requests import get
from requests.exceptions import RequestException, HTTPError, InvalidSchema, MissingSchema
from novelcores.novelclass.Func import ExFunc
get_soup = ExFunc.get_soup
get_title = ExFunc.get_title


class WuxiaWorldCo:
    slash = 3
    url = "https://www.wuxiaworld.co/"
    title_tag = "div"
    title_tag_class = "book-name"

    @staticmethod
    def get_soup(url: str):
        return get_soup(url)

    @staticmethod
    def get_title(soup: BeautifulSoup) -> str:
        return get_title(soup, WuxiaWorldCo.title_tag, WuxiaWorldCo.title_tag_class)

    @staticmethod
    def get_author(soup: BeautifulSoup) -> str:
        author_soup = soup.find("div", class_="author")
        author = BeautifulSoup(str(author_soup), "html.parser").find("span", class_="name").text
        return str(author)

    @staticmethod
    def get_url_chapters(soup: BeautifulSoup) -> list:
        pass

    @staticmethod
    def get_url_image(soup: BeautifulSoup) -> str:
        pass

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
    def get_soup(url: str) -> BeautifulSoup:
        return get_soup(url)

    @staticmethod
    def get_title(soup: BeautifulSoup) -> str:
        return get_title(soup, LightNovelWorld.title_tag, LightNovelWorld.title_tag_class)

    @staticmethod
    def get_author(soup: BeautifulSoup) -> str:
        author_div = soup.find("div", class_="author")
        author_a = str(BeautifulSoup(str(author_div), 'html.parser').find("a")["title"])
        return author_a

    @staticmethod
    def get_url_chapters(soup: BeautifulSoup) -> str:
        # Rather difficult souping, can take a while
        url_list_pages = soup.find_all("a", {"data-ajax-method": "get"})
        print(x.href for x in url_list_pages)


s = LightNovelWorld.get_soup("https://www.lightnovelworld.com/novel/trash-of-the-counts-family-wn")
x = LightNovelWorld.get_url_chapters(s)

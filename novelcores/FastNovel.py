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

    @staticmethod
    def get_url_chapters(soup: BeautifulSoup) -> list:
        chapters = []
        chapter_soup = soup.findAll("a", class_="chapter")
        for url in list(chapter_soup):
            chapter_item = {"url": "https://fastnovel.net" + url["href"],
                            "title": url.text}
            chapters.append(chapter_item)
        return chapters


if __name__ == "__main__":
    # Test of Fastnovel.net
    soup = FastNovel.get_soup("https://fastnovel.net/the-conquerors-bloodline-9825/")
    print(FastNovel.get_url_chapters(soup))
    print(FastNovel.get_title(soup))
    print(FastNovel.get_author(soup))

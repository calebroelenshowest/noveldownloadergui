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
    def __get_novel_id(soup: BeautifulSoup) -> int:
        return int(soup.find("div", id="rating")["data-novel-id"])

    @staticmethod
    def get_url_chapters(soup: BeautifulSoup) -> list:
        url = f"https://readnovelfull.com/ajax/chapter-archive?novelId={ReadNovelFull.__get_novel_id(soup)}"
        links = get_soup(url, True).find_all("a")
        chapters = []
        for chapter in links:
            template = {"url": chapter.href, "title": chapter["title"]}
            chapters.append(template)
        return chapters

    @staticmethod
    def get_url_image(soup: BeautifulSoup) -> str:
        image = soup.find("meta", attrs={"name": "image"})
        return image["content"]


if __name__ == "__main__":
    soup_X = ReadNovelFull.get_soup("https://readnovelfull.com/ghost-emperor-wild-wife-dandy-eldest-miss.html")
    x = ReadNovelFull.get_url_chapters(soup_X)
    image = ReadNovelFull.get_url_image(soup_X)

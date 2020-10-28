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
            author = soup.find("div", class_="info").find("div").find("a").text
            return author
        except Exception:
            return "Unknown"

    @staticmethod
    def __get_novel_id(soup: BeautifulSoup) -> int:
        find_id = soup.find("div", id="rating")
        return find_id["data-novel-id"]

    @staticmethod
    def get_url_chapters(soup: BeautifulSoup) -> list:
        chapters = []
        # Usage of AJAX, "NovelId needed
        url = "https://novelfull.com/ajax-chapter-option?novelId=" + str(NovelFull.__get_novel_id(soup))
        chapter_soup = get_soup(url, True).find_all("option")
        for chapter in chapter_soup:
            chapters.append({"url": "https://novelfull.com/" + chapter["value"], "title": chapter.text})
        return chapters

    @staticmethod
    def get_url_image(soup: BeautifulSoup) -> str:
        image = soup.find("meta", attrs={"name": "image"})
        return image["content"]


if __name__ == "__main__":
    soap = NovelFull.get_soup("https://novelfull.com/reincarnation-of-the-strongest-sword-god.html")
    author = NovelFull.get_author(soap)
    chapters = NovelFull.get_url_chapters(soap)
    image = NovelFull.get_url_image(soap)
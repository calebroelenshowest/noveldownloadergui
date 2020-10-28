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
    def get_soup(url: str) -> BeautifulSoup:
        return get_soup(url, True)

    @staticmethod
    def get_title(soup: BeautifulSoup) -> str:
        return get_title(soup, NovelHall.title_tag, NovelHall.title_tag_class, class_req=False)

    @staticmethod
    def get_author(soup: BeautifulSoup) -> str:
        prop = soup.find("meta", property="books:author")["content"]
        return str(prop)

    @staticmethod
    def get_url_chapters(soup: BeautifulSoup) -> list:
        chapters = []
        soup_chapters = soup.find("div", class_="book-catalog inner mt20  hidden-xs")
        print(soup_chapters)
        for chapter in soup_chapters:
            new_chapter = chapter.find("a")
            title = new_chapter.text
            url = "https://novelhall.com/" + new_chapter["href"]
            chapters.append({"url": url, "title": title})
        return chapters

    @staticmethod
    def get_url_image(soup: BeautifulSoup) -> str:
        pass


if __name__ == "__main__":
    soup = NovelHall.get_soup("https://novelhall.com/Invincible-136/")
    print(soup)
    chapters = NovelHall.get_url_chapters(soup)
    print(chapters)

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
        chapters_item = soup.find_all("a", class_="chapter-item")
        chapters = []
        for chapter in chapters_item:
            title = chapter.find("p", class_="chapter-name").text
            chapter_a = BeautifulSoup(str(chapter), 'html.parser').find("a")["href"]
            template = {"url": "https://www.wuxiaworld.co" + chapter_a, "title": title}
            chapters.append(template)
        return chapters

    @staticmethod
    def get_url_image(soup: BeautifulSoup) -> str:
        img = soup.find("div", class_="book-img").find("img")["src"]
        return img


if __name__ == "__main__":
    s = WuxiaWorldCo.get_soup("https://www.wuxiaworld.co/Genius-Doctor--Black-Belly-Miss/")
    img = WuxiaWorldCo.get_url_image(s)
    chap = WuxiaWorldCo.get_url_chapters(s)

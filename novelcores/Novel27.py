import json
from bs4 import BeautifulSoup
from pubsub.pub import sendMessage
from requests import get
from requests.exceptions import RequestException, HTTPError, InvalidSchema, MissingSchema
from novelcores.novelclass.Func import ExFunc
get_soup = ExFunc.get_soup
get_title = ExFunc.get_title


class Novel27:
    slash = 4
    url = "https://novel27.com/novel/"
    title_tag = "title"
    title_tag_class = ""

    @staticmethod
    def get_soup(url: str):
        return get_soup(url)

    @staticmethod
    def get_title(soup: BeautifulSoup) -> str:
        return get_title(soup, Novel27.title_tag, Novel27.title_tag_class, ["online free - Novel27", "Read"], False)

    @staticmethod
    def get_author(soup: BeautifulSoup) -> str:
        author_div = soup.find("div", class_="author-content")
        author_item = author_div.find("a").text
        return author_item

    @staticmethod
    def get_url_chapters(soup: BeautifulSoup) -> list:
        chapters = []
        li_elements = soup.find_all("li", class_="wp-manga-chapter")
        for li in li_elements:
            a_tag = li.find("a")
            chapter = {"url": a_tag["href"], "title": a_tag.text}
            chapters.append(chapter)
        print(f"Found {len(chapters)} chapters.")
        return list(reversed(chapters))

    @staticmethod
    def get_url_image(soup: BeautifulSoup) -> str:
        image = soup.find("meta", property="og:image")
        return image["content"]


if __name__ == "__main__":
    soup_x = Novel27.get_soup("https://novel27.com/novel/cultivation-chat-group/")
    chapters_x = Novel27.get_url_chapters(soup_x)
    image_x = Novel27.get_url_image(soup_x)
    author_x = Novel27.get_author(soup_x)

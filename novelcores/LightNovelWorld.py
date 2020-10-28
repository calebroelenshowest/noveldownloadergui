import json
from bs4 import BeautifulSoup
from pubsub.pub import sendMessage
from requests import get
from requests.exceptions import RequestException, HTTPError, InvalidSchema, MissingSchema
from novelcores.novelclass.Func import ExFunc
import time

get_soup = ExFunc.get_soup
get_title = ExFunc.get_title


class LightNovelWorld:
    slash = 4
    url = "https://www.lightnovelworld.com/novel/"
    title_tag = "h1"
    title_tag_class = "novel-title"

    @staticmethod
    def get_soup(url: str) -> BeautifulSoup:
        return get_soup(url, anti_bot=True)

    @staticmethod
    def get_title(soup: BeautifulSoup) -> str:
        return get_title(soup, LightNovelWorld.title_tag, LightNovelWorld.title_tag_class)

    @staticmethod
    def get_author(soup: BeautifulSoup) -> str:
        author_div = soup.find("div", class_="author")
        author_a = str(BeautifulSoup(str(author_div), 'html.parser').find("a")["title"])
        return author_a

    @staticmethod
    def get_url_chapters(soup: BeautifulSoup) -> list:
        # Rather difficult souping, can take a while
        url_list_pages = []
        li_item = soup.find("li", class_="PagedList-skipToLast")
        a_item = str(BeautifulSoup(str(li_item), 'html.parser').find("a")["href"])
        index = a_item.find("&page=") + len("&page=")
        max_number = int(a_item[index])
        for page in range(1, max_number+1):
            url_list_pages.append("https://www.lightnovelworld.com" + a_item[:index] + str(page) + a_item[index+1:])
        # Got all urls to all pages!
        print("Downloading " + str(len(url_list_pages)) + " pages, 100c/p.")
        chapters = []
        time.sleep(0.5)  # Delay! To many requests code 429
        for url_page in url_list_pages:
            print("Souping and getting urls: " + url_page)
            new_soup = get_soup(url_page, True)
            new_chapters_ul = new_soup.find("ul", class_="chapter-list")
            new_chapters_a = BeautifulSoup(str(new_chapters_ul), 'html.parser').find_all("a")
            for chapter in list(new_chapters_a):
                chapters.append({"url": str("https://www.lightnovelworld.com" + chapter["href"]), "title": chapter["title"]})
        print(f"Found {len(chapters)} chapters.")
        return chapters

    @staticmethod
    def get_url_image(soup : BeautifulSoup) -> str:
        figure = soup.find("meta", itemprop="image")
        return figure["content"]


if __name__ == "__main__":
    s = LightNovelWorld.get_soup("https://www.lightnovelworld.com/novel/trash-of-the-counts-family-wn")
    z = LightNovelWorld.get_url_chapters(s)
    g = LightNovelWorld.get_url_image(s)



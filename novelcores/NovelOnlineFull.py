import json
from bs4 import BeautifulSoup
from pubsub.pub import sendMessage
from requests import get
from requests.exceptions import RequestException, HTTPError, InvalidSchema, MissingSchema
from novelcores.novelclass.Func import ExFunc
get_soup = ExFunc.get_soup
get_title = ExFunc.get_title


class NovelOnlineFull:
    slash = 4
    url = "https://novelonlinefull.com/novel/"
    title_tag = "h1"
    title_tag_class = ""

    @staticmethod
    def get_soup(url: str):
        return get_soup(url)

    @staticmethod
    def get_title(soup: BeautifulSoup) -> str:
        return get_title(soup, NovelOnlineFull.title_tag, NovelOnlineFull.title_tag_class, class_req=False)

    @staticmethod
    def get_author(soup: BeautifulSoup) -> str:
        author_soup = soup.find("ul", class_="truyen_info_right")
        author_item = BeautifulSoup(str(author_soup), "html.parser").findAll("li")[1]
        author = BeautifulSoup(str(author_item), "html.parser").find("a").text
        return str(author)

    @staticmethod
    def get_url_chapters(soup: BeautifulSoup) -> list:
        new_soup = soup.find("div", class_="chapter-list").find_all("div", class_="row")
        chapters = []
        for item in new_soup:
            chapter_item = item.find("a")
            new_item = {"title": chapter_item["title"], "url": chapter_item.href}
            chapters.append(new_item)
        return chapters

    @staticmethod
    def get_url_image(soup: BeautifulSoup) -> str:
        image = soup.find("meta", property="og:image")
        return image["content"]


if __name__ == "__main__":
    novel_soup = NovelOnlineFull.get_soup("https://novelonlinefull.com/novel/a_mistaken_marriage_match_mysteries_in_the_imperial_harem")
    chapters = NovelOnlineFull.get_url_chapters(novel_soup)

from requests import get
from pubsub.pub import subscribe, sendMessage
from bs4 import BeautifulSoup
import gui.Listeners


class Chapter:

    def __init__(self, url: str, title: str, identifier: int, text_html=True):
        self.__title = title
        self.__text = []
        self.__identifier = identifier
        self.__html = ""
        self.__is_text_html = text_html
        self.__url = url

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, value: str):
        if isinstance(value, str):
            if value == "":
                raise ValueError("Title cannot be empty")
            else:
                self.__title = value
        else:
            raise TypeError("Title must be type string.")

    @property
    def identifier(self) -> int:
        return self.__identifier

    @identifier.setter
    def identifier(self, value: int):
        if isinstance(value, int):
            if value >= 0:
                self.__identifier = value
            else:
                raise ValueError("Identifier must be bigger than or equal to 0")
        else:
            raise TypeError("Identifier must be an int.")

    def generate_html(self) -> str:
        self.__html = f"<h1>{self.__title}</h1>"
        if self.__is_text_html:
            self.__html += self.__text
            return self.__html
        else:
            for text in self.__text:
                self.__html += f"<p>{text}</p>"
            return self.__html

    def download_chapter(self, tags, class_tags="") -> str:
        download = get(self.__url)
        if download.status_code == 200:
            soup = BeautifulSoup(download.content, 'html.parser')
            if class_tags == "":
                html_p_tags = soup.find_all(tags)
            else:
                html_p_tags = soup.find_all(tags, class_=class_tags)

            self.__html = "".join(map(str, html_p_tags))
        else:
            gui.Listeners.Message.error(f"Failed to download chapter: {self.__title} ")

    @property
    def html(self) -> str:
        return self.__html

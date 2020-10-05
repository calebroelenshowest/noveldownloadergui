import json
from bs4 import BeautifulSoup
from pubsub.pub import sendMessage
from requests import get
from requests.exceptions import RequestException, HTTPError, InvalidSchema, MissingSchema
from novelcores.novelclass.Func import ExFunc
get_soup = ExFunc.get_soup


class LightNovelWorld:
    slash = 4
    url = "https://www.lightnovelworld.com/novel/"

    @staticmethod
    def get_soup(url: str):
        return get_soup(url)
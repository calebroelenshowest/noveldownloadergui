# External imports

import json
from bs4 import BeautifulSoup
from pubsub.pub import sendMessage
from requests import get
from requests.exceptions import RequestException, HTTPError, InvalidSchema, MissingSchema
from novelcores.novelclass.Exceptions import IncorrectURL, UnknowSourceError

# NOVEL core imports

from novelcores.FastNovel import FastNovel
from novelcores.LightNovelWorld import LightNovelWorld
from novelcores.Novel27 import Novel27
from novelcores.NovelFull import NovelFull
from novelcores.NovelHall import NovelHall
from novelcores.NovelOnlineFull import NovelOnlineFull
from novelcores.ReadNovelFull import ReadNovelFull
from novelcores.WuxiaWorldCo import WuxiaWorldCo
source_obj = [FastNovel, LightNovelWorld, Novel27, NovelFull, NovelHall, NovelOnlineFull, ReadNovelFull, WuxiaWorldCo]


class Source:
    source_set = None

    @staticmethod
    def validate(url):
        if isinstance(url, str):
            if url.strip() != "":
                if "http" in url:
                    c = 3
                    if url[-1] == "/":
                        c -= 1
                    for source in source_obj:
                        if source.url in url:
                            Source.source_set = source
                            return True
                    if Source.source_set is None:
                        raise UnknowSourceError("Failed to find source sheme.")
                else:
                    raise IncorrectURL("URL incorrect. No HTTP or HTTPS in the URL.")
            else:
                raise ValueError("URL cannot be empty")
        else:
            raise TypeError("URL must be a string type!")




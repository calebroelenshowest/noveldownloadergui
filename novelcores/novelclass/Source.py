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
                    for source in source_obj:
                        if source.url in url:
                            Source.source_set = source
                            break
                    if Source.source_set is None:
                        raise UnknowSourceError("Failed to find source sheme.")
                    else:
                        c = Source.source_set.slash
                        if url[-1] == "/":
                            s = -1
                        else:
                            s = 0
                        if c == url.count("/")+s:
                            return True
                        else:
                            raise IncorrectURL("URL source is found, but the wrong page is selected.")
                else:
                    raise IncorrectURL("URL incorrect. No HTTP or HTTPS in the URL.")
            else:
                raise ValueError("URL cannot be empty")
        else:
            raise TypeError("URL must be a string type!")

    @staticmethod
    def get_novel_controller():
        return Source.source_set

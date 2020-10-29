# External imports

import json
from bs4 import BeautifulSoup
from pubsub.pub import sendMessage
from requests import get
from requests.exceptions import RequestException, HTTPError, InvalidSchema, MissingSchema
from novelcores.novelclass.Exceptions import IncorrectURL, UnknowSourceError
from gui.Listeners import Message

# NOVEL core imports

from novelcores.FastNovel import FastNovel
from novelcores.LightNovelWorld import LightNovelWorld
from novelcores.Novel27 import Novel27
from novelcores.NovelFull import NovelFull
from novelcores.NovelHall import NovelHall  # Disabled
from novelcores.NovelOnlineFull import NovelOnlineFull
from novelcores.ReadNovelFull import ReadNovelFull
from novelcores.WuxiaWorldCo import WuxiaWorldCo
source_obj = [FastNovel, LightNovelWorld, Novel27, NovelFull, NovelOnlineFull, ReadNovelFull, WuxiaWorldCo]


class Source:
    source_set = None

    @staticmethod
    def validate(url: str):
        if isinstance(url, str):
            if url.strip() != "":
                if "http" in url:
                    for source in source_obj:
                        if source.url in url:
                            Source.source_set = source
                            break
                    if Source.source_set is None:
                        Message.error("Failed to find source sheme!")
                        return False
                    else:
                        c = Source.source_set.slash
                        if url[-1] == "/":
                            s = -1
                        else:
                            s = 0
                        if c == url.count("/")+s:
                            return True
                        else:
                            Message.error("URL source is found, but the wrong page is selected.")
                            return False
                else:
                    Message.error("URL incorrect. No HTTP or HTTPS in the URL.")
                    return False
            else:
                Message.error("URL cannot be empty")
                return False
        else:
            Message.error("URL must be a string type!")
            return False

    @staticmethod
    def get_novel_controller():
        return Source.source_set



import json
from bs4 import BeautifulSoup
from pubsub.pub import sendMessage
from requests import get
from requests.exceptions import RequestException, HTTPError, InvalidSchema, MissingSchema


class LightNovelWorld:
    slash = 4
    url = "https://www.lightnovelworld.com/novel/"

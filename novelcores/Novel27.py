import json
from bs4 import BeautifulSoup
from pubsub.pub import sendMessage
from requests import get
from requests.exceptions import RequestException, HTTPError, InvalidSchema, MissingSchema


class Novel27:
    slash = 4
    url = "https://novel27.com/novel/"

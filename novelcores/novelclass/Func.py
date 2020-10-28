from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException, HTTPError, InvalidSchema, MissingSchema

# Functions that do not change per class are stored here.


class ExFunc:

    @staticmethod
    def get_soup(url: str, anti_bot: bool = False):
        # Please check URL beforehand using Source class
        try:
            if anti_bot:
                response = get(url, headers={'User-Agent': 'Mozilla/5.0'})
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    return soup
                else:
                    print("Cannot connect to ", url)
                    print("Code: ", response.status_code)
                    raise HTTPError("Failed")
            else:
                response = get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    return soup
                else:
                    raise RequestException("Status code is not 200: ", response.status_code)
        except HTTPError:
            print("HTTP error")
        except InvalidSchema:
            print("Invalid HTTP(s) scheme")
        except MissingSchema:
            print("URL has no HTTP scheme")
        except RequestException as exception:
            print("Exception in getting URL")
            print(exception)

    @staticmethod
    def get_title(soup: BeautifulSoup, tag: str, tag_class: str, banned: list = None, class_req: bool = True) -> str:
        try:
            if class_req:
                title = soup.find(tag, class_=tag_class).text
            else:
                title = soup.find(tag).text
            if banned is None:
                return title
            else:
                for banned_str in banned:
                    title = title.replace(banned_str, "")
                return title
        except Exception as exception:
            print("Failed to get title:")
            print(exception)


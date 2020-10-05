from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException, HTTPError, InvalidSchema, MissingSchema

# Functions that do not change per class are stored here.


class ExFunc:

    @staticmethod
    def get_soup(url: str):
        # Please check URL beforehand using Source class
        try:
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

from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

from extract_data import json_parser

address = "0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a"
api_url_test1 = "http://api.etherscan.io/api?module=account&action=balance&address=0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae&tag=latest&apikey=F6KD4YVEAVT9P6M2U3TPCGZCXT4PRQG4U9"
api_url_test2 = "http://api.etherscan.io/api?module=account&action=txlist&address=0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey=F6KD4YVEAVT9P6M2U3TPCGZCXT4PRQG4U9"
api_url_test3 = "http://api.etherscan.io/api?module=account&action=txlist&address=" + address + "&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey=F6KD4YVEAVT9P6M2U3TPCGZCXT4PRQG4U9"


def website_connection():
    request_page = urlopen(api_url_test2)
    page_html = request_page.read()
    request_page.close()

    html_soup = BeautifulSoup(page_html, 'html.parser')


def get_data():
    response = requests.get(api_url_test2)
    address_content = response.json()
    result = address_content.get("result")
    return result



if __name__ == '__main__':
    json_parser(get_data())

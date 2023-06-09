import requests
from .data_cleaner import clean_options_data
from typing import Union
from requests import Response


def get_api_data(url: str, month: str)->Union[dict , Response]:
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
        "authority": "www.nseindia.com",
        "scheme": "https",
    }

    response = requests.get(url, headers=header)
    if response.status_code == 200:
        response = response.text
        return clean_options_data(response=response, month=month)
    else:
        return response.headers

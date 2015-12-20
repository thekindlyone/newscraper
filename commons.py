from bs4 import BeautifulSoup as bs
import requests
import re
from datetime import datetime,timedelta
import traceback


def get_soup(url,params):
    r=requests.get(url,params=params)
    if r.status_code==200:
        return bs(r.content,'lxml'),r.url

def handle(func):
    try:
        return func()
    except:
        return None
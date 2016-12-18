from bs4 import BeautifulSoup as bs
import requests

req = requests.get("https://en.wikipedia.org/wiki/Main_Page")
soup = bs(req.content)

def hi():
    return "hi"

def site_name():
    return soup.title.string

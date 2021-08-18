import csv
import xml.etree.ElementTree as et
import requests
import  re
# import lxml.html
# from bs4 import BeautifulSoup

class Parser:

    def data_lenta(self, url):                                  # парсер с сайта лента
        root = et.fromstring(requests.get(url).content)
        item_lenta = {}
        for i in root.iter('item'):
            item_lenta[str(i.find('title').text)] = []
            item_lenta[str(i.find('title').text)].append(str(i.find('link').text))
            desc = re.sub("[\n]","",str(i.find('description').text))
            item_lenta[str(i.find('title').text)].append(desc)
            item_lenta[str(i.find('title').text)].append(str(i.find('enclosure').attrib['url']))
            item_lenta[str(i.find('title').text)].append(str(i.find('pubDate').text))
            # item_lenta[str(i.find('title').text)].append(str(i.find('category').text))

        return item_lenta

    def data_cnews(self, url):                                  # парсер с сайта cnews
        root = et.fromstring(requests.get(url).content)
        item_cnews = {}
        for i in root.iter('item'):
            item_cnews[str(i.find('title').text)] = []
            item_cnews[str(i.find('title').text)].append(str(i.find('link').text))
            desc = re.sub("[\n<>p/]", "", str(i.find('description').text))
            item_cnews[str(i.find('title').text)].append(desc)
            item_cnews[str(i.find('title').text)].append(str(i.find('pubDate').text))

        return item_cnews


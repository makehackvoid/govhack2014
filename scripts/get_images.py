#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import urllib.request
import os


def save_file(url,filename):
    if (os.path.exists(filename)):
        print(filename + ' already exists locally')
        pass
    urllib.request.urlretrieve(url,filename)

def get_filename(url):
    relpath = urlparse(url).path
    return os.path.split(relpath)[-1]


url = 'http://www.data.act.gov.au/resource/j746-krni.json'
data = requests.get(url).json()

filedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/images'))

if not os.path.exists(filedir):
    os.makedirs(filedir)


download_list = []

for item in data:
    title = item['title']
    page = item['url_1']['url']
    pic = item['url_2']['url']
    filename = get_filename(pic)

    download_list.append({'title': title, 'page': page, 'file': filename })
for item in download_list:
    retry = requests.get(item['page']).text
    data = BeautifulSoup(retry)
    imageurl = data.find_all('div',{'id' :'artinfo'})[0].find_all('img')[0]['src']
    save_file(imageurl,os.path.join(filedir,item['file']))


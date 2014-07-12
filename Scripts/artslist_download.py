import os
import urllib.request

url = 'http://www.data.act.gov.au/resource/j746-krni.json'
filedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/'))

if not os.path.exists(filedir):
    os.makedirs(filedir)

urllib.request.urlretrieve(url, os.path.join(filedir, "arts-list.json"))

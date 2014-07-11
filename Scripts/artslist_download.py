import urllib.request

url = 'http://www.data.act.gov.au/resource/j746-krni.json'
fileName = 'artsList.json'

urllib.request.urlretrieve(url, fileName)

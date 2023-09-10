import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=61b8cb52e787484388c5395e6f9c7596')
response = requests.get(url)
# print (response.json())
# print (response.text)


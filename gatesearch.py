'''
1) Article from date function: Gives the url's and published dates of articles from the date in-putted till today.
2)Word Search function
	Output: URL links
	Input: A specific word you are looking for in the articles of NY times
'''

import urllib.request
import json
import codecs

nytimes_apikey = '145d3afa81afdda88c53f2fc42c6d459:18:71835164'

def articlefromdate(query):
    api_key = nytimes_apikey
    url= 'http://api.nytimes.com/svc/search/v2/articlesearch.json?api-key='+api_key
    q=query
    final_url= url + "&begin_date=" +q
    json_obj= urllib.request.urlopen(final_url)
    reader = codecs.getreader("utf-8")
    data = json.load(reader(json_obj))
    for item in data['response']['docs']:
		print(item['web_url'],item['pub_date']) 
		
		
def word_search(query):
    api_key = nytimes_apikey
    url= 'http://api.nytimes.com/svc/search/v2/articlesearch.json?api-key='+api_key
    q=query
    final_url= url + "&q=" +q
    json_obj= urllib.request.urlopen(final_url)
    reader = codecs.getreader("utf-8")
    data = json.load(reader(json_obj))
    for item in data['response']['docs']:
        print(item['web_url'])
		
		
'''
this portion of code directly gives you the URLs for word GATE

import urllib.request
import json
import codecs

ny_api = '145d3afa81afdda88c53f2fc42c6d459:18:71835164'

#URl for NY times artical search for word "GATE"
url = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?q=gate&api-key=145d3afa81afdda88c53f2fc42c6d459%3A18%3A71835164'

# returns http json object responce in utf-8 format
json_obj= urllib.request.urlopen(url) 

# reader decodes the utf-8 byte format to string format
reader = codecs.getreader("utf-8")
data = json.load(reader(json_obj))
#print(data)
for item in data['response']['docs']:
    print(item['web_url'])
'''
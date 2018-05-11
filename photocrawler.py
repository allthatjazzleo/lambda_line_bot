from bs4 import BeautifulSoup
import random
import lxml
import urllib.request

def return_url():

	request_headers = {
	"Accept-Language": "en-US,en;q=0.5",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Referer": "http://jdailyhk.com",
	"Connection": "keep-alive" 
	}

#from urllib.request import urlopen
	req = urllib.request.Request('http://jdailyhk.com/topranking', headers=request_headers)
	soupnotbeauttiful = urllib.request.urlopen(req)
	soup = BeautifulSoup(soupnotbeauttiful,"html.parser")

	links = []
	for div in soup.find_all("div",{"class":"td-module-thumb"}):
		img = BeautifulSoup(str(div),"html.parser")
		link = img.findAll('img')[0]['src']   
		links.append(link)
		
	return random.choice(links)
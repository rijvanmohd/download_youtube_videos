import os
from django.conf import settings
import requests
# from bs4 import BeautifulSoup
import json
# from requests_html import HTMLSession 
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.phantomjs.service import Service as PhantomService
# from selenium import webdriver
import time
from pytube import YouTube

# DOWNLOAD_PATH

def download_youtube_video(filename):
	file = os.path.join(settings.MEDIA_ROOT,filename)
	with open(file) as reader:
		reader_tags = [line.rstrip('\n') for line in reader]
		reader_tags = set(reader_tags)
		for tag in reader_tags:
			print(tag)
			search_video(tag)



def search_video(tag):

# Beautifulsoup does not work on js rendered websites i.e. youtube

	# headers = {'User-Agent': 'Mozilla/5.0'}
	# session = HTMLSession()
	# response = session.get('https://www.youtube.com/results?search_query='+tag)
	# soup = BeautifulSoup(response.html.html, 'html.parser')
	# print(response.html.html)

# selenium solution

	# driver_path = '/usr/local/bin/phantomjs'
	# service = PhantomService(driver_path)
	# service.start()
	# options = {}
	# driver = webdriver.Remote(service.service_url, options)
	# driver.implicitly_wait(10)

	# youtube = 'https://www.youtube.com'
	# search_url = youtube+'?search_query='+str(tag)
	# driver.get(search_url)
	# time.sleep(3)

	# page = BeautifulSoup(driver.page_source, 'html.parser')
	# print(page)
	# links = page.select('a[href^="/watch?v="]')
	# print(links)


	# Convert scrape results to JSON
	# data = []
	# for x in links:
	#     if x.has_attr('title'):
	#         name = x.get_text()
	#         partial_link = x['href']
	#         full_link = "https://www.youtube.com"+partial_link

	#         data.append(json.dumps({"Name":name, "Link":full_link}))

	# print(json.dumps(data))



# Alternate solution to fetch the video link

	tag = tag.replace(' ','%20')
	response = requests.get('http://youtube-scrape.herokuapp.com/api/search?q='+tag)
	response_data = response.json()
	# first_video = response_data['results'][0]['video']
	# url = first_video['url']
	# print(url)
	save_path = os.path.join(settings.DOWNLOAD_PATH,tag)

	
	for idx,each in enumerate(response_data['results']):
		url = each['video']['url']
		print(f'checking url availability - {idx}')
		print(f'url - {url}')
		try:
			yt = YouTube(url)
			break;
		except:
			print('Url not available. checking next')

	if not os.path.exists(os.path.join(save_path,tag)):
		yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').first().download(save_path,filename=tag)

	print('Task Completed')


#!/bin/python

from bs4 import BeautifulSoup
import sys
import requests
import re
import os

def download_img(folder, name):
	parts = name.split(".")
	name = parts[0][:-1] + "." + parts[1]
	url = "http://i.imgur.com/" + name
	print "Downloading " + name + "..."
	img_data = requests.get(url)
	
	file = open(folder + "/" + name, "w")
	file.write(img_data.content)
	file.close()
	
if __name__ == '__main__':
	album = sys.argv[1]
	album_name = re.findall(r"\/a\/([A-Za-z0-9]{5})", album)[0]
	folder = album_name + "-files"
	
	try:
		os.mkdir(folder)
	except:
		print "Folder already exists."
	
	if album_name == None:
		print "Malformed album URL."
		sys.exit()

	page = requests.get(sys.argv[1]).content
	soup = BeautifulSoup(page)
	
	imgs = soup.findAll("img", id = re.compile("thumb-([A-Za-z0-9]{5})"))
	for img in imgs:
		url = img['data-src']
		download_img(folder, url.split(".com/")[1])
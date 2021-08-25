#!/usr/bin/env python3

import re
import urllib.request
from bs4 import BeautifulSoup
from mongoDB import manageDB
from filter import filterLinks
from writelog import Logging


def getAndParseURL(url):

	html_page = urllib.request.urlopen(url)
	testDB = manageDB()						#creates database object
	testDB.createDB()						#creates database object

	soup = BeautifulSoup(html_page, 'html.parser')						#parsing html page into soup variable
	for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):						#for every item in soup variable extract the necessary strings
		if url == 'https://lightdlmovies.blogspot.com/search/label/MOVIES/':
			valid = filterLinks(link.get('href'))
			if valid == True:
				testDB.insertMovies (link.get('href'))
		elif url == 'https://www.lightdl.xyz/search/label/TV%20SERIES/':
			valid = filterLinks(link.get('href'))
			if valid == True:
				testDB.insertSeries (link.get('href'))
		else:
			pass

if __name__ == "__main__":
	try:
		getAndParseURL('https://lightdlmovies.blogspot.com/search/label/MOVIES/')
		getAndParseURL('https://www.lightdl.xyz/search/label/TV%20SERIES/')
	except Exception as error:
		Logging('error.md', error)
		print('Please review error.md file.')

#version with mongoDB
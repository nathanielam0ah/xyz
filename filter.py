#!/usr/bin/env python3

def filterLinks(link):
	validLink = False
	if 'f2m' in link:
		validLink = True
	elif 'upload10' in link:
		validLink =  True
	elif 'uploadcdn' in link:
		validLink =  True
	elif 'ariamovie' in link:
		validLink =  True
	elif 'hostgig' in link:
		validLink ==  True
	return validLink

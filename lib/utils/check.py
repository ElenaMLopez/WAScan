#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Wascan - Web Application Scanner
# @repo:    https://github.com/m4ll0k/Wascan
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt'

from urlparse import urlsplit,urljoin
from lib.utils.printer import *
from lib.utils.rand import r_string

def CPath(url,path):
	return urljoin(url,path)

def AParams(params):
	random_string = "%s"%(r_string(10)).upper()
	if '=' not in params:
		return "%s=%s"%(params,random_string)
	else:
		return "%s%s"%(r_string(10)).upper()
	return params

def CQuery(url,params):
	params = AParams(params)
	if url.endswith('?'):
		return url+params
	elif not url.endswith('?'):
		if url.endswith('&'):
			return url+params
		elif '?' in url and '&' not in url:
			return url+'&'+params
		else:
			return url+"?"+params
	else:
		return url+"?"+ params


def CUrl(url):
	split = urlsplit(url)
	# check URL scheme
	if split.scheme not in ['http','https','']:
		# e.g: exit if URL scheme = ftp,ssh,..etc
		exit(less('Check your URL, scheme "%s" not supported!!'%(split.scheme)))
	else:
		# if URL --> www.site.com
		if split.scheme not in ['http','https']:
			# return http://www.site.com
			return "http://%s"%(url)
		else:
			return url

def CEndUrl(url):
	if url.endswith('/'):
		return url[:-1]
	return url

def CScan(scan):
	# check scan options
	if scan not in ['0','1','2','3','4','5']:
		info('Option --scan haven\'t argument, assuming default value 5')
		scan = int('5') 
	if isinstance(scan,str):
		return int(scan)
	return int(scan)

class SplitURL:
	def __init__(self,url):
		# http,https
		self.scheme = urlsplit(url).scheme 
		# www.site.com
		self.netloc = CUrl(urlsplit(url).netloc)
		# /test/index.php
		self.path = urlsplit(url).path
		# id=1&f=1
		self.query = urlsplit(url).query
		# #test
		self.fragment = urlsplit(url).fragment

def CHeaders(headers):
	# e.g: "Host:google.com" return {'Host':'google.com'}
	_ = {}
	if ':' in headers:
		if ',' in headers:
			headerList = headers.split(',')
			for header in headerList:
				_[header.split(':')[0]] = header.split(':')[1]
		else:
			_[headers.split(':')[0]] = headers.split(':')[1]
	return _

def CAuth(auth):
	if ':' not in auth:
		return "%s:"%(auth)
	return auth
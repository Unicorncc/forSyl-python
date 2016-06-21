# -*- coding:utf-8 -*-

import re
from urllib import request

def getHtml(url):
	page = request.urlopen(url)
	html = page.read()
	return html
	
def getImg(html):
	html = html.decode('utf-8')
	imglist=re.findall(r'src="([.*\S]*\.jpg)"', html)
	x = 0
	for imgurl in imglist:
		request.urlretrieve(imgurl,'%s.jpg' % x)
		x+=1
	

for n in range(10):
	html = getHtml("http://tieba.baidu.com/p/{s}".format(s = n + 461555000))

	
print(getImg(html))
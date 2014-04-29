#coding:utf-8

from urlparse import urlparse, parse_qs

URL_GET = """http://www.12380.gov.cn/ssl/feedback.shtml?_wdxid=000000000000000000000000000000000000000000&_wdc=OTH_0001018&_wdt=112&
"""

URL_POST = """http://luxinshe.sbsm.gov.cn/review/review.jsp(POST)username=atestuseru&aid=20080800040292&content=atestu&sid=luxinshe&atitle=%E9%B9%BF%E5%BF%83%E7%A4%BE%E5%9C%A8%E5%90%AC%E5%8F%96%E5%8C%97%E4%BA%AC%E5%B8%82%E6%B5%8B%E7%BB%98%E5%B7%A5%E4%BD%9C%E6%B1%87%E6%8A%A5%E6%97%B6%E8%A6%81%E6%B1%82%3Cbr%3E%3Cb%3E%E6%89%93%E7%89%A2%E5%9F%BA%E7%A1%80+%E5%8A%A0%E5%BC%BA%E7%AE%A1%E7%90%86+%E6%90%9E%E5%A5%BD%E6%9C%8D%E5%8A%A1%3C%2Fb%3E%22%27%3E%3CIMG+SRC%3D%22%2Ftest.html%22%3E
"""

url_list = [URL_GET, URL_POST]

for i in url_list:
	if i.find('(POST)') == -1: #POST
		pass
	else: #GET
		pass
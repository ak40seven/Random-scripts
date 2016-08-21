import mechanize
import urllib2
def viewPage(url):
	browser = mechanize.Browser()
	page = browser.open(url)
	source_code = page.read()
	print source_code
viewPage('http://www.name-of-Site-here.com')

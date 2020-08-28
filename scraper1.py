#import basic HTTP handling processes
import urllib
from urllib.request import urlopen
#import scraping libraries
from bs4 import BeautifulSoup

#import the main page of Polygon
polygon = urlopen('https://www.polygon.com/')
bs = BeautifulSoup(polygon.read(),'html.parser')
#print the title of the current bs page
print(bs.title)

#import basic HTTP handling processes
import urllib
from urllib.request import urlopen

#import the main page of Polygon
polygon = urlopen('https://www.polygon.com/')
print(polygon.read())
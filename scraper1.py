#import system functions
import sys
import requests
#sys.path.append('/usr/local/lib/python3.8/site-packages/')
#import basic HTTP handling processes
#import urllib
#from urllib.request import urlopen
#import scraping libraries

#import newspaper and BS dependencies

from bs4 import BeautifulSoup
import newspaper
from newspaper import Article 
from newspaper import Source 
from newspaper import news_pool

#import broad data libraries
import pandas as pd

#import gaming related news sources as newspapers
gamespot = newspaper.build('https://www.gamespot.com/news', memoize_articles=False)
polygon = newspaper.build('https://www.polygon.com/gaming', memoize_articles=False)

#organize the gaming related news sources using a list
gamingPress = [gamespot, polygon]
print("About to set the pool.")
#parallel process these articles using multithreading (store in mem)
news_pool.set(gamingPress, threads_per_source=4)
print("Setting the pool")
news_pool.join()
print("Pool set")
#create the interim pandas dataframe based on these sources
final_df = pd.DataFrame()

#a limit on sources could be placed here; intentionally I have placed none
limit = 10

for source in gamingPress:
    #these are temporary placeholder lists for elements to be extracted
    list_title = []
    list_text = []
    list_source = []

    count = 0

    for article_extract in source.articles:
        article_extract.parse()
        
        #further limit functionality could be placed here; not placed
        if count > limit:
            break

        list_title.append(article_extract.title)
        list_text.append(article_extract.text)
        list_source.apprend(article_extract.source_url)

        print(count)
        count +=1 #progress the loop *via* count

    temp_df = pd.DataFrame({'Title': list_title, 'Text': list_text, 'Source': list_source})
    #Append this to the final DataFrame
    final_df = final_df.append(temp_df, ignore_index=True)

#export to CSV, placeholder for deeper analysis/more limited scope, may remain
final.df.to_csv('gaming_press.csv')


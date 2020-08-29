# created with assistance from https://towardsdatascience.com/the-easy-way-to-web-scrape-articles-online-d28947fc5979

import newspaper #parsing of news sources
from newspaper import Article #separate out specific parts of the text we want
from newspaper import Source # see previous line comment
import pandas as pd #dataframe for temporary data storage

polygon = newspaper.build('https://www.polygon.com/archives/2020/6', memoize_articles=False, number_threads=4)
gamespot = newspaper.build("https://www.gamespot.com//news/", memoize_articles = False, number_threads=4)

final_df = pd.DataFrame()
polygonTLOU=0

for each_article in polygon.articles:

    each_article.download()
    each_article.parse()
    each_article.nlp()

    temp_df = pd.DataFrame(columns = ['Title', 'Authors', 'Text',
                                    'Summary', 'published_date', 'Source'])

    temp_df['Authors'] = each_article.authors
    temp_df['Title'] = each_article.title
    temp_df['Text'] = each_article.text
    temp_df['Summary'] = each_article.summary
    temp_df['published_date'] = each_article.publish_date
    temp_df['Source'] = each_article.source_url
    if (each_article.text.find('Last of Us') != -1):
        final_df = final_df.append(temp_df, ignore_index = True)
        polygonTLOU = polygonTLOU+1
        print(polygonTLOU)
    else:
        print(polygonTLOU)

# From here you can export this Pandas DataFrame to a csv file
final_df.to_csv('my_scraped_articles.csv')


print(polygon.size())

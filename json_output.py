#!/usr/bin/python3
from newspaper import Article
import json
import pprint


'''Uncomment the three lines inside the function to get KEYWORDS and SUMMARY, btw it would increase the computational cost which is obvious'''

def article(url):
    smart_article_dict = dict()
    smart_article = Article(url)

    smart_article.download()
    smart_article.parse()
    # smart_article.nlp()

    smart_article_dict['Title'] = smart_article.title
    smart_article_dict['Text'] = str(smart_article.text).replace("\n","<br/>")
    smart_article_dict['Authors'] = smart_article.authors
    # smart_article_dict['Keywords'] = smart_article.keywords
    # smart_article_dict['Summary'] = smart_article.summary
    smart_article_dict['Publish_date'] = str(smart_article.publish_date)
    smart_article_dict['Favicon_img'] = smart_article.meta_favicon
    smart_article_dict['Top_img'] = smart_article.top_image
    #smart_article_dict['site_name'] = smart_article.meta_data['og']['site_name']

    # Comment these 2 lines below for not printing the json output
    #json_output = json.dumps(smart_article_dict)
    #pprint.pprint(json_output)

    return smart_article_dict   #Returning dictionary here, if you want json the replace it by json output

if __name__=='__main__':
    url = input('Enter the url of article')
    article(url)

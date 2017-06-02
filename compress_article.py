from newspaper import Article
import json
# import pprint
from json2html import *
import webbrowser

f = open("output_html.html",'w')

# Declarations here
url = input("Enter the url")
smart_article_dict = dict()

smart_article = Article(url)

smart_article.download()
smart_article.parse()
# smart_article.nlp()

smart_article_dict['Title'] = smart_article.title
smart_article_dict['Text'] = str(smart_article.text)
smart_article_dict['Authors'] = smart_article.authors
# smart_article_dict['Keywords'] = smart_article.keywords
# smart_article_dict['Summary'] = smart_article.summary
smart_article_dict['Publish_date'] = str(smart_article.publish_date)
smart_article_dict['Favicon_img'] = smart_article.meta_favicon

json_output = json.dumps(smart_article_dict)

# pprint.pprint(json_output)
html_output = json2html.convert(json=json_output)
# print(html_output)

f.write(html_output)
webbrowser.open_new_tab('output_html.html')
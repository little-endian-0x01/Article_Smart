from newspaper import Article
# import json
# import pprint
#from json2html import *
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
smart_article_dict['Text'] = str(smart_article.text).replace("\n","<br/>")
smart_article_dict['Authors'] = smart_article.authors
# smart_article_dict['Keywords'] = smart_article.keywords
# smart_article_dict['Summary'] = smart_article.summary
smart_article_dict['Publish_date'] = str(smart_article.publish_date.date())
smart_article_dict['Favicon_img'] = smart_article.meta_favicon

'''Uncomment below lines if you need json output, variable json_output would be the answer'''
# json_output = json.dumps(smart_article_dict)
# pprint.pprint(json_output)
# html_output = json2html.convert(json=json_output)
# print(smart_article_dict['Publish_date'])

html_open = """<html> """
f.write(html_open)
html_heading = """<center><h1>%s</h1></center>"""%(smart_article_dict['Title'])
f.write(html_heading)

for author in range(0, len(smart_article_dict['Authors'])):
    html_author = """<h4 align = "right">%s</h4>"""%((smart_article_dict['Authors'])[author])
    f.write(html_author)

html_date = """<h4 align = "right">%s</h4>"""%(smart_article_dict['Publish_date'])
f.write(html_date)
html_body = """<div class = "center"><p>%s</p></div>"""%(smart_article_dict['Text'])
f.write(html_body)
html_close = """</html>"""
f.write(html_close)


f.close()
webbrowser.open_new_tab('output_html.html')


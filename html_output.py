import json_output
import webbrowser

if __name__=='__main__':
    url = input('Enter the article url')

    content = json_output.article(url)

    f=open("output_html.html", 'w')

    html_open = """<html> """
    f.write(html_open)

    if content['Title'] != None:
        html_heading = """<center><h1>%s</h1></center>"""%(content['Title'])
        f.write(html_heading)

    if content['Authors'] != None:
        html_author = """<h4 align = "right">by %s</h4>"""%((content['Authors'])[0])
        f.write(html_author)

    if content['Publish_date'] != None:
        html_date = """<h4 align = "right">%s</h4>""" % ((str(content['Publish_date']))[:10])
        f.write(html_date)

    if content['Text'] != None:
        html_body = """%s"""%(content['Text'])
        f.write(html_body)
    html_close = """</html>"""
    f.write(html_close)

    f.close()
    webbrowser.open_new_tab('output_html.html')


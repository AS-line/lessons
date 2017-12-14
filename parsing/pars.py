import requests as req
from lxml import html

c = req.get('https://ru.wikipedia.org/')
page = html.document_fromstring(c.text)
# print(page)

div = page.find_class('mw-parser-output')
# print(div)
print(div[0].getchildren()[1].getchildren()[0].getchildren()[0].getchildren()[3].text_content())
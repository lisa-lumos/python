# 13. Web scraping with Python

## Intro
Rules of web scraping:
- Always try to get permission before scraping
- If you make too many scraping attempts, your IP address may get blocked
- Some sites automatically block scraping software

Limitations of web scraping:
- Generally every website is unique, so every web scraping script is unique
- A slight change or update to a website may completely break your web scraping script. 

To web scrape with Python, we can use the BeautifulSoup and requests (to allow for a request to the website) libraries:
- `pip install requests`
- `pip install lxml`
- `pip install bs4`

We can inspect the html elements, and see their classes, for the parts of the website that we are interested in. 

## Setting up web scraping and grab a title/class
```py
import requests
result = requests.get("http://www.example.com")
print(type(result)) # requests.models.Response
print(result.text) # return the html document contents # '<!doctype html>\n<html>\n<head>\n    <title>Example Domain</title>\n\n    <meta charset="utf-8" />\n    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />\n    <meta name="viewport" content="width=device-width, initial-scale=1" />\n    <style type="text/css">\n    body {\n        background-color: #f0f0f2;\n        margin: 0;\n        padding: 0;\n        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;\n        \n    }\n    div {\n        width: 600px;\n        margin: 5em auto;\n        padding: 2em;\n        background-color: #fdfdff;\n        border-radius: 0.5em;\n        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);\n    }\n    a:link, a:visited {\n        color: #38488f;\n        text-decoration: none;\n    }\n    @media (max-width: 700px) {\n        div {\n            margin: 0 auto;\n            width: auto;\n        }\n    }\n    </style>    \n</head>\n\n<body>\n<div>\n    <h1>Example Domain</h1>\n    <p>This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission.</p>\n    <p><a href="https://www.iana.org/domains/example">More information...</a></p>\n</div>\n</body>\n</html>\n'

import bs4 # beautifulSoup library can obtain info from html string
soup = bs4.BeautifulSoup(result.text, "lxml") # lxml is the engine to use to parse the html text
print(soup) # # makes it easy to read, in indented format, with multiple lines
print(soup.select('title')) # grab things from the html document, based on tag name, returns a list # [<title>Example Domain</title>]
print(soup.select('p')) # 
# [<p>This domain is for use in illustrative examples in documents. You may use this
#      domain in literature without prior coordination or asking for permission.</p>,
#  <p><a href="https://www.iana.org/domains/example">More information...</a></p>]
print(soup.select('title')[0].getText()) # getText() method removes the tag name in the specified bs4 object element # 'Example Domain'
print(soup.select('div')) # returns all elements with a 'div' tag
print(soup.select('#my_id')) # returns elements with this id
print(soup.select('.my_class')) # returns elements with this class
print(soup.select('div span')) # returns elements with tag name 'span' within a 'div' element
print(soup.select('div > span')) # returns elements with tag name 'span' directly within a div element, with nothing in between
```

Another example:
```py
import requests
import bs4
res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text, 'lxml')
print(soup.select('div .vector-toc-text'))
# Output exceeds the size limit. Open the full output data in a text editor
# [<div class="vector-toc-text">(Top)</div>,
#  <div class="vector-toc-text">
#  <span class="vector-toc-numb">1</span>Early life and education</div>,
#  <div class="vector-toc-text">
#  <span class="vector-toc-numb">2</span>Career</div>,
#  <div class="vector-toc-text">
#  <span class="vector-toc-numb">2.1</span>World War II</div>,
#  <div class="vector-toc-text">
#  <span class="vector-toc-numb">2.2</span>UNIVAC</div>,
#  <div class="vector-toc-text">
#  <span class="vector-toc-numb">2.3</span>COBOL</div>,
#  <div class="vector-toc-text">
#  <span class="vector-toc-numb">2.4</span>Standards</div>,
#  <div class="vector-toc-text">
#  <span class="vector-toc-numb">3</span>Retirement</div>,
#  <div class="vector-toc-text">
#  <span class="vector-toc-numb">4</span>Post-retirement</div>,
#  <div class="vector-toc-text">
#  <span class="vector-toc-numb">5</span>Anecdotes</div>,
#  <div class="vector-toc-text">
#  <span class="vector-toc-numb">6</span>Death</div>,
#  <div class="vector-toc-text">
#  <span class="vector-toc-numb">7</span>Dates of rank</div>,
#  <div class="vector-toc-text">
#  <span class="vector-toc-numb">8</span>Awards and honors</div>,
# ...
#  <span class="vector-toc-numb">13</span>References</div>,
#  <div class="vector-toc-text">
#  <span class="vector-toc-numb">14</span>Further reading</div>,
#  <div class="vector-toc-text">
#  <span class="vector-toc-numb">15</span>External links</div>]
print(soup.select('div .vector-toc-text')[1].text) # '\n1Early life and education'
for item in soup.select('div .vector-toc-text'):
    print(item.getText())
# Output exceeds the size limit. Open the full output data in a text editor
# (Top)

# 1Early life and education

# 2Career

# 2.1World War II

# 2.2UNIVAC

# 2.3COBOL

# 2.4Standards

# 3Retirement

# 4Post-retirement

# 5Anecdotes

# 6Death

# 7Dates of rank

# 8Awards and honors
# ...

# 14Further reading

# 15External links

```
























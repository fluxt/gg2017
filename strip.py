# wtf am I doing trying to strip angular frontend

from bs4 import BeautifulSoup as bs
from bs4 import Comment
import os

# WARNING: 50% HACK and 50% LAZINESS

for f in os.listdir():
    if f.endswith(".html"):
        filename = str(f)
        soup = bs(open(filename), "html.parser")

        elems = soup('script')

        # stop tracking me google
        if len(elems) == 4:
            elems[0].decompose()
            elems[2].decompose()
            elems[3].decompose()

        elems = soup('md-toolbar')
        if len(elems) == 1:
            elems[0].decompose()

        elems = soup('button')
        if len(elems) == 1:
            elems[0].decompose()

        elems = soup('md-card-title')
        if len(elems) == 1:
            elems[0].decompose()

        elems = soup.find_all(class_="solved")

        for elem in elems:
            elem['class'].remove('solved')

        comments = soup.findAll(text=lambda text:isinstance(text, Comment))
        [comment.extract() for comment in comments]

        with open(filename, "w") as f:
            f.write(soup.prettify())

''' A Module Description '''
from app.Post import Post

from masonite.facades.Auth import Auth
from slugify import slugify

import re
import unidecode

def slugify(text):
    text = unidecode.unidecode(text).lower()
    return re.sub(r'\W+', '-', text)

class NewPostController(object):
    ''' Home Blog Dashboard Controller '''

    def __init__(self):
        pass

    def show(self, Request, Application):
        """ Blog controller for Dashboard"""

        # if not Auth(Request).user():
        #     Request.redirect('/login')

        # return view('dashboard/blog/new', {'app': Application, 'Auth': Auth(Request)})
        return view('create')

    def store(self, Request):
        """ Create new post """

        title = Request.input('title')
        slug = slugify(title)
        category = Request.input('category')
        body = Request.input('body')

        Post.create(
            title=title,
            slug=slug,
            category=category,
            body=body,
            # author_id=Request.user().id
            author_id=1
        )

        return 'post created'

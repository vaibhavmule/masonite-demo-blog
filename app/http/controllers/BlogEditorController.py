''' A Module Description '''
from app.Post import Post

from masonite.facades.Auth import Auth
# from slugify import slugify

import re
import unidecode


def slugify(text):
    text = unidecode.unidecode(text).lower()
    return re.sub(r'\W+', '-', text)


class BlogEditorController(object):
    ''' Home Blog Dashboard Controller '''

    def __init__(self):
        pass

    def show(self, Request):
        """ Blog controller for Dashboard"""

        if not Auth(Request).user():
            Request.redirect('dashboard')

        posts = Post.all()

        return view('dashboard/blog', {'Auth': Auth(Request),
                                       'posts': posts})

    def show_create(self, Request):
        """ Blog controller for Dashboard"""

        if not Auth(Request).user():
            Request.redirect('/dashboard')

        return view('dashboard/post/create', {'Auth': Auth(Request)})

    def create(self, Request):
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

        return view('dashboard/blog', {'Auth': Auth(Request)})

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

    def show_all(self, Request):
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

        if not Auth(Request).user():
            Request.redirect('/dashboard')

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

    def show_update(self, Request):

        if not Auth(Request).user():
            Request.redirect('/dashboard')

        # Get post via slug
        slug = Request.param('id')
        posts = Post.where('slug', slug).get()
        post = posts[0]

        return view('dashboard/post/update', {'post': post, 'Auth': Auth(Request)})

    def update(self, Request):

        if not Auth(Request).user():
            Request.redirect('/dashboard')

        slug = Request.param('id')
        posts = Post.where('slug', slug).get()
        post = posts[0]

        post.title = Request.input('title')
        post.body = Request.input('body')

        post.save()

        return view('dashboard/blog', {'Auth': Auth(Request)})

    def show_delete(self, Request):

        if not Auth(Request).user():
            Request.redirect('/dashboard')

        slug = Request.param('id')
        posts = Post.where('slug', slug).get()
        post = posts[0]

        return view('dashboard/post/delete', {'post': post, 'Auth': Auth(Request)})

    def delete(self, Request):

        if not Auth(Request).user():
            Request.redirect('/dashboard')

        slug = Request.param('id')
        posts = Post.where('slug', slug).get()
        post = posts[0]        
        post.delete()
        return view('dashboard/blog', {'Auth': Auth(Request)})
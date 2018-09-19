''' A Module Description '''
from mistune import Markdown
from app.Post import Post
from masonite.facades.Auth import Auth


class PostsController(object):
    ''' Home Blog Controller '''

    def __init__(self):
        self.markdown = Markdown()

    def show_all(self):
        """ Blog controller for Dashboard"""
        posts = Post.all()
        return view('blog', {'posts': posts})

    def show_one(self, Request):
        """ Blog controller for Dashboard"""

        # Get post via slug
        slug = Request.param('id')
        posts = Post.where('slug', slug).get()
        post = posts[0]
        post.body = self.markdown(post.body)
        return view('blog/post', {'post': post})
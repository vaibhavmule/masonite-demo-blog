''' A Module Description '''
from mistune import Markdown
from app.Post import Post
from masonite.facades.Auth import Auth


class PostsController(object):
    ''' Posts Controller '''

    def __init__(self):
        self.markdown = Markdown()

    def show_all(self):
        """ Controller to show all posts"""
        posts = Post.all()
        return view('blog', {'posts': posts})

    def show_one(self, Request):
        """ Controller to show single post"""

        # Get post via slug
        slug = Request.param('id')
        posts = Post.where('slug', slug).get()
        post = posts[0]
        post.body = self.markdown(post.body)
        return view('blog/post', {'post': post})

    def show_category(self, Request):
        """ Controller to show category"""

        category = Request.param('id')

        posts = Post.where('category', category).get()

        return view('blog/category', {'category': category, 'posts': posts})

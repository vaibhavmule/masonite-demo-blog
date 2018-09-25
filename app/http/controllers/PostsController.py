''' A Module Description '''
from app.Post import Post
from app.User import User
from masonite.facades.Auth import Auth


class PostsController(object):
    ''' Posts Controller '''

    def __init__(self):
        pass

    def show_all(self):
        """ Controller to show all posts"""
        
        posts = Post.all()
        return view('blog', {'author': User, 'posts': posts})

    def show_one(self, Request, RenderEngine):
        """ Controller to show single post"""

        # Get post via slug
        slug = Request.param('id')
        posts = Post.where('slug', slug).get()
        post = posts[0]
        post.body = RenderEngine(post.body)

        return view('blog/post', {'author': User,'post': post})

    def show_category(self, Request):
        """ Controller to show category"""

        category = Request.param('id')

        posts = Post.where('category', category).get()

        return view('blog/category', {'category': category, 'posts': posts})

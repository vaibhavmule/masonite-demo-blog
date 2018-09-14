''' A Module Description '''
from app.Post import Post

class AllPostsController(object):
    ''' Home Blog Controller '''

    def __init__(self):
        pass

    def show(self):
        """ Blog controller for Dashboard"""
        posts = Post.all()
        return view('posts', {'posts': posts})
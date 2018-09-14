''' A Module Description '''
from app.Post import Post

class ShowPostController:
    ''' Class Docstring Description '''

    def __init__(self):
        pass

    def show(self, Request):
        """ Blog controller for Dashboard"""
        slug = Request.param('id')
        return slug
        # post = Post.where('slug', str(slug))
        # return view('post', {'post': post})

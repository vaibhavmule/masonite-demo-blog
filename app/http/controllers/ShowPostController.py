''' A Module Description '''
from app.Post import Post

class ShowPostController:
    ''' Class Docstring Description '''

    def __init__(self):
        pass

    def show(self, Request):
        """ Blog controller for Dashboard"""

        # Get post via slug
        slug = Request.param('id')
        posts = Post.where('slug', slug).get()
        post = posts[0]
        return view('blog/post', {'post': post})

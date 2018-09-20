''' A Module Description '''
import re
import unidecode

from app.Post import Post
from masonite.facades.Auth import Auth
    

def slugify(text):
    # helper function that creates slugs for the articles
    text = unidecode.unidecode(text).lower()
    return re.sub(r'\W+', '-', text)


class BlogEditorController(object):
    ''' Dashboard Blog Controller '''

    def __init__(self):
        pass
        

    def show_all(self, Request):
        """ Display all posts in blog editor """

        if not Auth(Request).user():
            Request.redirect('dashboard')

        posts = Post.all()

        return view('dashboard/blog', {'Auth': Auth(Request),
                                       'posts': [post for post in posts]})

    def show_create(self, Request):
        """ Display page to create post"""

        if not Auth(Request).user():
            Request.redirect('/dashboard')

        return view('dashboard/post/create', {'Auth': Auth(Request)})

    def create(self, Request, Upload):
        """ Create new post """

        if not Auth(Request).user():
            Request.redirect('/dashboard')

        # Make slug
        slug = slugify(Request.input('body'))

        # Save image
        try:
            image=Upload.driver('disk').store(Request.input('file_upload'), location='storage/blog/img')
        except AttributeError:
            # If user did not pick image, set image to none. (Load default)
            image="nightlife1.jpg"
        

        Post.create(
            title=Request.input('body'),
            slug=slug,
            category=Request.input('category'),
            body=Request.input('body'),
            image=image,
            author_id=1
        )

        return view('dashboard/blog', {'Auth': Auth(Request)})

    def show_update(self, Request):
        """ Display Post Update page """

        if not Auth(Request).user():
            Request.redirect('/dashboard')

        # Get post via slug
        slug = Request.param('id')
        posts = Post.where('slug', slug).get()
        post = posts[0]

        return view('dashboard/post/update', {'post': post, 'Auth': Auth(Request)})

    def update(self, Request):
        """ Update Post Controller """

        if not Auth(Request).user():
            Request.redirect('/dashboard')

        slug = Request.param('id')
        posts = Post.where('slug', slug).get()
        post = posts[0]

        # Updates Post
        post.title = Request.input('title')
        post.slug = slugify(post.title)
        post.body = Request.input('body')
        post.category = Request.input('category')

        post.save()

        return view('dashboard/blog', {'Auth': Auth(Request)})

    def show_delete(self, Request):
        """ Display Post Delete page """


        if not Auth(Request).user():
            Request.redirect('/dashboard')

        slug = Request.param('id')
        posts = Post.where('slug', slug).get()
        post = posts[0]

        return view('dashboard/post/delete', {'post': post, 'Auth': Auth(Request)})

    def delete(self, Request):
        """ Delete Post Controller """

        if not Auth(Request).user():
            Request.redirect('/dashboard')

        slug = Request.param('id')
        posts = Post.where('slug', slug).get()
        post = posts[0]
        post.delete()
        return view('dashboard/blog', {'Auth': Auth(Request)})

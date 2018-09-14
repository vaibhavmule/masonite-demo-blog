''' A Module Description '''
from masonite.facades.Auth import Auth

class AllPostsController(object):
    ''' Home Blog Dashboard Controller '''

    def __init__(self):
        pass

    def show(self, Request, Application):
        """ Blog controller for Dashboard"""

        if not Auth(Request).user():
            Request.redirect('/login')
        return view('dashboard/blog/all', {'app': Application, 'Auth': Auth(Request)})
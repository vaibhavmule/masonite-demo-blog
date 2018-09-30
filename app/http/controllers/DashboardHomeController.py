''' Dashboard Controller '''
from masonite.facades.Auth import Auth

class DashboardHomeController(object):
    ''' Home Dashboard Controller '''

    def __init__(self):
        pass

    def show(self, Request, Application):
    	""" Show Dasboard page """

        if not Auth(Request).user():
            Request.redirect('/login')

        return view('auth/home', {'app': Application, 'Auth': Auth(Request)})
